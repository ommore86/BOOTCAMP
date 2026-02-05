# # Task 1: Number Checker
# n = int(input("Enter a number:"))

# if n==0:
#     print("Zero")
# elif n>0:
#     print("Positive")
# else:
#     print("Negative")

# # Task 2: Even or Odd Checker
# n = int(input("Enter a number:"))

# if n%2==0:
#     print("Even")
# else:
#     print("Odd")

# # Task 3: Voting Eligibility
# age = int(input("Enter your age:"))

# if age>=18:
#     print("Eligible")
# else:
#     print("Not eligible")

# STUDENT GRADE EVALUATOR
name = input("Enter Student's name:")
marks = int(input("Enter marks:"))

if marks>=90:
    grade = "A"
    status = "Outstanding"
elif marks>=80:
    grade = "B"
    status = "Good"
elif marks>=60:
    grade = "C"
    status = "Fair"
elif marks>=40:
    grade = "D"
    status = "Can do Better"
else:
    grade = "Fail"
    status = "Fill re-exam form"

print("RESULT".center(25,"-"))
print("Student".ljust(8),":",name)
print("Marks".ljust(8),":",marks)
print("Grade".ljust(8),":",grade)
print("Status".ljust(8),":",status)
print("-"*25)