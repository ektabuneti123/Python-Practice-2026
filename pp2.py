#Strings & Conditional statement
str1 = "This is a string"
str2 = 'Apna college'
str3 = """This is a string"""

string = "this is string. \nwe are creating int in python"
print(string)
str_1 = "This is string. \tWe are creating int in python."
print(str_1)

#Concatenation of string
str_1 ="apna"
str_2 ="College"
Final_string = str_1 + str_2
print(Final_string)

#Adding space in concating to string
st_r1 = "apna"
st_r2 = "College"
final_str = st_r1 + " " + st_r2
print(final_str)
print(len(final_str))

#len function finding the length of a string 
str01 = "apna college"
len1 = len(str01)
print(len1)

#Indexing
str = "apna College"
print(str[3])

#Slicing
print(str[5:12])
print(str[5: len(str)])
print(str[5:])
print(str[:4])

#Negative slicing
sr = "apple"
print(sr[-5:])

neg = str[-5:-2]
print(neg)
print(str[-3:-1])

#String Function
#Str.endswith()
st = "I am studing Python from apnacollege"
print(str.endswith("ege"))
print(str.endswith("app"))

#str.capitalize()
s_r = "i am studying from apnacollege"
s_r = s_r.capitalize()
print(s_r)

#str.replace("","")
st = "I want do studying from Python from ApnaCollege"
print(st.replace("o","n"))

#str.replace
string = "I want to do coding"
print(string.replace("coding", "javascript"))

#st.find()
st = "i am from studying python from college"
print(st.find("o"))
print(st.find("from"))

#str.count()
str = "I am from studying python from MVLU college"
print(str.count("from"))
print(str.count("o"))


#practcie Question
#WAP to input user's first name & print its length
name =input("Enter your First name: ")
print(name)
print("Length of your name is: ",len(name))

#WAP to find the occurence of '$' in a string

string = "Hii i am $ a $ symbol $99.99"
print(string.count("$"))

age =21

if(age>=18):
    print("can vote & apply for license")

age = 16
if(age>=18):
    print("can vote & apply for license")
#It will not show any output
age = 18
if(age>=18):
    print("can vote")
    print("can drive")

#we can directly write True also in if conditon 
age = 18
if(True):
    print("can vote")
    print("can drive")

#elif practice
#1
light = "Green"
if (light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("go")
elif(light == "Yellow"):
    print("look")

print("End of program")

#2 in this we can use both two if statement in one code but both will execute
num = 5

if(num >= 2):
    print("greater than 2")

if(num >= 3):
    print("Greater than 3")

#3 in this if elif will same code as above

num = 5

if(num >= 2):
    print("greater than 2")

elif(num >= 3):
    print("Greater than 3")#greater than 2 #this only execute because of elif condition

#else: statement practice
#1
light = "Pink"
if(light == "Red"):
    print("Stop")
elif(light == "Green"):
    print("Go")
elif(light == "yellow"):
    print("look")
else:
    print("Light is broken")#Light is broken
                                    #End of the program

print("End of the program")

#2
age = 14

if(age>=18):
    print("can vote")
else:
    print("CANNOT vote")

#Q1
marks = int(input("Enter your marks: "))

if (marks >= 90):
    grade = "A"
    
elif (marks >= 80 and marks <90):
    grade = "B"

elif (marks >= 70 and marks < 80):
    grade = "C"

else:
    grade = "D"

print("Grade of the student is", grade)

age = 34
if(age  >= 18):
    print("can drive")
else:
    print("Cannot drive")

age = 17

if(age  >= 18):
    if(age >= 80):
        print("Cannot drive")
    else:
        print("can drive")
else:
    print("Cannot drive")


#WAP to check if a number entered by the user is odd or even
num = 95

if (num % 2 == 0):
    print("the given number is even")
else:
    print("The given number is odd")

print("End of the program")

#WAP to find the greatest of 3 number entered by the user

n1 = int(input("Enter any first number: "))
n2 = int(input("Enter any second number: "))
n3 = int(input("Enter any third number: "))

if (n1 > n2 and n1 > n3):
    print("First number is the greatest number")
elif(n2 >= n3):
    print("Second number is the greatest number")
else:
    print("Third number is the greatest number")

#WAP to find the greatest of 4 number entered by the user

#WAP to check if a number is a multiple of 7 or not

num = int(input("Enter any number: "))

if(num % 7 == 0):
    print("The number is a multiple of 7")
else:
    print("The number is not a multiple of 7")

#WAP to find the greatest of 4 number entered by the user

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

if(a>b and a>c) and (a>d):
    print("First number is the largest number.")
elif(b>c and b>d):
    print("Second number is largest number.")
elif(c>b and c>a) and (c>d):
    print("Third number is largest number.")
else:
    print("Fourth number is the largest number.")





























    
    









