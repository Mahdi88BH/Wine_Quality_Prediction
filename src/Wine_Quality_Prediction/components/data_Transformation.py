import os
import pandas as pd
from src.Wine_Quality_Prediction.entity.config_entity import DataTransformationConfig
from sklearn.model_selection import train_test_split
from src.Wine_Quality_Prediction import logger


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config= config
    
    ## Add the different data transformation technique such as Scaler, PCA

    def train_test_spliting(self):
        df=pd.read_csv(self.config.data_path, delimiter=";")

        # Split the data into train test split
        train, test = train_test_split(df)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        logger.info("Splited Data into train test split")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)