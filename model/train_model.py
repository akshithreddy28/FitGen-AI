import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("../dataset/fitness_data.csv")

X = data[["Age", "Gender", "Height", "Weight", "Activity", "Goal"]]
y = data["Calories"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

accuracy = model.score(X_test, y_test)

print(f"Model Accuracy : {accuracy * 100:.2f}%")

joblib.dump(model, "fitness_model.pkl")

print("Model trained successfully!")
print("Model saved as fitness_model.pkl")