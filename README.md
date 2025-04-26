📊 Fraudulent Transaction Detection
Detect and predict fraudulent financial transactions based on customer behavior and transaction patterns.

📁 Dataset
Source: Custom uploaded dataset (Final Transactions.csv).

Main columns:

TX_AMOUNT – Amount of transaction.

TX_TIME_SECONDS – Transaction time during the day (in seconds).

TX_TIME_DAYS – Transaction day number.

TX_FRAUD – Target variable (1 = Fraudulent, 0 = Genuine).

TX_FRAUD_SCENARIO – Type of fraud scenario (only for fraud cases).

🚀 Project Pipeline
1. Data Loading
Load and inspect the dataset.

Handle missing values if any.

2. Exploratory Data Analysis (EDA)
Visualize distribution of fraudulent vs genuine transactions.

Analyze transaction amount and time patterns for frauds.

3. Data Preprocessing
Select important features: TX_AMOUNT, TX_TIME_SECONDS, TX_TIME_DAYS.

Scale features using StandardScaler.

Balance the dataset using SMOTE to handle class imbalance.

4. Model Building
Train machine learning models:

Logistic Regression

Random Forest

Isolation Forest (for anomaly detection)

Evaluate using:

Confusion Matrix

Classification Report

ROC AUC Score

5. Deployment (Optional)
Deploy a simple Streamlit web application where users can input transaction details and get fraud risk prediction.

🛠️ Technologies Used
Python

Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn

imbalanced-learn (for SMOTE)

Streamlit (for deployment)

🧠 Skills Demonstrated
Fraud detection modeling

Anomaly detection

Handling imbalanced datasets

Model evaluation with ROC-AUC

Building and deploying a Machine Learning application

📦 Installation & Setup
Install dependencies:

bash
Copy
Edit
pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn streamlit
Run training script to train and evaluate models.

Launch Streamlit app:

bash
Copy
Edit
streamlit run app.py
📈 Sample EDA Output
Fraud vs Non-Fraud Count

Transaction Amount Distribution

Fraud Trend Over Time

📑 License
This project is for educational purposes.

🎯 Final Goal
Build a reliable machine learning model to identify fraudulent transactions early and accurately, helping to prevent financial loss.
