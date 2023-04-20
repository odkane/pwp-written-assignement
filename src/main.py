import json
from pathlib import Path
from databases.database import create_tables
from sqlalchemy import create_engine

from databases.orm import Ideal, Test, Train
from services.database_service import DatabaseService
from services.plotting_service import PlottingService
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
    ideals=[]
    for col in df_train.loc[:, df_train.columns != 'x'].columns:
        ideal = find_ideal(df_train[col],df_ideal)
        ideals.append(ideal)
        train_ideals[col] = ideal.get('ideal')
    

    df_test_result = find_test_ideal(ideals, df_ideals=df_ideal)
    
    db_service.insert_from_dataframe(table=Test, df=df_test_result)
    
    plt_service = PlottingService(engine=engine)
    plt_service.plot_test()
    
    for key, value in train_ideals.items():
        plt_service.plot_and_save(train_col= key, ideal_col=value)

 #   print(df.head())

    # print(Ideal.y1)
    # for field in fields(Ideal):
    #     if ("y1" == field.name):
    #         print(field)   