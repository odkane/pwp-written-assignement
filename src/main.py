from pathlib import Path
from databases.database import create_tables
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from databases.orm import Ideal, Test, Train


db_path= Path('task_database.db').absolute()
engine =  create_engine(rf"sqlite:///{db_path}")

def create_session() -> Session:
    return Session(engine)
    


if __name__ == '__main__':
    create_tables()

    df = pd.read_sql_query(sql = create_session().query(Train.x).add_columns(Train.y2).statement, con = engine)

    print(type(df))
    print(df)
