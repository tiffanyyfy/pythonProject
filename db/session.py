from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from common.config import config


SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://' \
                          f'{config.get_username}:' \
                          f'{config.get_password}@' \
                          f'{config.get_server}:' \
                          f'{config.get_port}/' \
                          f'{config.get_dbname}'

engine = create_engine(SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine, expire_on_commit=True, autocommit=False)

Base = declarative_base()

