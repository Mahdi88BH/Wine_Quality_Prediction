from src.Wine_Quality_Prediction import logger
from src.Wine_Quality_Prediction.pipeline.data_Ingestion_pipeline import DataIngestionTrainingPipeline
from src.Wine_Quality_Prediction.pipeline.data_Validation_pipeline import DataValidationTrainingPipeline
from src.Wine_Quality_Prediction.pipeline.data_Transformatio_pipeline import DataTransformationTrainingPipeline
from src.Wine_Quality_Prediction.pipeline.model_Trainer_pipeline import ModelTrainingTrainingPipeline
from src.Wine_Quality_Prediction.pipeline.model_Evaluation_pipeline import ModelEvaluationTrainingPipeline

logger.info("Welcome to our project Data Science Prediction to the Wine Quality")

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    raise e


STAGE_NAME = "Model Training Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    model_training = ModelTrainingTrainingPipeline()
    model_training.initiate_data_trainig()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    raise e



STAGE_NAME = "Model Evaluation Stage"
try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e