from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load Trained Logistic Regression Model
model = pickle.load(open("BCModel2.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index2.html")


@app.route('/predict', methods=['POST'])
def predict():

    # Read user inputs
    Study_Hours = float(request.form['Study_Hours'])
    Previous_Year_Marks = float(request.form['Previous_Year_Marks'])

    # Prediction
    prediction = model.predict(np.array([[Study_Hours, Previous_Year_Marks]]))

    # Convert numeric prediction to text
    if prediction[0] == 1:
        result = "Student is Pass"
    else:
        result = "Student is Fail"

    return render_template(
        "index2.html",
        prediction_text=result
    )


if __name__ == "__main__":
    app.run(debug=True)