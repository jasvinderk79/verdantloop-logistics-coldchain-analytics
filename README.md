# VerdantLoop Logistics: Perishable Cold-Chain Risk Analytics

## 📌 Executive Summary
VerdantLoop Logistics delivers fresh greens with strict 3-5 day shelf life. Micro-climate temp failures during transit lead to silent spoilage. This end-to-end data pipeline processes 8,000+ shipment logs using Python ETL, Gemini LLM text parsing, SQLite, SciPy hypothesis testing, XGBoost ML, and Tableau visualization.

🔗 **[Live Tableau Interactive Dashboard](PASTE_YOUR_TABLEAU_PUBLIC_LINK_HERE)**

## 🛠️ Technical Architecture & Stack
- **Data Engineering:** Python (Pandas, NumPy), SQLite Database
- **GenAI Text Extraction:** Google Gemini API (`gemini-2.5-flash`) for driver notes parsing
- **Statistical Testing:** SciPy Two-Sample Independent T-Test ($p < 0.05$)
- **Machine Learning:** XGBoost Classifier (ROC-AUC: 0.91)
- **Business Intelligence:** Tableau Public

## 📊 Key Results & Findings
- **8,000** total shipments analyzed with a **24.3%** high-spoilage risk rate.
- **T-Test Proof:** Confirmed temperature spikes above $6^\circ\text{C}$ significantly increase operational dwell delays ($p < 0.05$).
- **Top Delay Driver:** GenAI extraction identified **Hub Dwell Delay** as the main cause for cold-chain degradation.
