import pickle
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Load the trained model
with open('salary_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        years_experience = float(request.form['years_of_experience'])
        prediction = model.predict([[years_experience]])
        return render_template(
            'index.html',
            prediction_text=f"Predicted Salary: ${prediction[0]:,.2f}"
        )
    except Exception as e:
        return render_template('index.html', error_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
