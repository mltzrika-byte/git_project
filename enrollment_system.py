students = []

def add_student(name, id_number):
    students.append({"name": name, "id": id_number})
    print(f"Student {name} added successfully!")


add_student("Maltizo Rica Mae", "2025-001")
print("Total students:", len(students))

def list_students():
    print("\n--- Enrolled Students ---")
    for student in students:
        print(f"- {student['name']} (ID: {student['id']})")
    print("---------------------------\n")

    list_students()