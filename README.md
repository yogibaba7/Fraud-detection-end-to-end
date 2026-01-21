## 📄 Project Documents

This repository contains detailed documentation and analysis reports for deeper understanding:

- 📘 **Project Documentation**  
  Detailed explanation of the end-to-end project workflow, data preprocessing, feature engineering, model building, threshold optimization, and system design.  
  👉 [Read Project Documentation](end_to_end_fraud_detection_Documentation.pdf)

- 📊 **Project Report**  
  Understanding fraud behaviour,solution and its impact.  
  👉 [Read Insight Report](Project_Report.pdf)



# 💳 End-to-End Financial Fraud Case Study & Solution

**Behavioral Analysis, Explainable ML & Business-Driven Decisioning**



## Project Overview

This project focuses on **detecting and understanding financial fraud in banking transaction systems** using large-scale transaction data.
Rather than treating fraud detection as only a modeling problem, this project emphasizes:

* **Fraud behavior understanding**
* **Money flow analysis**
* **Explainable machine learning**
* **Business-realistic decision strategies**

The final solution balances **fraud loss, customer impact, and operational cost**, making it suitable for real-world deployment.

---

## 🎯 Objective

* Analyze how fraud actually happens in transaction data
* Identify behavioral patterns that separate fraud from genuine activity
* Build a high-precision fraud detection model
* Understand **why** the model flags transactions using explainability
* Design a **business-ready ALLOW / REVIEW / BLOCK system**

---

## 📊 Dataset Description

* ~6.3 million transactions (~500 MB raw size)
* Time span: **30 days** (1 step = 1 hour, total 744 steps)
* 11 transaction-level features

### Key Columns

* `step` – time index (hour-level)
* `type` – transaction type (CASH_IN, CASH_OUT, TRANSFER, etc.)
* `amount` – transaction amount
* `oldbalanceOrg`, `newbalanceOrg` – sender balances
* `oldbalanceDest`, `newbalanceDest` – receiver balances
* `isFraud` – fraud label
* `isFlaggedFraud` – rule-based business flag

Fraud scenario: attackers take control of accounts, transfer funds, then cash out.

---

## 🛠️ Project Workflow

1. Large-scale data preprocessing
2. Exploratory Data Analysis (EDA)
3. Feature engineering driven by fraud behavior
4. Model building & imbalance handling
5. Threshold optimization (business-oriented)
6. Model explainability using SHAP
7. Model weakness analysis
8. Improvement trials & trade-off analysis
9. Final production-ready system design

---

## ⚙️ Data Preprocessing

* Optimized data types to reduce memory usage
* Removed merchant transactions (0% fraud → noise reduction)
* Reduced dataset size from **534 MB → 264 MB**
* Removed high-cardinality ID columns (`nameOrig`, `nameDest`)

---

## 🔍 Exploratory Data Analysis (EDA)

Due to scale, EDA was performed using:

* **All fraud cases**
* **25% sampled non-fraud cases**

### Key Insights

* Fraud peaks during **late-night hours**
* Fraud mainly occurs in **TRANSFER & CASH_OUT**
* Strong fraud signal in **sender & receiver balance changes**

---

## 🧠 Feature Engineering

### Balance Change Features

To remove multicollinearity:

```text
diffOrg  = newbalanceOrg  − oldbalanceOrg
diffDest = newbalanceDest − oldbalanceDest
```

These directly capture **money movement**, which is central to fraud behavior.

### Time Features

* Converted step → hour of day
* Categorized into: Morning, Afternoon, Night, Late Night

---

## 🤖 Model Building

### Models Tested

* Logistic Regression
* KNN
* Decision Tree
* Random Forest
* Extra Trees
* Gradient Boosting
* AdaBoost
* Bagging
* SVM
* Naive Bayes
* XGBoost
* LightGBM

⚠️ Accuracy was misleading due to heavy class imbalance.

---

## 🎯 Threshold Optimization

Instead of default 0.5:

* Precision–Recall curve used
* Threshold selected by **maximum F1-score**
* Focused on **business-relevant metrics**

---

## 🏆 Final Model Selection

**LightGBM** chosen over XGBoost because:

* Faster training
* Lower memory usage
* Better scalability
* Comparable performance

### Final Test Performance

* Precision: **95%**
* Recall: **77%**
* F1-Score: **85%**

Validation results confirmed **model stability (no overfitting)**.

---

## 🔍 Model Explainability (SHAP)

Fraud detection cannot be a black box.

SHAP was used for:

* **Global explanations** (overall model behavior)
* **Local explanations** (transaction-level reasoning)

### Key Findings

* **Sender balance reduction** is the primary decision driver
* **Receiver balance increase** confirms fraud accumulation
* **Amount & transaction type** only adjust confidence
* Fraud detection is driven by **money flow behavior**, not metadata

---

## ⚠️ Model Weakness Analysis

### When Fraud Is Detected

* Large sender balance drop
* Clear receiver balance increase
* Medium–high transaction amount

### When Fraud Is Missed

* Small or moderate amounts
* Mild sender balance reduction
* Weak receiver balance increase

> **The model catches loud fraud well, but struggles with quiet (stealth) fraud.**

---

## 🔧 Improvement Experiments

### 1. Rule-Based + Model System

Dynamic thresholds for weak-signal regions

### 2. Recall Booster Model

Secondary model trained on missed fraud cases

❌ Both approaches increased false positives heavily
➡️ Limitation identified in **data overlap**, not model design

---

## ✅ Final Business Solution

Instead of forcing risky predictions, a **review-based system** was designed:

```text
Transaction → Model → ALLOW / REVIEW / BLOCK
```

* High confidence fraud → BLOCK
* High confidence non-fraud → ALLOW
* Uncertain cases → MANUAL REVIEW

This handles fraud that ML alone cannot safely classify.

---

## 📈 Final System Comparison

### Single LightGBM Model

* Precision: **97.4%**
* Recall: **93.7%**
* Review rate: **~2.4%**

### Combined Model (Main + Booster)

* Recall: **98.5%**
* Precision: **~89.7%**
* Review rate: **~8.5%**

---

## 🏁 Final Decision

From a **loss–cost optimization perspective**:

* Single LightGBM offers the best balance
* Fewer false blocks
* Manageable review workload
* Strong fraud detection

✅ **Selected as final production system**

---

## 🧰 Tools & Technologies

* Python (Pandas, NumPy)
* Data Analysis
* Data Vizualization
* Machine Learning
* Scikit-learn
* LightGBM, XGBoost
* SHAP
* Optuna
* Matplotlib / Seaborn

---


