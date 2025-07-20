# 💳 Credit Card Fraud Detection

This project uses machine learning to detect fraudulent credit card transactions. It is built using **Logistic Regression** and features an interactive **Streamlit web app** for real-time predictions.

## 🚀 Features

- Trains on the **Kaggle Credit Card Fraud Detection** dataset
- Balances data for better fraud detection accuracy
- Uses **StandardScaler** for feature normalization
- Streamlit UI accepts input for prediction
- Displays whether a transaction is legitimate or fraudulent

## 📊 Dataset

The dataset used is from Kaggle:  
👉 [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

- **Total Records**: 284,807 transactions  
- **Features**: 30 anonymized features + `Class` label  
- `Class = 0`: Legitimate transaction  
- `Class = 1`: Fraudulent transaction  

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## 📦 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jobin-r/credit_fraud_detection.git
   cd credit_fraud_detection
2. # 💳 Credit Card Fraud Detection

This project uses machine learning to detect fraudulent credit card transactions. It is built using **Logistic Regression** and features an interactive **Streamlit web app** for real-time predictions.

## 🚀 Features

- Trains on the **Kaggle Credit Card Fraud Detection** dataset
- Balances data for better fraud detection accuracy
- Uses **StandardScaler** for feature normalization
- Streamlit UI accepts input for prediction
- Displays whether a transaction is legitimate or fraudulent

## 📊 Dataset

The dataset used is from Kaggle:  
👉 [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)

- **Total Records**: 284,807 transactions  
- **Features**: 30 anonymized features + `Class` label  
- `Class = 0`: Legitimate transaction  
- `Class = 1`: Fraudulent transaction  

## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit

## 📦 How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/jobin-r/credit_fraud_detection.git
   cd credit_fraud_detection
   pip install -r requirements.txt
   streamlit run fraud_dete.py
🧪 Example Input Format
When prompted in the Streamlit UI, enter 30 feature values separated by semicolons (;), like:
   -1.3598;1.1919;0.2661;-1.3405;0.1666;... (total 30 values)

🧠 Note
To handle the class imbalance, the model uses:

All fraud transactions
A random sample of 500 legitimate transactions

🤝 Contributions
Pull requests are welcome! Feel free to open issues or suggest improvements.






