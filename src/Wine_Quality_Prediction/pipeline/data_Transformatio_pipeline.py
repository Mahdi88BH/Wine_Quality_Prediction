from src.Wine_Quality_Prediction.config.configuration import ConfigurationManager
from src.Wine_Quality_Prediction.components.data_Transformation import DataTransformation
from src.Wine_Quality_Prediction import logger
from pathlib import Path

STAGE_NAME = "Data Validation Stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_transformation(self):

        try:
            with open(Path('artifacts/data_validation/status.txt'), 'r') as f:
                status = f.read().split(" ")[-1]
            if status == 'True':
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_spliting()
            else:
                print(status)
                raise Exception("Your data schema is not Valid")
                    
        except Exception as e:
            print(e)



