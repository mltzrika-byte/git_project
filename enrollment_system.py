students = []

def add_student(name, id_number):
    students.append({"name": name, "id": id_number})
    print(f"Student {name} added successfully!")


add_student("Maltizo Rica Mae", "2025-001")
print("Total students:", len(students))