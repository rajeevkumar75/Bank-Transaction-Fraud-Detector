# 🏦 Bank Transaction Fraud Detector  

## 📌 Project Overview  
Banking institutions handle millions of transactions daily, making it challenging to detect fraudulent activities in real time. This project leverages **Machine Learning algorithms** to automatically identify suspicious transactions and protect both banks and customers from financial losses.  

---

## 🎯 Problem Statement  
Fraud detection using manual processes is:  
- Slow and error-prone  
- Unable to scale with millions of transactions  
- Vulnerable to evolving fraud techniques  

**Objective:** Build an **intelligent fraud detection system** that flags fraudulent transactions with high accuracy and low false alarms.  

---

## ❓ Research Question  
*How can Machine Learning be applied to identify fraudulent transactions with high accuracy while minimizing false positives?*  

---

## 📊 Dataset  
- **Source:** [Kaggle – Credit Card/Bank Fraud Dataset](https://www.kaggle.com/datasets)  
- **Features:**  
  - `TransactionID` – Unique ID of transaction  
  - `Amount` – Transaction amount  
  - `Type` – Transaction type (Online, ATM, POS, etc.)  
  - `Location` – Transaction location  
  - `IsFraud` – Target variable (0 = Genuine, 1 = Fraudulent)  

---

## 🔧 Methodology  
1. **Data Preprocessing**  
   - Handle missing values  
   - Normalize transaction amounts  
   - Encode categorical features (Transaction Type, Location)  

2. **Feature Engineering**  
   - Time-based features  
   - Balance differences  
   - Transaction patterns  

3. **Modeling**  
   - Logistic Regression (baseline)  
   - Random Forest (supervised classification)  
   - Isolation Forest (anomaly detection)  

4. **Evaluation Metrics**  
   - Accuracy  
   - Precision, Recall, F1-Score  
   - ROC-AUC Curve
## 🚀 Expected Output  
Example Input:  
Amount: 24000
Type: ATM
Location: Unknown
Output : Fraud
