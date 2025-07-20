import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import streamlit as st

# Load data
credit_card_df = pd.read_csv('creditcard.csv')

# Balance data
legit = credit_card_df[credit_card_df.Class == 0]
fraud = credit_card_df[credit_card_df.Class == 1]
legit_sample = legit.sample(n=500, random_state=1)
credit_card_df = pd.concat([legit_sample, fraud], axis=0)

# Split data
X = credit_card_df.drop('Class', axis=1)
Y = credit_card_df['Class']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Scale features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Train model
model = LogisticRegression(class_weight='balanced', max_iter=1000)
model.fit(X_train_scaled, Y_train)

# Streamlit UI
st.title("💳 Credit Card Fraud Detection")

st.markdown("🔢 Enter **all feature values** separated by `;` (semicolon).")
input_df = st.text_input("Example input: `-1.3598;1.1919;...` (Total: 30 features)")

submit = st.button("Submit")

if submit:
    try:
        input_values = [float(i) for i in input_df.split(';')]

        if len(input_values) != X.shape[1]:
            st.error(f"❗ Please enter exactly {X.shape[1]} feature values.")
        else:
            # Reshape and scale input
            features_scaled = scaler.transform([input_values])
            prediction = model.predict(features_scaled)

            if prediction[0] == 0:
                st.success("✅ Legitimate Transaction")
            else:
                st.error("🚨 Fraudulent Transaction Detected!")

    except ValueError:
        st.error("⚠️ Invalid input. Make sure all values are numbers separated by `;`.")

