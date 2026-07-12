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

    water = round(weight * 0.035, 2)

    protein = round(weight * 1.5)

    ideal_min = round(18.5 * ((height / 100) ** 2), 1)

    ideal_max = round(24.9 * ((height / 100) ** 2), 1)

    if age < 18:
        sleep = "8-10 Hours"
    elif age <= 64:
        sleep = "7-9 Hours"
    else:
        sleep = "7-8 Hours"

    if bmi < 18.5:
        fitness_status = "Underweight"
    elif bmi < 25:
        fitness_status = "Healthy"
    elif bmi < 30:
        fitness_status = "Overweight"
    else:
        fitness_status = "Obese"

    if goal == 1:

        goal_name = "Weight Loss"

        workout = [
            "Monday - Cardio (30 min)",
            "Tuesday - Full Body Workout",
            "Wednesday - Brisk Walking",
            "Thursday - HIIT Training",
            "Friday - Core Exercises",
            "Saturday - Cycling",
            "Sunday - Rest"
        ]

        diet = [
            "Breakfast: Oats & Eggs",
            "Lunch: Brown Rice & Chicken",
            "Dinner: Salad & Soup",
            "Snack: Fruits",
            "Drink 3L Water"
        ]

    elif goal == 2:

        goal_name = "Maintain Weight"

        workout = [
            "Monday - Upper Body",
            "Tuesday - Lower Body",
            "Wednesday - Cardio",
            "Thursday - Core Workout",
            "Friday - Full Body",
            "Saturday - Yoga",
            "Sunday - Rest"
        ]

        diet = [
            "Breakfast: Idli & Milk",
            "Lunch: Rice & Dal",
            "Dinner: Chapati & Vegetables",
            "Snack: Fruits",
            "Drink 2.5L Water"
        ]

    else:

        goal_name = "Muscle Gain"

        workout = [
            "Monday - Chest + Triceps",
            "Tuesday - Back + Biceps",
            "Wednesday - Legs",
            "Thursday - Shoulders",
            "Friday - Arms + Abs",
            "Saturday - Cardio",
            "Sunday - Rest"
        ]

        diet = [
            "Breakfast: Eggs & Milk",
            "Lunch: Rice & Chicken",
            "Dinner: Paneer & Vegetables",
            "Snack: Dry Fruits",
            "Protein Shake"
        ]

    if bmi < 18.5:

        tips = [
            "Increase calorie intake.",
            "Eat protein-rich foods.",
            "Exercise with light weights.",
            "Sleep at least 8 hours."
        ]

    elif bmi < 25:

        tips = [
            "Maintain your current diet.",
            "Exercise regularly.",
            "Drink enough water.",
            "Continue healthy habits."
        ]

    elif bmi < 30:

        tips = [
            "Reduce sugar intake.",
            "Walk 30 minutes daily.",
            "Increase vegetables.",
            "Avoid junk food."
        ]

    else:

        tips = [
            "Consult a nutritionist.",
            "Follow a calorie deficit.",
            "Exercise daily.",
            "Avoid sugary drinks."
        ]

    return render_template(
        "dashboard.html",
        age=age,
        gender=gender,
        height=height,
        weight=weight,
        calories=calories,
        bmi=bmi,
        fitness_status=fitness_status,
        water=water,
        protein=protein,
        sleep=sleep,
        ideal_min=ideal_min,
        ideal_max=ideal_max,
        goal_name=goal_name,
        workout=workout,
        diet=diet,
        tips=tips
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)