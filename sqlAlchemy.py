from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import mapper, sessionmaker

dbPath = r'C:\webDev\pycharm\dieta\db\user.db'
engine = create_engine('sqlite:///' + dbPath, echo=True)

metadata = MetaData(engine)
symptoms = Table('symptoms', metadata, autoload=True)

print(symptoms)