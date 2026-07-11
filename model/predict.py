import joblib

model = joblib.load("fitness_model.pkl")

print("===== FitGen AI =====")

age = int(input("Age : "))
gender = int(input("Gender (Male=1 Female=0): "))
height = float(input("Height (cm): "))
weight = float(input("Weight (kg): "))
activity = int(input("Activity (1-Low 2-Moderate 3-High): "))
goal = int(input("Goal (1-Loss 2-Maintain 3-Muscle): "))

prediction = model.predict([[age, gender, height, weight, activity, goal]])

print()

print("Predicted Calories :", round(prediction[0]), "kcal/day")