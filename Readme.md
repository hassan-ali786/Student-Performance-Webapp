# Student Performance Predictor (Flagship ML Project)

---

## **Overview**
---

The **Student Performance Predictor** is a machine learning web application that predicts whether a student will **pass or fail** based on demographic and educational factors.

This project demonstrates a complete machine learning workflow including **data preprocessing, model training, model comparison, and deployment using a web application**.

The system compares multiple machine learning models and automatically selects the best performing model for predictions.

---

## **Features**
---

- **Multiple Machine Learning Models**

  - Logistic Regression  
  - Random Forest  
  - Gradient Boosting  

- **Automatic Best Model Selection**

- **Model Accuracy Comparison**

- **Prediction Confidence Score**

- **Professional Web Interface built using Flask**

- **Deployment Ready**

---

## **Dataset**
---

This project uses the **Students Performance in Exams dataset**.

Input features used:

- Gender  
- Race / Ethnicity  
- Parental Level of Education  
- Lunch Type  
- Test Preparation Course  

Target variable:

- **Pass / Fail Prediction**

---

## **Machine Learning Workflow**
---

1. Data Cleaning  
2. Feature Engineering  
3. OneHot Encoding  
4. Model Training  
5. Model Comparison  
6. Best Model Selection  
7. Web Application Integration  

---

## **Model Performance**
---

Example accuracy scores:

- **Logistic Regression:** 0.84  
- **Random Forest:** 0.91  
- **Gradient Boosting:** 0.89  

Best performing model:

**Random Forest**

---

## **Project Structure**
---

```bash
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
```

---

## **Technologies Used**
---

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-ML-orange?logo=scikit-learn)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-purple?logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-blue?logo=plotly)
![HTML](https://img.shields.io/badge/HTML-Frontend-red?logo=html5)
![CSS](https://img.shields.io/badge/CSS-Styling-blue?logo=css3)

---

## **Installation**
---

### 1 Clone the Repository

```bash
git clone https://github.com/yourusername/student-performance-predictor.git
cd student-performance-predictor
```

---

### 2 Install Dependencies

```bash
pip install flask pandas scikit-learn matplotlib
```

---

### 3 Train the Machine Learning Models

```bash
python train_model.py
```

This will train the models and save the best one:

```
model/best_model.pkl
```

---

### 4 Run the Web Application

```bash
python app.py
```

---

### 5 Open in Browser

```
http://127.0.0.1:5000
```

---

## **Future Improvements**
---

- Add more student features for better prediction  
- Create analytics dashboard for student insights  
- Deploy the application on cloud platforms  
- Store prediction history in a database  
- Add visualization for model comparison  

---

## **Author**
---

Hassan Ali  

GitHub:  
https://github.com/Hassan-Ali786

---

## **License**
---

This project is licensed under the MIT License.
