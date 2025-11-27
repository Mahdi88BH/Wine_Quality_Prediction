import os
import pandas as pd
import joblib
from sklearn.linear_model import ElasticNet
from src.Wine_Quality_Prediction import logger
from src.Wine_Quality_Prediction.entity.config_entity import ModelTrainingConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    def train(self):
        train_df = pd.read_csv(self.config.train_data_path)
        test_df = pd.read_csv(self.config.test_data_path)

        train_X = train_df.drop([self.config.target_column], axis=1)
        test_X = test_df.drop([self.config.target_column], axis=1)
        train_y = train_df[[self.config.target_column]]
        test_y = test_df[[self.config.target_column]]

        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=88)
        lr.fit(train_X, train_y)

        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))