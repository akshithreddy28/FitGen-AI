from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("model/fitness_model.pkl")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/dashboard", methods=["POST"])
def dashboard():

    age = int(request.form["age"])
    gender = int(request.form["gender"])
    height = float(request.form["height"])
    weight = float(request.form["weight"])
    activity = int(request.form["activity"])
    goal = int(request.form["goal"])

    prediction = model.predict([[age, gender, height, weight, activity, goal]])

    calories = round(prediction[0])

    bmi = weight / ((height / 100) ** 2)
    bmi = round(bmi, 2)

    if bmi < 18.5:
        fitness_status = "Underweight"
    elif bmi < 25:
        fitness_status = "Healthy"
    elif bmi < 30:
        fitness_status = "Overweight"
    else:
        fitness_status = "Obese"

    if goal == 1:
        workout = "Cardio + Full Body Workout"
        tip = "Maintain a calorie deficit and stay hydrated."
    elif goal == 2:
        workout = "Upper / Lower Split"
        tip = "Maintain a balanced diet and exercise regularly."
    else:
        workout = "Push Pull Legs (PPL)"
        tip = "Increase protein intake and focus on strength training."

    return render_template(
        "dashboard.html",
        age=age,
        height=height,
        weight=weight,
        calories=calories,
        bmi=bmi,
        fitness_status=fitness_status,
        workout=workout,
        tip=tip
    )


if __name__ == "__main__":
    app.run(debug=True)