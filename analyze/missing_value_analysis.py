import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod


class MissingValueTemplateAnalysis(ABC):

    def analyze(self, df: pd.DataFrame):
        self.identify_missing_values(df)
        self.visualize_missing_values(df)



    @abstractmethod
    def identify_missing_values(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def visualize_missing_values(self, df:pd.DataFrame):
        pass


class SimpleMissingValueAnalysis(MissingValueTemplateAnalysis):

    def identify_missing_values(self, df: pd.DataFrame):
        print("\n Missing values count by column:")
        missing_values = df.isnull().sum()
        print(missing_values[missing_values >0 ])


    def visualize_missing_values(self, df: pd.DataFrame):
        print("\n Visualizing missing values:")
        plt.figure(figsize=(12, 8))
        sns.heatmap(df.isnull(), cbar=False , cmap="viridis")
        plt.title("Missing Value Heatmap")
        plt.show()



        


    