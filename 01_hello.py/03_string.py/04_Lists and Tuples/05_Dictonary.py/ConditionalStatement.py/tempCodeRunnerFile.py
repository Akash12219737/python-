marks = int(input("ENter your marks\n"))
if marks>=90:
    grade = "o"
elif marks>= 80:
    grade = "A"
elif marks>= 70:
    grade ="B"
elif marks>=60:
    grade = "c"
elif marks>= 50:
    grade = "D"
else:
    grade ="E"
    
print("Your grade is " + grade)