# Complete DataScience Project

## Workflows ML Pipeline :
1. Data Ingestion
2. Data Validation
3. Data Transformation (Features Ingineering, Data Preprocessing)
4. Model Training
5. Model Evaluation 


### WorFlows Steps :
1. Update config.yaml (all_process)
2. Update Schema.yaml (validation_data)
3. Update params.yaml (model_trainer)
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py


# Wine Quality Prediction – ETL Pipeline + ElasticNet + Flask

📌 Project Overview

This project implements a complete ETL pipeline and a Machine Learning workflow to predict wine quality using the ElasticNet regression algorithm.
The solution covers every step from data ingestion and cleaning to model training and deployment through a Flask web interface.


This project focuses on building a complete ETL pipeline combined with a Machine Learning model using the ElasticNet algorithm to predict wine quality. The workflow begins with an automated Extract-Transform-Load (ETL) process that collects raw wine data from multiple sources, cleans it, handles missing values, removes outliers, and performs feature engineering to improve model performance.

After the data is prepared, an ElasticNet regression model is trained to predict wine quality based on chemical properties such as acidity, alcohol content, density, and pH. ElasticNet is chosen because it combines both L1 and L2 regularization, allowing better generalization, feature selection, and robustness to multicollinearity within the dataset.

Once the model is trained and evaluated, it is integrated into a Flask web application. The application provides a simple interface where users can input wine characteristics and obtain a real-time prediction of wine quality. The interface also exposes the ETL workflow summary, model performance metrics, and prediction results.

Overall, the project demonstrates a complete end-to-end data engineering and machine learning pipeline, from raw data ingestion to model deployment via a lightweight web interface.