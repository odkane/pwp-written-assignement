import math
import pandas as pd
from pandas import DataFrame

FACTOR = math.sqrt(2)

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

def find_test_ideal(ideals: list[dict], df_ideals: DataFrame) -> DataFrame:
    df_test = pd.read_csv('src/resources/test.csv')
     
    deviations = pd.DataFrame()
    ideal_max_deviations = []
    ideals_lst = []
    deviations = df_test
    
    for ideal in ideals:
        ideal_col= ideal.get('ideal')
        ideal_max_deviations.append((ideal.get('deviation'))* FACTOR)
        ideals_lst.append(ideal_col)

        merged_df = df_test.merge(df_ideals[['x',ideal_col]], on='x')
        deviations[ideal_col] = (merged_df['y'] - merged_df[ideal_col]).abs()
    
    deviations['max'] = deviations.loc[:, deviations.columns != 'x'].max(axis=1)
    deviations['ideal_col_max'] = deviations.loc[:, deviations.columns != 'x'].idxmax(axis=1)

    tmp = {}
    tmp['ideal_deviation_max'] = ideal_max_deviations
    tmp['ideal_col_max'] = ideals_lst 

    df_tmp = pd.DataFrame(tmp)
    deviations = deviations.merge(df_tmp, on='ideal_col_max')
    deviations['ideal'] = deviations.loc[deviations['max'] <= deviations['ideal_deviation_max'], 'ideal_col_max']
    print(deviations)
    clean_deviations = deviations.dropna()
    clean_deviations.set_index('x').sort_index().to_csv('deviations1.csv')
    # df_test = df_test.merge(clean_deviations[['x','max', 'ideal']],right_on=['x','y'],left_on=['x','y'], how='left')
  #  df_test['ideal'] = deviations.loc[deviations['max'] <= deviations['ideal_deviation_max'], 'ideal_col_max']

    return clean_deviations[['x','y','max','ideal']].rename(columns={"max":"delta_y"})
