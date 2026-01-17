# ❤️ Heart Disease Prediction using Machine Learning

This project predicts whether a person is likely to have heart disease based on clinical and medical parameters.  
It demonstrates a complete **machine learning classification pipeline**, from data preprocessing to model deployment.

---

## 📌 Problem Statement
Heart disease is one of the leading causes of death worldwide.  
Early prediction using medical data can help doctors take preventive actions and improve patient outcomes.

---

## 📊 Dataset
- Source: Kaggle (Heart Disease Dataset)
- Format: CSV / Excel
- Each row represents a patient’s medical record

### Key Features:
- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Serum Cholesterol
- Fasting Blood Sugar
- Resting ECG
- Maximum Heart Rate
- Exercise Induced Angina
- ST Depression
- Slope of ST Segment
- Number of Major Vessels
- Thalassemia

Target Variable:
- `target` → 1 (Heart Disease), 0 (No Heart Disease)

---

## ⚙️ Workflow & Steps

### Step 1: Data Loading & Cleaning
- Loaded dataset using Pandas
- Checked for missing values and data consistency

### Step 2: Exploratory Data Analysis (EDA)
- Analyzed feature distributions
- Studied relationships between medical features and heart disease

### Step 3: Data Preprocessing & Feature Selection
- Split features (X) and target (y)
- Train-test split (80% training, 20% testing)

### Step 4: Model Training
- Algorithm used: **Logistic Regression**
- Trained the model on medical features

### Step 5: Model Evaluation
- Accuracy Score
- Confusion Matrix
- Classification Report (Precision, Recall, F1-score)

### Step 6: Prediction System
- Built a user-input based prediction system
- Model predicts heart disease for new patient data

---

## 📈 Model Performance
- Accuracy: ~80%
- Logistic Regression performed well for binary classification

---

## 🚀 Deployment
- Deployed using **Streamlit**
- Users can input medical details and get real-time predictions

---

## 🛠️ Tools & Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

## 📂 Project Structure
heart-disease-prediction/
│
├── Heart_Disease_Prediction.ipynb
├── app.py
├── heart_model.pkl
├── heart.csv.xlsx
├── requirements.txt
└── README.md

---

## 🎯 Key Learnings
- End-to-end ML workflow
- Medical data preprocessing
- Binary classification using Logistic Regression
- Model evaluation techniques
- Deploying ML models using Streamlit

---

## 👩‍💻 Author
**Pranshi**
