import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier

from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("StudentsPerformance.csv")

# Create target
df["average"] = (df["math score"] + df["reading score"] + df["writing score"]) / 3
df["result"] = df["average"].apply(lambda x: 1 if x >= 50 else 0)

df = df.drop(["math score","reading score","writing score","average"], axis=1)

X = df.drop("result", axis=1)
y = df["result"]

# Preprocessing
preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), X.columns)
    ]
)

# Models
models = {
    "Logistic Regression": LogisticRegression(),
    "Random Forest": RandomForestClassifier(),
    "Gradient Boosting": GradientBoostingClassifier()
}

scores = {}
trained_models = {}

# Train models
for name, model in models.items():
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])
    
    X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    
    pipeline.fit(X_train, y_train)
    
    preds = pipeline.predict(X_test)
    
    acc = accuracy_score(y_test, preds)
    
    scores[name] = acc
    trained_models[name] = pipeline
    
    print(name, acc)

# Select best model
best_model_name = max(scores, key=scores.get)
best_model = trained_models[best_model_name]

print("Best Model:", best_model_name)

# Save best model
pickle.dump(best_model, open("best_model.pkl","wb"))
pickle.dump(scores, open("model_scores.pkl","wb"))

# Accuracy chart
plt.bar(scores.keys(), scores.values())
plt.title("Model Accuracy Comparison")
plt.savefig("static/accuracy.png")

print("Training Complete")