from pathlib import Path
from databases.database import create_tables
import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from databases.orm import Ideal, Test, Train
from services.database_service import DatabaseService
from utils.util import find_ideal

db_name = 'task_database.db'
db_path= Path(db_name).absolute()
engine =  create_engine(rf"sqlite:///{db_path}")

def create_session() -> Session:
    return Session(engine)
    

if __name__ == '__main__':
    create_tables(db_name)
    db_service = DatabaseService(engine=engine)
    db_service.insert_from_file('train.csv', Train)
    db_service.insert_from_file('ideal.csv', Ideal)
    df_train = db_service.get_data_from_table(Train)
    df_ideal = db_service.get_data_from_table(Ideal)

    result = find_ideal(df_train['y1'],df_ideal)

    print(result)