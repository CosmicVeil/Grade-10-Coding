# Name: Mohan Dixit
# Purpose: Practice Data Output

hours_per_month = float(input("Enter how many hours you work per month: "))
hourly_wage = float(input("Enter your hourly wage: "))

yearly_salary = 12*hours_per_month*hourly_wage

print("Your salary is: $", format(yearly_salary,'.2f'))

salary_with_bonus = yearly_salary*1.05

print("Your salary with a 5% bonus is: $", format(salary_with_bonus,'.2f'))

