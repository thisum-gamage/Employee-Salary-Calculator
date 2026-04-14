def calculate_total():
    total = basic_salary + allowance + bonus
    return total


def display():
    print("")


print("--Welcome To Employee Salary Calculator--")
print("-----------------------------------------")

employee_name = input("Enter Your Name : ")
basic_salary = float(input("Enter Your Basic Salary : Rs. "))
allowance = float(input("Enter Your Allowance : "))
bonus = float(input("Enter Your Bonus : "))

print("----------------------------------------")

print(f"\nHello {employee_name},")
print("-------This is Your Salary Breakdown------")
