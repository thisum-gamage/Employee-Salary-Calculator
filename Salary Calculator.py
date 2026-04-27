def calculate_total(**total_cal):
    total = total_cal["basic"] + total_cal["allowance"] + total_cal["bonus"]
    return total


def calculate_tax(**tax_cal):
    tax = calculate_total(**tax_cal) / 10
    net_amount = calculate_total(**tax_cal) - tax
    return net_amount, tax


def display(**details):
    print(f"\nHello {details['name']},")
    print("\n-----This is Your Salary Breakdown-----")
    print(f"\nBasic Salary\t= {details['basic']:.2f}")
    print(f"Allowance\t= {details['allowance']:.2f}")
    print(f"Bonus\t\t= {details['bonus']:.2f}")
    print(f"Total\t\t= {calculate_total(**details):.2f}")
    net_val, tax_val = calculate_tax(**details)
    print(f"Tax(10%)\t= {tax_val:.2f}")
    print(f"Net Amount\t= {net_val:.2f}")


print("--Welcome To Employee Salary Calculator--")
print("-----------------------------------------")

employee_name = input("Enter Your Name\t\t: ")

while True:

    try:
        basic_salary = float(input("Enter Your Basic Salary\t: Rs. "))
        allowance = float(input("Enter Your Allowance\t: Rs. "))
        bonus = float(input("Enter Your Bonus\t: Rs. "))
        break
    except ValueError:
        print("Value Error!!!")

print("----------------------------------------")

display(name=employee_name, basic=basic_salary, allowance=allowance, bonus=bonus)