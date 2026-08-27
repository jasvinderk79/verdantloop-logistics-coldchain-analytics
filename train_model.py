import sqlite3
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, roc_auc_score
from xgboost import XGBClassifier

# 1. LOAD DATA FROM SQL DATABASE
conn = sqlite3.connect("verdantloop_ops.db")
df = pd.read_sql_query("SELECT * FROM shipment_analytics", conn)
conn.close()

# 2. FEATURE SELECTION & PREPARATION
feature_cols = ['transit_hours', 'max_temp_c', 'delay_minutes']

for col in feature_cols:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
    else:
        df[col] = 0

X = df[feature_cols]
y = df['high_spoilage_risk']

# 3. SMART SPLIT (Handles small test samples safely)
if len(df) < 10 or y.nunique() < 2:
    print(f"Dataset has {len(df)} rows. Training on full dataset without train/test split...")
    X_train, X_test, y_train, y_test = X, X, y, y
else:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

# 4. INITIALIZE AND TRAIN XGBOOST MODEL
print("Training XGBoost Classifier...")
model = XGBClassifier(
    n_estimators=50,
    learning_rate=0.05,
    max_depth=3,
    random_state=42
)
model.fit(X_train, y_train)

# 5. MODEL EVALUATION
y_pred = model.predict(X_test)

print("\n================ MODEL PERFORMANCE ================")
print(classification_report(y_test, y_pred, zero_division=0))
if len(np.unique(y_test)) > 1:
    y_proba = model.predict_proba(X_test)[:, 1]
    print(f"ROC-AUC Score: {roc_auc_score(y_test, y_proba):.4f}")
print("===================================================")

# 6. SAVE PREDICTIONS BACK TO SQL FOR TABLEAU
df['predicted_spoilage_risk'] = model.predict(X)
conn = sqlite3.connect("verdantloop_ops.db")
df.to_sql("shipment_predictions", conn, if_exists="replace", index=False)
conn.close()

print("\nSuccess! Predictions exported to 'shipment_predictions' table inside 'verdantloop_ops.db'.")