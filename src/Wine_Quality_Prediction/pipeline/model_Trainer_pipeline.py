from src.Wine_Quality_Prediction.config.configuration import (ConfigurationManager)
from src.Wine_Quality_Prediction.components.model_trainer import (ModelTrainer)
from src.Wine_Quality_Prediction import logger

STAGE_NAME = "Data Training Stage"

class ModelTrainingTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_trainig(self):
        config = ConfigurationManager()
        model_trainer_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_trainer_config)
        model_trainer.train()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
        obj = ModelTrainingTrainingPipeline()
        obj.initiate_data_trainig()
        logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e