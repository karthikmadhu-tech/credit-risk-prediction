<p align="center">
<img width="381" alt="image" src="https://github.com/user-attachments/assets/16af1630-5f30-4f5c-996d-b861d84154bf" />
</p>

# Credit Risk Prediction using Machine Learning


## 🚀 Project Overview

Financial institutions rely on robust credit scoring to minimize loan defaults and optimize lending decisions. In this project, we predict the probability of loan default using real-world data from the Home Credit Default Risk competition on Kaggle. By combining data cleaning, feature engineering, and advanced ML algorithms, we deliver an interactive dashboard that empowers non-technical stakeholders to assess borrower risk in real time.

---

## 🎯 Business Context

Lenders must decide quickly whether to approve, decline, or adjust loan terms for applicants. A reliable credit risk model can:

- Reduce non-performing loan ratios  
- Lower capital reserves required by regulators  
- Enable customized interest rates for different risk profiles  

---

## 📊 Dataset

- **Source:** [Home Credit Default Risk Dataset on Kaggle](https://www.kaggle.com/competitions/home-credit-default-risk)  
- **Samples:** ~307,511 applications with 121 features  
- **Key Features:**  
  - Demographics (age, gender, family status)  
  - Financial (employment length, income, credit amount)  
  - Credit history (previous loans, payment records)  
- **Target:** `TARGET` — 1 = Defaulted, 0 = Paid

---

## 🧰 Tools & Libraries

- **Languages & Data:** Python 3.8+, pandas, NumPy  
- **ML & XAI:** scikit-learn, XGBoost, SHAP  
- **Visualization:** Matplotlib, Seaborn, Streamlit  
- **Deployment:** Streamlit Sharing / Heroku  
- **Environment:** Google Colab, Conda / venv  

---

## 📂 Repository Structure

credit-risk-prediction/
├── assets/
│   └── credit-risk-banner.png       # Project banner & screenshots
├── data/                            # (Optional) raw & processed data
├── notebook/
│   └── Credit\_risk\_prediction.ipynb # Analysis notebook for Google Colab
├── app/
│   └── streamlit\_app.py             # Interactive Streamlit dashboard
├── models/
│   └── xgb\_model.pkl                # Trained XGBoost model (if <100MB)
├── requirements.txt                 # pip install -r requirements.txt
└── README.md                        # This documentation

---

## ⚙️ Installation & Setup

1. **Clone the repo**  
   
   git clone https:[//github.com/your-username/credit-risk-prediction.git](https://github.com/karthikmadhu-tech/credit-risk-prediction.git)
   cd credit-risk-prediction

2. **Create & activate environment**

   python3 -m venv venv
   source venv/bin/activate      # macOS/Linux
   venv\Scripts\activate.bat     # Windows
   

3. **Install dependencies**

   pip install -r requirements.txt
   ```


## 📒 How to Run

### 1. Google Colab Notebook

* Open in Colab
* The notebook **Credit\_risk\_prediction.ipynb** includes sections for data exploration, feature engineering, model training, evaluation, **and an embedded Streamlit app demo**.

**To run the Streamlit demo within Colab:**

# Install dependencies
!pip install -r requirements.txt
!pip install pyngrok
from pyngrok import ngrok

# Launch Streamlit app in the background
!streamlit run app/streamlit_app.py &>/dev/null&

# Create a public URL for the app
public_url = ngrok.connect(8501)
print('Streamlit app URL:', public_url)


### 2. Local Streamlit Dashboard

* Clone the repo locally if you haven’t already:

  git clone https://github.com/your-username/credit-risk-prediction.git
  cd credit-risk-prediction
  
* Create & activate a virtual environment, then install dependencies:

  python3 -m venv venv
  source venv/bin/activate      # macOS/Linux
  venv\Scripts\activate.bat     # Windows
  pip install -r requirements.txt

* Run the app:

  streamlit run app/streamlit_app.py

* Open your browser at `http://localhost:8501` or the public URL from Colab.

---

## 📈 Sample Results


* **XGBoost** achieved **ROC AUC: 0.75** (Test)
* Feature importance highlights **EXT\_SOURCE\_2**, **DAYS\_BIRTH**, and **AMT\_INCOME\_TOTAL** as top predictors

---

## 🔍 Results & Discussion

* **Model Comparison:**

  | Model               | ROC AUC |
  | ------------------- | ------- |
  | Logistic Regression | 0.64    |
  | Random Forest       | 0.74    |
  | XGBoost             | 0.75    |

* **Key Insights:**

  * Applicants with *longer credit histories* and *higher incomes* show lower default risk.
  * Unexpected finding: a **single parent** status correlated with slightly higher risk, suggesting socio-demographic factors play a role.

* **Web App Demo:**
	* Launch locally via Streamlit: streamlit run app/streamlit_app.py opens at http://localhost:8501.
 	* Or run in Colab with ngrok and use the provided public URL.

<img width="1432" alt="image" src="https://github.com/user-attachments/assets/a956888f-e4bd-44a1-abe9-2dfadc6068ec" />



