from abc import ABC, abstractmethod
import pandas as pd

class DataInspectionStrategy(ABC):
    def inspect(self, df: pd.DataFrame):
        pass


class DataTypesInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        print("\n Data Types and non-null Counts:")
        print(df.info())


class SummaryStatisticsInspectionStrategy(DataInspectionStrategy):
    def inspect(self, df: pd.DataFrame):
        
        print("Summary Statistics (Numerical features) : ")
        print(df.describe())
        print("\n Summary Statistics (Categorical features): ")
        print(df.select_dtypes(include=['object']).describe())


class Inspector:
    def inspect_data(self, df : pd.DataFrame , strategy:str) -> DataInspectionStrategy:
        if strategy=="DataType Inspection":
            return DataTypesInspectionStrategy().inspect(df)
        if strategy=="SummaryStatistics":
            return SummaryStatisticsInspectionStrategy().inspect(df)
        


if __name__=="__main__":
    inspection = Inspector()
    

    pass



