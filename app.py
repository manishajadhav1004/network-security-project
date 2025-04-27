from flask import Flask, request, render_template
import pandas as pd
import numpy as np

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application

## Home Page Route
@app.route('/')
def index():
    return render_template('index.html') 

## Prediction Page Route
@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        data = CustomData(
            network_packet_size = float(request.form.get('network_packet_size')),
            login_attempts = int(request.form.get('login_attempts')),
            session_duration = float(request.form.get('session_duration')),
            ip_reputation_score = float(request.form.get('ip_reputation_score')),
            failed_logins = int(request.form.get('failed_logins')),
            unusual_time_access = int(request.form.get('unusual_time_access')),
            protocol_type = request.form.get('protocol_type'),
            encryption_used = request.form.get('encryption_used'),
            browser_type = request.form.get('browser_type')
        )

        pred_df = data.get_data_as_data_frame()
        print(pred_df)
        print("Before Prediction")

        predict_pipeline = PredictPipeline()
        print("Mid Prediction")
        results = predict_pipeline.predict(pred_df)
        print("After Prediction")

        return render_template('home.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)