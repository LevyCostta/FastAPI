from sqlalchemy import Column, Integer, Numeric, String
from shared.database import Base


class ContaPagarReceber(Base):
    __tablename__ = 'contas_pagar_receber'

    id = Column(Integer, primary_key=True, auto_increment=True)
    descricao = Column(String, index=True)
    valor = Column(Numeric)
    tipo = Column(String(30)) 
    