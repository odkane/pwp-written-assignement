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
        print(df)
        plot = df.plot(x='x', y=[train_col, ideal_col])
        plot.set_xlabel('[x]')
        plot.set_ylabel('[y]')
        
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