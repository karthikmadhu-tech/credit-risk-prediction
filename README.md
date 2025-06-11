# Credit Risk Prediction using ML Models

This project aims to predict the probability of loan default using a real-world dataset from Home Credit. We trained models using Logistic Regression, Random Forest, and XGBoost to identify high-risk applicants.

🔍 Objective

Help financial institutions assess the creditworthiness of applicants by predicting their default probability based on financial and demographic features.

📊 Dataset
	•	Source: Home Credit Default Risk Dataset on Kaggle
	•	Features include age, income, employment history, credit amount, education type, and more.
	•	Target: 1 = Defaulted, 0 = Non-defaulted

🧠 Models Used
	•	Logistic Regression
	•	Random Forest (tuned)
	•	XGBoost (tuned)

🏆 Performance (AUC on Test Set)
	•	Logistic Regression: 0.6389
	•	Random Forest: 0.7366
	•	XGBoost: 0.7515

📁 Project Structure

notebook/credit_risk_prediction.ipynb → End-to-end data cleaning, EDA, modeling
app/streamlit_app.py → Streamlit interface
models/xgb_simple_model.pkl → Trained model
requirements.txt → List of Python packages

🚀 How to Run the Notebook
	1.	Clone this repo
	2.	Open credit_risk_prediction.ipynb in Colab or Jupyter
	3.	Run all cells

🌐 Run the Streamlit App Locally

Make sure you have streamlit installed:

pip install -r requirements.txt
streamlit run app/streamlit_app.py

📸 Screenshot of App
(Insert an image here if you want: you can upload an app screenshot in the repo)

🛠️ Tools & Libraries
	•	Python, Pandas, NumPy
	•	Scikit-learn, XGBoost
	•	Streamlit, Joblib
	•	Google Colab
