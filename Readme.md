Student Performance Predictor (Flagship ML Project)
Overview

The Student Performance Predictor is a machine learning web application that predicts whether a student will pass or fail based on demographic and educational factors.

This project demonstrates a complete machine learning workflow including data preprocessing, model training, model comparison, and deployment using a web application.

It also compares multiple models and automatically selects the best performing one for predictions.

Features

Multiple Machine Learning Models

Logistic Regression

Random Forest

Gradient Boosting

Automatic Best Model Selection

Model Accuracy Comparison

Prediction Confidence Score

Professional Web Interface
Built using the Flask framework.

Deployment Ready
The application structure allows easy deployment.

Dataset

This project uses the Students Performance in Exams dataset.

Input features used:

Gender

Race / Ethnicity

Parental Level of Education

Lunch Type

Test Preparation Course

Target variable:

Pass / Fail prediction

Machine Learning Workflow

Data Cleaning

Feature Engineering

OneHot Encoding

Model Training

Model Comparison

Best Model Selection

Web Application Integration

Model Performance

Example accuracy scores:

Logistic Regression: 0.84

Random Forest: 0.91

Gradient Boosting: 0.89

Best performing model:

Random Forest

Project Structure
student-performance-predictor/

data/
    students.csv

model/
    best_model.pkl

templates/
    index.html
    result.html

static/
    css/style.css

train_model.py
app.py
requirements.txt
README.md
Technologies Used














Installation
1 Clone the Repository
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor
2 Install Dependencies
pip install flask pandas scikit-learn matplotlib
3 Train the Machine Learning Models
python train_model.py

This will train multiple models and save the best model:

model/best_model.pkl
4 Run the Web Application
python app.py
5 Open in Browser
http://127.0.0.1:5000
Future Improvements

Add more student features for better prediction

Create a dashboard for performance analytics

Deploy the application on cloud platforms

Store prediction history in a database

Add visualization for model comparison

Author

Hassan Ali

GitHub
https://github.com/Hassan-Ali786

License

This project is licensed under the MIT License.
