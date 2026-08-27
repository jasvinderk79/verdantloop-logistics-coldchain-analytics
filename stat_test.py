import sqlite3
import pandas as pd
from scipy import stats

# 1. Load data from SQLite
conn = sqlite3.connect("verdantloop_ops.db")
df = pd.read_sql_query("SELECT max_temp_c, delay_minutes FROM shipment_analytics", conn)
conn.close()

# 2. Split data into two comparison groups
temp_spiked = df[df['max_temp_c'] > 6.0]['delay_minutes'].dropna()
temp_normal = df[df['max_temp_c'] <= 6.0]['delay_minutes'].dropna()

# 3. Perform Two-Sample Independent T-Test
t_stat, p_value = stats.ttest_ind(temp_spiked, temp_normal, equal_var=False)

print(f"Mean delay for Spiked Temp Group: {temp_spiked.mean():.2f} mins")
print(f"Mean delay for Normal Temp Group: {temp_normal.mean():.2f} mins")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_value:.6e}")

# 4. Draw Hypothesis Conclusion
alpha = 0.05
if p_value < alpha:
    print("\nCONCLUSION: Reject Null Hypothesis (H0).")
    print("Statistically significant proof that temperature spikes correlate with higher delivery delays.")
else:
    print("\nCONCLUSION: Fail to reject Null Hypothesis (H0).")