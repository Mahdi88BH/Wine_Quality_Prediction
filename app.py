from flask import Flask, render_template, request
import os
import numpy as np
from src.Wine_Quality_Prediction.pipeline.prediction_pipeline import PredictionPipeline

app = Flask(__name__)

@app.route('/', methods=['GET'])
def homePage():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def trainPipeline():
    os.system('python main.py')
    return 'Training Successful!'

@app.route('/prediction_result', methods=['POST', 'GET'])
def resultPage():
    if request.method == 'POST':
        try:
            quality_features = [float(feature) for feature in request.form.values()]
            final_features = np.array(quality_features).reshape(1, -1)

            pipeline = PredictionPipeline()
            prediction = pipeline.predict(final_features)

            return render_template('result.html', prediction=str(prediction[0]))
        except Exception as e:
            return f'Error occurred: {e}'
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)