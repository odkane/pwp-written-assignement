import json
from pathlib import Path
import pandas as pd
from databases.database import create_tables
from sqlalchemy import create_engine

from databases.orm import Ideal, Test, Train
from services.database_service import DatabaseService
from utils.util import find_ideal, find_test_ideal

db_name = 'task_database.db'
db_path= Path(db_name).absolute()
engine =  create_engine(rf"sqlite:///{db_path}")
    

if __name__ == '__main__':
    create_tables(db_name)
    db_service = DatabaseService(engine=engine)
    db_service.insert_from_file('train.csv', Train)
    db_service.insert_from_file('ideal.csv', Ideal)
    df_train = db_service.get_data_from_table(Train)
    df_ideal = db_service.get_data_from_table(Ideal)

    train_ideals = {}
    for col in df_train.loc[:, df_train.columns != 'x'].columns:
        train_ideals[col] = find_ideal(df_train[col],df_ideal)

    df_test = find_test_ideal(train_ideals)
    
    print(json.dumps(train_ideals, indent=4))
    print(df_test.head())