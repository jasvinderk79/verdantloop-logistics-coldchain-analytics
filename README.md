# Cold-Chain Logistics Analytics & Spoilage Risk Prediction

End-to-end analytics project that turns raw cold-chain telemetry and unstructured driver logs into a predictive spoilage-risk system, with a Tableau dashboard for stakeholder reporting.

## Problem
Cold-chain logistics operations generate telemetry data and unstructured driver logs, but failures were typically only caught after spoilage had already occurred. This project builds an early-warning system instead.

## What this project does
- Processes raw cold-chain telemetry data using **Pandas**
- Integrates the **Google Gemini API** to extract structured failure categories from unstructured driver logs stored in **SQLite**
- Trains an **XGBoost Classifier** to predict high spoilage-risk shipments, optimized for ROC-AUC
- Exports the transformed, model-scored data to **Tableau** for stakeholder-facing reporting

## Tools & Stack
Python · Pandas · SQLite · Google Gemini API · XGBoost · Tableau

## Dashboard
🔗 [View the live Tableau dashboard](https://public.tableau.com/app/profile/jasvinder.kaur8501/vizzes) *(link to the specific viz once published)*

## Outcome
A predictive system that flags high-risk shipments before spoilage occurs, replacing after-the-fact reporting with early, actionable warnings.

## Author
Jasvinder Kaur — [LinkedIn](https://www.linkedin.com/in/jasvinder-kaur-406b13285/) · [Kaggle](https://www.kaggle.com/jasvinderkaur13)
