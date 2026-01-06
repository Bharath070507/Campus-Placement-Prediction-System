# 🎓 Campus Placement Prediction System

## 📌 Project Overview
The **Campus Placement Prediction System** is an end-to-end **Machine Learning + Web Application** that predicts whether a student will be **Placed or Not Placed** based on academic performance, skills, certifications, and background information.

This project demonstrates the **complete Machine Learning lifecycle**, including:
- Data preprocessing
- Feature engineering
- Model training and evaluation
- Model serialization
- Web deployment using Flask

---

## 🎯 Project Objective
The main objectives of this project are:
- To predict the **placement status** of a student
- To identify factors influencing campus placements
- To calculate a **performance score** for students
- To group students into **skill-based clusters**
- To deploy the trained ML model using a web interface

---

## 🗂️ Dataset Description
**Dataset Name:** Campus Placement Dataset  
**File Used:** `Placement_Data_Full_Class.csv`

### Key Features
| Feature | Description |
|-------|------------|
| ssc_p | Secondary school percentage |
| hsc_p | Higher secondary percentage |
| degree_p | Degree percentage |
| etest_p | Employability test score |
| mba_p | MBA percentage |
| gender | Gender of student |
| workex | Work experience |
| ssc_b | SSC board |
| hsc_b | HSC board |
| hsc_s | HSC stream |
| degree_t | Degree type |
| specialisation | MBA specialization |
| status | Placement status (Target variable) |

Additional features like **projects** and **certifications** were included to make the dataset more realistic.

---

## 🏗️ Project Structure
The project contains the following key files and directories:

static/
Contains the CSS file used to style the web interface.

templates/
Contains the HTML file used to collect user input and display prediction results.

app.py
- Flask application file that loads the trained machine learning models and handles user requests and predictions.

training.ipynb
- Jupyter Notebook used for data preprocessing, feature engineering, model training, and evaluation.

Placement_Data_Full_Class.csv
- Dataset used for training and testing the machine learning models.

classifier.pkl
- Trained Random Forest classification model used to predict placement status.

regressor.pkl
- Trained Random Forest regression model used to calculate the performance score.

scaler.pkl
- StandardScaler object used to normalize input features before prediction.

kmeans.pkl
- KMeans clustering model used to group students based on skill levels.

.gitignore
- File that specifies which files and folders should be ignored by Git.

README.md
- Documentation file that explains the project, its structure, and usage.


---

## 🧠 Model Training and Evaluation

### Data Preprocessing
- Removed irrelevant columns (`salary`, `sl_no`)
- Converted categorical variables using **One-Hot Encoding**
- Scaled numerical features using **StandardScaler**

### Models Used
- Logistic Regression (baseline)
- Random Forest Classifier (placement prediction)
- Random Forest Regressor (performance score)
- KMeans (student clustering)

### Evaluation Metrics
- Accuracy Score
- Classification Report
- Confusion Matrix
- RMSE and R² Score

---

## 📦 Model Saving
All trained models were saved using **pickle** for reuse:
- `classifier.pkl` – placement prediction model
- `regressor.pkl` – performance score model
- `scaler.pkl` – feature scaling
- `kmeans.pkl` – clustering model

---

## 🚀 Model Loading and Usage
The saved models are loaded in the Flask application.

### Workflow
1. User enters details through the web form
2. Input data is preprocessed and scaled
3. Model predicts placement status
4. Result is displayed on the website

The application runs locally at:
http://127.0.0.1:5000/

---

## 🖥️ Technologies Used
- Python
- Pandas & NumPy
- Scikit-learn
- Matplotlib & Seaborn
- Flask
- HTML & CSS
- Pickle

---

## ✅ Conclusion
This project showcases a **complete real-world ML application**, from dataset analysis to deployment. It helped me gain practical experience in:
- Machine Learning algorithms
- Feature engineering
- Model deployment
- Web integration with Flask
