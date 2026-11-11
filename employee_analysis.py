import pandas as pd

# Step 1: Read the employee data.
employees = pd.read_csv("employees.csv")

# Step 2: Show the average salary.
print("Average salary:", employees["salary"].mean())

# Step 3: Count employees in each department.
print("\nEmployees in each department:")
print(employees["department"].value_counts())

# Step 4: Find employees earning more than the amount entered.
amount = int(input("\nEnter a salary amount: "))
above_amount = employees[employees["salary"] > amount]
print("\nEmployees earning more than", amount, ":")
print(above_amount)

# Step 5: Save those employees in a new CSV file.
above_amount.to_csv("employees_above_threshold.csv", index=False)
print("\nResults saved in employees_above_threshold.csv")
