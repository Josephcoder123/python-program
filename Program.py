num1_str = input("Enter the first number:")
operator = input("Enter the operator(+,-,*,/):")
num2_str = input("Enter the second number:")

try:
    num1=float(num1_str)
    num2=float(num2_str)

    if operator =="+":
        result= num1 + num2
    elif operator =="-":
        result= num1-num2
    elif operator =="*":
        result= num1*num2
    elif operator =="/":
        if num2 != 0:
            result =num1/num2
        else:
            result= "Error:Division by zero"
    else:
        result= "Error: Invalid operator"
    print(f"The result is:{result}")

except ValueError:
    print("Error:Invalid number input.Please enter numerical values.")
