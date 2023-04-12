import pandas as pd
from pandas import DataFrame

def find_ideal(train_column: DataFrame, ideal: DataFrame) -> dict:
   ideal= ideal.loc[:, ideal.columns != 'x']
   deviations= pd.DataFrame()
   for column in ideal.columns:
       deviations[column] = (train_column - ideal[column])**2
    
 #  print(deviations.sum()) 
   result = {}
   result['ideal'] = deviations.sum().idxmin()
   result['deviation'] = deviations.sum().min()

   return result

def find_test_ideal(ideals) -> DataFrame:
    df_test = pd.read_csv('src/resources/test.csv')
    return df_test
