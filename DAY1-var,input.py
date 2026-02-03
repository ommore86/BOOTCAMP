# var, print
a=b=c=10
print(a,b,c)
print()

name = "Om More"
age = 20
CGPA = 9.78

print("My name is", name, "and my age is", age)
print("My CGPA is",CGPA)
print()

# Input, split
# name, age, CGPA = input("Enter name, age and CGPA:").split(',')
name, age, CGPA = input("Enter name, age and CGPA:").split()
print("My name is", name, "and my age is", age)
print("My CGPA is",CGPA)
print(type(name), type(age), type(CGPA))
print()

name = input("Enter your name:")
age = int(input("Enter your age:"))
CGPA = float(input("Enter your CGPA:"))
print("My name is", name, ", my age is", age, "and my CGPA is", CGPA)
print(type(name), type(age), type(CGPA))

name,age,CGPA = input("Name:"), int(input("Age:")), float(input("CGPA:"))
print(name,age,CGPA)
print(type(name),type(age),type(CGPA))

x=10
print(x)
# del x
print(x)

a,b=5,10
a,b=b,a
print(a,b)

print("I live in {}. I am studying in {}. My name is {}. My age is {}".format("Kalyan", "VESIT", "Om", 20))
