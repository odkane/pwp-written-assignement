import abc
from pandas import DataFrame
import matplotlib.pyplot as plt
from sqlalchemy import Engine

from services.database_service import DatabaseService 

class PlottingService:
    def __init__(self,engine: Engine):
        self.db_service = DatabaseService(engine=engine)

    def plot_and_save(self, train_col:str, ideal_col:str) -> None:
        df_train = self.db_service.get_data_from_train(train_col)
        df_ideal = self.db_service.get_data_from_ideal(ideal_col)
        df = df_train.merge(df_ideal, on='x')
        df_train['deviation'] = (df_train[train_col]-df_ideal[ideal_col])**2
        # print(df)
        ax = df_train.plot(x='x', y=train_col, yerr='deviation')
        df_ideal.plot(x='x', y=ideal_col, ax=ax)
        
        ax.set_xlabel('[x]')
        ax.set_ylabel('[y]')
        
        plt.show()

    def plot_test(self):
        df_test = self.db_service.get_data_from_test_table()

        ideals = df_test['ideal'].unique()

        fig, axes = plt.subplots(nrows=len(ideals))

        for i, ideal in enumerate(ideals):
            print(str(i) + ideal)
            df :DataFrame = df_test.loc[df_test['ideal'] == ideal]
            df_ideal = self.db_service.get_data_from_ideal(ideal)
            print(df)
            df.plot(x='x', y='y',yerr='delta_y', ax=axes[i])
            df_ideal.plot(x='x', y=ideal, ax=axes[i])
            
        plt.show()        
    

    @abc.abstractmethod
    def _plot():
        raise NotImplementedError
        
    @abc.abstractmethod
    def _save_plot():
        raise NotImplementedError


class MatPlottingService(PlottingService):
    pass


class BokehPlettingService(PlottingService):
    pass