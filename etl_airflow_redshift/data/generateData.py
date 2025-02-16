import pandas as pd
import random
from datetime import datetime, timedelta

# Define sample data
customer_names = ["Alice", "Bob", "Charlie", "David", "Eva", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
product_categories = ["Electronics", "Clothing", "Home Appliances", "Books", "Grocery"]
payment_modes = ["Credit Card", "UPI", "Debit Card", "Cash", "Net Banking"]

# Generate sample records
num_records = 1000
data = []

for i in range(1, num_records + 1):
    customer_name = random.choice(customer_names)
    amount = round(random.uniform(50, 500), 2)
    transaction_date = datetime(2024, 2, 1) + timedelta(days=random.randint(0, 20), hours=random.randint(0, 23), minutes=random.randint(0, 59))
    category = random.choice(product_categories)
    payment_mode = random.choice(payment_modes)

    data.append([i, customer_name, amount, transaction_date.strftime("%Y-%m-%d %H:%M:%S"), category, payment_mode])

# Create DataFrame
df = pd.DataFrame(data, columns=["id", "customer_name", "amount", "transaction_date", "product_category", "payment_mode"])

# Save to CSV
df.to_csv("sales_data.csv", index=False)

print("Sample sales_data.csv file generated successfully!")
