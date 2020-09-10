import requests
import database
import pandas as pd
from tqdm import tqdm
from sqlalchemy.orm import sessionmaker


def extract():
    ''' Extract data from API '''
    req = requests.get('http://dataeng.quero.com:5000/caged-data')
    req.raise_for_status()
    try:
        return req.json()['caged']
    except KeyError:
        raise KeyError('Conteúdo do retorno da API desconhecido')


def transform(json_data):
    ''' Data transformation stage '''
    transformed_data = pd.DataFrame(json_data)
    float_columns = ['salario', 'saldo_movimentacao']
    for column in float_columns:
        transformed_data[column] = pd.to_numeric(
            transformed_data[column].str.replace(',', ''))
    return transformed_data.to_dict(orient='records')


def load(data):
    ''' Insert or update data in the target database '''
    db_engine = database.initialize()
    db_session = sessionmaker(bind=db_engine)()
    generator_data = (database.models.Caged(**caged) for caged in data)
    for caged in tqdm(generator_data, total=len(data)):
        db_session.merge(caged)
    db_session.commit()


def run():
    try:
        print('[+] Extraindo dados')
        data = extract()
    except Exception as err:
        raise Exception('[-] Não foi possível acessar a API: ' + str(err))
    try:
        print('[+] Tratando dados coletados')
        data = transform(data)
    except Exception as err:
        raise Exception('[-] Não foi possível tratar os dados: ' + str(err))
    try:
        print('[+] Gravando os dados tratados')
        load(data)
    except Exception as err:
        raise Exception('[-] Não foi possível gravar no banco de dados: ' + str(err))


if __name__ == '__main__':
    try:
        run()
        print('[+] Processo finalizado com sucesso!')
    except Exception as err:
        print(err)
