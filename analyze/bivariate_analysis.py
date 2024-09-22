import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class BivariateAnalysis(ABC):

    
    


    @abstractmethod

    def analyze(self, df: pd.DataFrame , feature_1: str, feature_2:str):
        pass

    
class NumericalVsNumericalAnalysis(BivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature_1: str, feature_2: str):
        plt.figure(figsize=(10,5))
        sns.scatterplot(x=feature_1, y=feature_2 , data=df)
        plt.title(f"{feature_1 } vs  {feature_2}")
        plt.xlabel(feature_1)
        plt.ylabel(feature_2)
        plt.show()

class CategoricalVsNumericalAnalysis(BivariateAnalysis):
    def analyze(self, df: pd.DataFrame, feature_1: str, feature_2: str):
        plt.figure(figsize=(10,5))
        sns.boxplot(x=feature_1, y=feature_2 , data=df)
        plt.title(f"{feature_1 } vs  {feature_2}")
        plt.xlabel(feature_1)
        plt.ylabel(feature_2)
        # plt.xticks(rotatation=45)
        plt.show()



