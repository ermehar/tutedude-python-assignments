marks = {"Alice":80, "John" :90, "Tom":85, "Bunny":95, "Robin":75, "Jack":80}
stud_name = input("Enter student's name: ")
if stud_name in marks:
    print(f"{stud_name}'s marks:", marks[stud_name])
else:
    print("Student not found")