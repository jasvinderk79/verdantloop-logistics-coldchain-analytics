import sqlite3
import pandas as pd

# Connect to SQLite database generated in Step 3
conn = sqlite3.connect("verdantloop_ops.db")

print("--- QUERY 1: Spoilage Risk Rate by Transit Duration ---")
query_1 = """
SELECT 
    CASE 
        WHEN transit_hours > 8 THEN 'Long Transit (>8 hrs)'
        ELSE 'Normal Transit (<=8 hrs)'
    END AS transit_category,
    COUNT(*) AS total_shipments,
    SUM(high_spoilage_risk) AS high_risk_shipments,
    ROUND(AVG(high_spoilage_risk) * 100, 2) AS risk_percentage
FROM shipment_analytics
GROUP BY transit_category;
"""
df_q1 = pd.read_sql_query(query_1, conn)
print(df_q1.to_string(index=False))

print("\n--- QUERY 2: Parsed GenAI Failure Categories ---")
query_2 = """
SELECT 
    failure_category,
    COUNT(*) AS total_incidents,
    ROUND(AVG(delay_minutes), 1) AS avg_delay_mins
FROM shipment_analytics
WHERE failure_category IS NOT NULL
GROUP BY failure_category
ORDER BY total_incidents DESC;
"""
df_q2 = pd.read_sql_query(query_2, conn)
print(df_q2.to_string(index=False))

conn.close()