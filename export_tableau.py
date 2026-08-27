import sqlite3, pandas as pd
conn = sqlite3.connect("verdantloop_ops.db")
pd.read_sql_query("SELECT * FROM shipment_predictions", conn).to_csv("tableau_export.csv", index=False)