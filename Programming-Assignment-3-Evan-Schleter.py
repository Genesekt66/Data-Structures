def calculate_gross(hours, rate):
    return hours * rate
def calculate_deductions(gross_salary):
    return gross_salary * 0.20
def calculate_net_salary(gross_salary, deductions):
    return gross_salary - deductions

name = input("What is the employee's name?")
hours = float(input(f"How many hours did {name} work?"))
rate = float(input(f"What is {name}'s hourly rate?"))

print(f"\n{name}'s Salary information:")
print(f"Gross Salary: ${round(calculate_gross(hours,rate),2)}")
print(f"Deductions: ${round(calculate_deductions(calculate_gross(hours,rate)),2)}")
print(f"Net Salary: ${round(calculate_net_salary(calculate_gross(hours, rate),calculate_deductions(calculate_gross(hours, rate))),2)}")