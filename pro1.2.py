#2. Write a program to input 2 numbers and one arithmetic operator. Perform operations as per arithmetic operator which is given as input
num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
op=input("Enter Operator(+,-,*,/):")

if op=="+":
    result=num1+num2
elif op=="-":
    result=num1-num2
elif op=="*":
    result=num1*num2
elif op=="/":
    
    if num2!=0:
        result=num1/num2
    else:
        result ="error ! division by zero"
else:
    result="invalid operator"

print("Result:",result)
      