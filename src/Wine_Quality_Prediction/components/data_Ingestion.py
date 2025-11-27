import os
import urllib.request as request
from src.Wine_Quality_Prediction import logger
import zipfile
from src.Wine_Quality_Prediction.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        filename = os.path.basename(self.config.local_data_file)
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} Download! with following info: \n {headers}")
        else:
            logger.info(f"The {filename} is already exist")
    

    def extract_zip_file(self):
        """
        zip_file_path : str
        Extracts the zip file into the data directory
        Function return None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(path=unzip_path)
            zip_ref.close()