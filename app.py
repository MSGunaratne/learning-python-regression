from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

with open('house_price_prediction.pkl', 'rb') as f:
    model = pickle.load(f);

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        feature_names = ['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT']
        features = [float(request.form[name]) for name in feature_names]
        
        features_array = np.array([features])
        prediction = model.predict(features_array)
        output = round(prediction[0],2)
        
        return render_template('index.html', prediction_text=f"Predicted Price: ${output:,}")
    except ValueError:
        return render_template('index.html', prediction_text="Error: Please enter valid numeric values for all fields.")


if __name__ == "__main__":
    # Get the PORT from environment variable or default to 10000
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)