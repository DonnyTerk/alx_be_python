#Ask the user for their monthly income and expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses

#Annual projection with 0.05% interest
projected_annual_savings = (monthly_savings * 12) + (monthly_savings * 12 * 0.05)

#Display results
print("\n--- savings summary ---")
print(f"Your monthly savings are: ${monthly_savings:.2f}")
print(f"Your projected savings after one year (with 5% interest) are: ${projected_annual_savings:.2f}")
