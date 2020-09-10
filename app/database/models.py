from sqlalchemy import (
    create_engine,
    Column,
    String,
    Integer,
    Float
)
from sqlalchemy.ext.declarative import declarative_base

DeclarativeBase = declarative_base()


def connect():
    return create_engine('postgresql://quero:educacao@quero-educacao-database/caged_data')


def create_table(engine):
    DeclarativeBase.metadata.create_all(engine)


def initialize_database():
    engine = connect()
    create_table(engine)
    return engine


class Caged(DeclarativeBase):
    __tablename__ = 'caged'
    id = Column(Integer, primary_key=True)
    categoria = Column(Integer)
    cbo2002_ocupacao = Column(Integer)
    competencia = Column(Integer)
    fonte = Column(Integer)
    grau_de_instrucao = Column(Integer)
    horas_contratuais = Column(Integer)
    idade = Column(Integer)
    ind_trab_intermitente = Column(Integer)
    ind_trab_parcial = Column(Integer)
    indicador_aprendiz = Column(Integer)
    municipio = Column(Integer)
    raca_cor = Column(Integer)
    regiao = Column(Integer)
    salario = Column(Float)
    saldo_movimentacao = Column(Float)
    secao = Column(String)
    sexo = Column(Integer)
    subclasse = Column(Integer)
    tam_estab_jan = Column(Integer)
    tipo_de_deficiencia = Column(Integer)
    tipo_empregador = Column(Integer)
    tipo_estabelecimento = Column(Integer)
    tipo_movimentacao = Column(Integer)
    uf  = Column(Integer)
