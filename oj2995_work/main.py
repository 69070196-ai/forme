student_id = input().strip()

if len(student_id) == 8 and student_id.isdigit() and "1" in student_id[2] and "6" in student_id[3]:
    print("yes")
else:
    print("no")