import json
from sqlalchemy import Engine, insert, delete, select
from sqlalchemy.orm import Session
import pandas as pd
from pandas import DataFrame
from databases.orm import Base


class DatabaseService:
    engine: Engine
    session: Session

    def __init__(self, engine:Engine):
        self.engine = engine
        self.session = Session(engine)
        
    def insert_from_file(self, filename:str, table:Base) -> None:
        df = pd.read_csv(rf'src/resources/{filename}')
        df_as_dict = df.head(15).to_dict('records')
 #       print(df.iloc[:20].sort_values('x'))
 #       print(json.dumps(df_as_dict, indent=4))
        self.insert_in_table(table=table, values=df_as_dict)
        

    def insert_in_table(self, table:Base, values) -> None:
        delete_stmt = delete(table)
        insert_stmt = insert(table).values(values)
        with self.engine.connect() as conn:
            conn.execute(delete_stmt)
            conn.execute(insert_stmt)
            conn.commit()

    def get_data_from_table(self, table: Base) -> DataFrame:
        return pd.read_sql_query(sql = self.session.query(table).statement, con = self.engine)
    
     
    def get_data(self, table: Base) -> DataFrame:
        select_stmt = select()
        return pd.read_sql_query(sql = self.session.query(table).add_columns().statement, con = self.engine)
    

