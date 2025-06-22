import sqlite3
import random
from datetime import datetime, timedelta

# Connect to SQLite database (will be created if not exists)
conn = sqlite3.connect("costs.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS daily_costs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    service TEXT,
    region TEXT,
    cost REAL
)
""")

# Fake data options
services = ["Compute Engine", "Cloud Storage", "Load Balancer", "Cloud SQL", "Cloud Functions"]
regions = ["us-west1", "us-east1", "asia-south1", "europe-west1"]

# Generate 30 days of data
start_date = datetime.now() - timedelta(days=30)

for i in range(30):
    date = (start_date + timedelta(days=i)).strftime("%Y-%m-%d")
    for _ in range(random.randint(2, 4)):  # 2 to 4 entries per day
        service = random.choice(services)
        region = random.choice(regions)
        cost = round(random.uniform(0.01, 0.50), 2)
        cursor.execute("INSERT INTO daily_costs (date, service, region, cost) VALUES (?, ?, ?, ?)",
                       (date, service, region, cost))

conn.commit()
conn.close()

print("✅ Fake cost data inserted into 'costs.db'")
