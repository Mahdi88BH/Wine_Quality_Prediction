import os
from src.Wine_Quality_Prediction.entity.config_entity import ModelEvaluationConfig
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib
from mlflow.models.signature import infer_signature
from src.Wine_Quality_Prediction.utils.common import save_json
from pathlib import Path

import os

os.environ["MLFLOW_TRACKING_URL"] = "https://dagshub.com/Mahdi88BH/Wine_Quality_Prediction.mlflow"
os.environ["MLFLOW_TRACKING_USERNAME"] = "Mahdi88BH"
os.environ["MLFLOW_TRACKING_PASSWORD"] = "da1c411fd97cfb5322aaa99dd5864543daf608ae"

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
    
    def evaluate_metrics(self, current, pred):
        rmse = mean_squared_error(current, pred)
        mae = mean_absolute_error(current, pred)
        r2 = r2_score(current, pred)

        return rmse, mae, r2
    
    def log_info_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Configurer MLflow pour DagsHub
        mlflow.set_tracking_uri(self.config.mlflow_uri)
        mlflow.set_registry_uri(self.config.mlflow_uri)

        tracking_url_type_store= urlparse(mlflow.get_tracking_uri()).scheme

        # Définir l'expériment si besoin
        mlflow.set_experiment("model_evaluation")

        with mlflow.start_run():

            predict_qualities = model.predict(test_x)

            (rmse, mae, r2) = self.evaluate_metrics(test_y, predict_qualities)

            # Saving metrics as log
            scores = {"rmse": rmse, "mae": mae, "r2_score": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2_score", r2)
            
            #signature = infer_signature(test_x, predict_qualities)

            # # Model registery does not work with file store
            # if tracking_url_type_store != "file":

            #     mlflow.sklearn.log_model(model, "model", registered_model_name="ElasticNet_Modelv1")
            # else:
            #     mlflow.sklearn.log_model(model, "model")

