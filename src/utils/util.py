import pandas as pd
from pandas import DataFrame

def find_ideal(train_column: DataFrame, ideal: DataFrame) -> dict:
   ideal= ideal.loc[:, ideal.columns != 'x']
   deviations= pd.DataFrame()
   for i, column in enumerate(ideal.columns):
       deviations[column] = (train_column - ideal[column])**2
    
   result = {}
   result['ideal'] = deviations.sum().idxmin()
   result['deviation'] = deviations.sum().min()

   return result