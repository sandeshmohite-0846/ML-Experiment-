from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load Trained Model
model = pickle.load(open("MCModel02.pkl", "rb"))


@app.route('/')
def home():
    return render_template("index02.html")


@app.route('/predict', methods=['POST'])
def predict():

    # Read input values
    weight_g = float(request.form['weight_g'])
    sweetness = float(request.form['sweetness'])
    size_cm = float(request.form['size_cm'])

    # Prediction
    prediction = model.predict([[weight_g, sweetness, size_cm]])

    # Convert class into fruit type
    fruit = prediction[0]

    return render_template(
        "index02.html",
        prediction_text=f"Predicted Fruit Type : {fruit}"
    )


if __name__ == "__main__":
    app.run(debug=True)
