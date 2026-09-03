from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained Multiple Linear Regression model
model = pickle.load(open("MLRModel.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/predict', methods=['POST'])
def predict():

    # Read inputs from the HTML form
    area = float(request.form['area'])
    bedrooms = float(request.form['bedrooms'])

    # Predict price
    prediction = model.predict(np.array([[area, bedrooms]]))

    return render_template(
        "index.html",
        prediction_text=f"Predicted price : {prediction[0] / 100000:.2f} Lakhs"
    )


if __name__ == "__main__":
    app.run(debug=True)