from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:2219499@localhost/fast-api"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
