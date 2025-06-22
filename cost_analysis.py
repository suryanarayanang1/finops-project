import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to SQLite
conn = sqlite3.connect("costs.db")

# Load data into a DataFrame
df = pd.read_sql_query("SELECT * FROM daily_costs", conn)

# Total cost
total_cost = df['cost'].sum()
print(f"💰 Total Cloud Cost (Simulated): ${total_cost:.2f}")

# Average cost per day
avg_cost = df.groupby('date')['cost'].sum().mean()
print(f"📊 Average Daily Cost: ${avg_cost:.2f}")

# Day with highest total cost
daily_totals = df.groupby('date')['cost'].sum()
max_day = daily_totals.idxmax()
print(f"🔥 Highest Cost Day: {max_day} - ${daily_totals[max_day]:.2f}")

# Cost per service
service_totals = df.groupby('service')['cost'].sum()
print("\n🔧 Cost per Service:")
print(service_totals)

# Optional: Plot daily spend
plt.figure(figsize=(10, 5))
daily_totals.plot(kind='bar', title='Daily Cloud Cost')
plt.ylabel("Cost ($)")
plt.xlabel("Date")
plt.tight_layout()
plt.show()
