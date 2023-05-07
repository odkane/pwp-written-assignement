import json
import math
from pathlib import Path
from databases.database import create_tables
from sqlalchemy import create_engine

from databases.orm import Ideal, Test, Train
from services.database_service import DatabaseService
from services.plotting_service import PlottingService
from utils.util import find_train_ideal, find_test_ideals


db_name = 'task_database.db'
db_path= Path(db_name).absolute()
engine =  create_engine(rf"sqlite:///{db_path}")
FACTOR = math.sqrt(2)


if __name__ == '__main__':
    create_tables(db_name)
    db_service = DatabaseService(engine=engine)
    db_service.insert_from_file('train.csv', Train)
    db_service.insert_from_file('ideal.csv', Ideal)
    df_train = db_service.get_data_from_table(Train)
    df_ideal = db_service.get_data_from_table(Ideal)

    train_ideals = {}
    ideals=[]
    max_deviations = {}
    for train_col in df_train.loc[:, df_train.columns != 'x'].columns:
        result = find_train_ideal(df_train[train_col],df_ideal)
        ideal_col = result.get('ideal')
        ideals.append(ideal_col)
        max_deviations[ideal_col] = result.get('max_deviation')
        train_ideals[train_col] = ideal_col
    
    print(train_ideals)
    print(max_deviations)
    test_ideals = find_test_ideals(max_deviations=max_deviations, df_ideal=df_ideal)
    db_service.delete_from_dataframe(table=Test)
    for df_test_ideal in test_ideals:
        db_service.insert_from_dataframe(table=Test, df=df_test_ideal)
    
    
    plt_service = PlottingService(engine=engine)
    
    for key, value in train_ideals.items():
        plt_service.plot_and_save(train_col= key, ideal_col=value)

    plt_service.plot_test_single()