import numpy as np
import pandas as pd
import logging
from abc import ABC, abstractmethod
import seaborn as sns
import matplotlib.pyplot as plt


class OutlierDetectionStrategy(ABC):

    @abstractmethod
    def detect_outliers(self, df:pd.DataFrame) -> pd.DataFrame:
        pass


class ZScoreOutlierDetection(OutlierDetectionStrategy):
    def __init__(self, threshold=3):
        self.threshold = threshold

    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outliers using Z-Score method")
        z_scores = np.abs((df - df.mean())/df.std())
        outliers = z_scores>self.threshold
        logging.info(f"Outliers detected using Z score: {outliers}")
        return outliers
    
class IQROutlierDetection(OutlierDetectionStrategy):
    def detect_outliers(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info("Detecting outliers using IQR")
        Q1 = df.quantile(0.25)
        Q3 = df.quantile(0.75)
        IQR = Q3 - Q1
        outliers = (df < (Q1 - 1.5 * IQR) ) | (df > (Q3 + 1.5 * IQR))
        logging.info(f"Outliers detected using IQR: {outliers}")
        return outliers
    

class OutlierDetector:
    def __init__(self, strategy: OutlierDetectionStrategy):
        self.strategy = strategy
    def set_strategy(self, strategy : OutlierDetectionStrategy):
        logging.info("Switching the outlier detection strategy")
        self.strategy = strategy
    def detect_outliers(self, df:pd.DataFrame)->pd.DataFrame:
        logging.info("Executing outlier detection strategy")
        return self.strategy.detect_outliers(df)
    
    def handle_outliers(self, df:pd.DataFrame, method="remove", **kwargs) -> pd.DataFrame:
        outliers = self.detect_outliers(df)
        if method=="remove":
            logging.info("Removing outliers from the dataset")
            df_cleaned = df[(~outliers).all(axis=1)]
        elif method=="cap":
            logging.info("Capping outliers in the dataset")
            df_cleaned = df.clip(lower=df.quantile(0.01), upper=df.quantile(0.99), axis=1)
        else:
            logging.warning(f"Unknown method : {method}. No outlier handled")
            return df
        
        logging.info("Outlier handling completed")
        return df_cleaned
    
    def visualize_outliers(self, df:pd.DataFrame, features :list = None):
        logging.info(f"Visualizing outliers for features: {features}")
        for feature in features:
            plt.figure(figsize=(10,5))
            sns.boxplot(x=df[feature])
            plt.title(f"Boxplot of {feature}")
            plt.show()