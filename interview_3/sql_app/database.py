from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "postgres://csmioatpgikziv:824d42b1351211dc23033d47acd0387d4aa315a48123b85f6d83cc88b3010cf4@ec2-174-129-27-3.compute-1.amazonaws.com:5432/dbb0f21vsr7v0b"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()