from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("best_model.pkl","rb"))
scores = pickle.load(open("model_scores.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html", scores=scores)

@app.route("/predict", methods=["POST"])
def predict():

    data = {
        "gender":[request.form["gender"]],
        "race/ethnicity":[request.form["race"]],
        "parental level of education":[request.form["education"]],
        "lunch":[request.form["lunch"]],
        "test preparation course":[request.form["prep"]]
    }

    df = pd.DataFrame(data)

    prediction = model.predict(df)
    probability = model.predict_proba(df)

    result = "Pass" if prediction[0]==1 else "Fail"
    confidence = round(max(probability[0])*100,2)

    return render_template("index.html",
                           prediction=result,
                           confidence=confidence,
                           scores=scores)

if __name__ == "__main__":
    app.run(debug=True)