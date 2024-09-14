from sqlalchemy import Column, Integer, String

from db.session import Base


class PdaUser(Base):
    __tablename__ = 'pda_user'
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    gsid = Column(Integer, default=None)
    glybh = Column(String, nullable=False)
    zsmc = Column(String, nullable=False)
    dlmc =  Column(String, nullable=False)
    dlmm = Column(String, nullable=False)
    mmyz =  Column(String, nullable=False)
    yhlx =  Column(Integer, nullable=False)


