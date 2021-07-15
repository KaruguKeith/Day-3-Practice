#Program that asks for marks input and displays the grade

marks = int(input("What marks did the student get"))

if 100>marks>=90:
    print("Grade A")
if 90>marks>=80:
    print("Grade B")
if 80>marks>=70:
    print("Grade C")
if 70>marks>=60:
    print("Grade D")
if marks <60:
    print("Grade E")