import numpy as np
import pandas as pd
import logging
from abc import ABC, abstractmethod
from sklearn.preprocessing import MinMaxScaler, StandardScaler, OneHotEncoder


class FeatureEngineering(ABC):

    @abstractmethod
    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        pass


class LogTransformation(FeatureEngineering):
    def __init__(self, features):
        self.features=features

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying Log Transformation to features: {self.features}")
        df_transformed = df.copy()
        for feature in self.features:
            df_transformed[feature] = np.log1p(df[feature])
        logging.info("Log Transformation completed")
        return df_transformed
    

class StandardScaling(FeatureEngineering):
    def __init__(self, features):
        self.features=features
        self.scaler=StandardScaler()

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying Standard Scaler to features : {self.features}")
        df_transformed=df.copy()
        for feature in self.features:
            df_transformed[feature] = self.scaler.fit_transform(df[feature])
        logging.info("Standard scaling completed")
        return df_transformed
    

class MinMaxScaling(FeatureEngineering):
    def __init__(self, features, feature_range = (0,1)):
        self.features=features
        self.scaler=MinMaxScaler(feature_range = feature_range)

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        logging.info(f"Applying MinMax Scaler to features : {self.features}")
        df_transformed=df.copy()
        for feature in self.features:
            df_transformed[feature] = self.scaler.fit_transform(df[feature])
        logging.info("MinMax scaling completed")
        return df_transformed


class OneHotEncoding(FeatureEngineering):
    def __init__(self, features):
        self.features=features
        self.encoder=OneHotEncoder(sparse_output=False, drop="First")

    def apply_transformation(self, df: pd.DataFrame) -> pd.DataFrame:
        
        logging.info(f"Applying One-Hot encoding to features: {self.features}")
        df_transformed=df.copy()

        encoded_data = self.encoder.fit_transform(df[self.features])
        encoded_columns = self.encoder.get_feature_names_out(self.features)
        encoded_df = pd.DataFrame(encoded_data, columns= encoded_columns, index=df.index)
        df_transformed = df_transformed.drop(columns=self.features)
        df_transformed=pd.concat([df_transformed, encoded_df], axis=1)
        logging.info("One-Hot encoding completed")
        return df_transformed
    
class FeatureEngineer:
    def __init__(self, strategy= FeatureEngineering):
        self.strategy=strategy

    def set_strategy(self, strategy=FeatureEngineering):
        logging.info("Switching feature engineering strategy")
        self.strategy=strategy

    def apply_feature_engineering(self, df:pd.DataFrame) ->pd.DataFrame:
        logging.info("Applying feature engineering strategy")
        return self.strategy.apply_transformation(df)
    

if __name__=="__main__":
    pass

        


