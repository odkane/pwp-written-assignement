import math
from typing import List
import pandas as pd
from pandas import DataFrame


FACTOR = math.sqrt(2)

def find_train_ideal(train_column: DataFrame, df_ideal: DataFrame) -> dict:
   df_ideals= df_ideal.loc[:, df_ideal.columns != 'x']
   deviations= pd.DataFrame()
   for column in df_ideals.columns:
       deviations[column] = (train_column - df_ideal[column])**2
    

 #  print(deviations.sum()) 
   ideal = deviations.sum().idxmin()
   df = (train_column-df_ideal[ideal]).abs()

   result = {}
   result['ideal'] = ideal
   result['max_deviation']= (df.max())*FACTOR
   result['ls_deviation'] = deviations.sum().min()

   return result

def find_test_ideals(max_deviations: dict, df_ideal: DataFrame) -> List[DataFrame]:
    df_test = pd.read_csv('src/resources/test.csv')
    
    test_ideals = []
    for ideal in max_deviations.keys():
        df = df_test.merge(df_ideal[['x', ideal]], on='x')
        df['delta_y'] = (df['y'] - df[ideal]).abs()
        df.loc[df['delta_y'] <= max_deviations.get(ideal), 'ideal'] = ideal
        test_ideals.append(df.loc[:, df.columns != ideal].dropna())

    return test_ideals