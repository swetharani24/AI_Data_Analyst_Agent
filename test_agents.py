
import pandas as pd

from agents.manager_agent import manager_agent


# Sample dataset
data = {
    "Customer Name": ["A", "B", "C", "D", "D"],
    "Age": [25, 30, None, 40, 40],
    "Monthly Charges": [500, 600, 700, 800, 800],
    "City": [
        "Hyderabad",
        "Mumbai",
        None,
        "Delhi",
        "Delhi"
    ]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

# Run multi-agent workflow
result = manager_agent(df, "Analyze my dataset and find important insights")
result = manager_agent(df, "Clean my dataset and analyze the results")
result = manager_agent(df, "Identify trends and correlations in my data")

print("\nFinal Status:")
print(result["status"])

print("\nFinal Dataset:")
print(result["data"])

print("\nAgent Reports:")

for item in result["report"]:
    print("-", item)
