#3. Write a program to enter marks of 4 subjects and display result (result shall include total, percentage and grade)

s1=int(input("Enter marks for CN:"))
s2=int(input("Enter marks for PYP:"))
s3=int(input("Enter marks for JAVA:"))
s4=int(input("Enter marks for ANDROID:"))

total=s1+s2+s3+s4
percentage=(total/400)*100
if percentage >=95:
   print("grade : A+")
elif percentage >=90:
    print("grade : B")
elif percentage >=75:
    print("grade : C")
elif percentage >=50:
   print("grade : D")
elif percentage >=35:
    print("grade : E")
else:
    print("grade:Fail")

print("\n----Student Result ----")
print("Total Marks:",total)
print("Percentage Marks:",percentage)