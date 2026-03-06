# 1.Write a program to display basic exception handling in python. 

print("Basic Exception Handling Program")
print("----------------------------------")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    result = num1 / num2
    
except ZeroDivisionError:
    print("Error: Division by zero is not allowed!")

except ValueError:
    print("Error: Please enter valid integer numbers!")

except Exception as e:
    print("Unexpected Error:", e)

else:
    print("Division Result =", result)

finally:
    print("Program executed successfully (Exception handling demo).")
