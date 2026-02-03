# # var, print
# a=b=c=10
# print(a,b,c)
# print()

# name = "Om More"
# age = 20
# CGPA = 9.78

# print("My name is", name, "and my age is", age)
# print("My CGPA is",CGPA)
# print()

# # Input, split
# # name, age, CGPA = input("Enter name, age and CGPA:").split(',')
# name, age, CGPA = input("Enter name, age and CGPA:").split()
# print("My name is", name, "and my age is", age)
# print("My CGPA is",CGPA)
# print(type(name), type(age), type(CGPA))
# print()

# name = input("Enter your name:")
# age = int(input("Enter your age:"))
# CGPA = float(input("Enter your CGPA:"))
# print("My name is", name, ", my age is", age, "and my CGPA is", CGPA)
# print(type(name), type(age), type(CGPA))

# name,age,CGPA = input("Name:"), int(input("Age:")), float(input("CGPA:"))
# print(name,age,CGPA)
# print(type(name),type(age),type(CGPA))

# x=10
# print(x)
# # del x
# print(x)

# a,b=5,10
# a,b=b,a
# print(a,b)

# print("I live in {}. I am studying in {}. My name is {}. My age is {}".format("Kalyan", "VESIT", "Om", 20))

name, age, cgpa = input("Enter Name:"), int(input("Enter age:")), float(input("Enter CGPA:"))

print("STUDENT PROFILE".center(30,'-'))
# print("Name: {}\nAge: {}\nCGPA: {}".format(name,age,cgpa))
print("Name".ljust(5),":",name)
print("Age".ljust(5),":",age)
print("CGPA".ljust(5),":",cgpa)

if(cgpa>=9):
    print("Satus: Excellent Performer")
else:
    print("Status: Keep Improving")

print("-"*30)