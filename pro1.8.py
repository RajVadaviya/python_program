# 8. Write a Python program to perform following operation on given string input:
# a) Count Number of Vowel in given string
# b) Count Length of string (donot use len() )
# c) Reverse string
# d) Find and replace operation
# e) check whether string entered is a palindrome or not

def count_vowel(str):
    count = 0
    for s in str.lower():
        if s=="a" or s=="e" or s=="i" or s=="o" or s=="u":
            count += 1
    return count

def countlen(str):
    len = 0
    for i in str:
        len += 1
    return len

def reverseStr(str):
    return str[::-1]

def palindrome(str):
    return str==str[::-1]

def findandreplace(str,oldVal,newVal):
    return str.replace(oldVal,newVal)   

string = input("Enter string : ")

print("vowel is : ",count_vowel(string))
print("Length of string : ",countlen(string))
print("Reverse string : ",reverseStr(string))

print("Palindrome : ",palindrome(string))

oldVal = input("Enter oldValue : ")
newVal = input("Enter newValue : ")

print("Replace string : ",findandreplace(string,oldVal,newVal))