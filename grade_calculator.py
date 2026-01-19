# Grade Calculator Program

marks = int(input("Enter your marks (0 to 100): "))

if marks < 0 or marks > 100:
    print("Invalid marks! Please enter marks between 0 and 100.")

elif marks >= 90 and marks <= 100:
    print("Grade: A")

elif marks >= 75 and marks < 90:
    print("Grade: B")

elif marks >= 60 and marks < 75:
    print("Grade: C")

elif marks >= 40 and marks < 60:
    print("Grade: D")

else:
    print("Grade: Fail")