import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

class UnivariateAnalysis(ABC):
    

    @abstractmethod
    def analyze(self, df: pd.DataFrame, feature : str):
        pass


class NumericalUnivariateAnalysis(UnivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature: str):
        

        plt.figure(figsize=(10,5))
        sns.histplot(df[feature], kde=True , bins=30)
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Frequency")
        plt.show()


class CategoricalUnivariateAnalysis(UnivariateAnalysis):

    def analyze(self, df: pd.DataFrame, feature: str):
        
        plt.figure(figsize=(10,5))
        sns.countplot(x=feature, data=df , palette="muted")
        plt.title(f"Distribution of {feature}")
        plt.xlabel(feature)
        plt.ylabel("Count")
        plt.xticks(rotation=45)
        plt.show()



class UnivariateAnalyzer:
    def plotting_graphs(self, df: pd.DataFrame, feature: str) -> UnivariateAnalysis:
        if df[feature].dtype == 'object':
            CategoricalUnivariateAnalysis().analyze(df, feature)
        else:
            NumericalUnivariateAnalysis().analyze(df, feature)
        

if __name__=="__main__":
    anal = UnivariateAnalyzer()
    

    pass



