from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine


db_url="mysql+pymysql://root:Gomathi@9305@localhost:3306/Fastapi"
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=engine)
engine=create_engine(db_url)
