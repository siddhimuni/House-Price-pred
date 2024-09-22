import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from abc import ABC, abstractmethod

class MultivariateAnalysis(ABC):

    def analyze(self, df: pd.DataFrame):
        self.generate_correlation_heatmap(df)
        self.generate_pairplot(df)


    @abstractmethod
    def generate_correlation_heatmap(self, df: pd.DataFrame):
        pass

    @abstractmethod
    def generate_pairplot(self, df: pd.DataFrame):
        pass


class SimpleMultivariateAnalysis(MultivariateAnalysis):

    def generate_correlation_heatmap(self, df: pd.DataFrame):
        plt.figure(figsize=(10,5))
        sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
        plt.title("Correlation Heatmap")
        plt.show()


    def generate_pairplot(self, df: pd.DataFrame):
        plt.figure(figsize=(10,5))
        sns.pairplot(df)
        plt.title("Pairplot of selected features", y=1.02)
        plt.show