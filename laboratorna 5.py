students = {
    "andrii": {"institution_id": 1}, "artem": {"institution_id": 2}, "anastasia": {"institution_id": 3},
    "alina": {"institution_id": 4}, "anna": {"institution_id": 5}, "alex": {"institution_id": 6}
}

institutions = {
    1: {"name": "Школа №1", "kind": "school"}, 2: {"name": "Коледж №1", "kind": "college"},
    3: {"name": "Технікум №1", "kind": "texnikum"}, 4: {"name": "Школа №2", "kind": "school"},
    5: {"name": "Технікум №2", "kind": "texnikum"}, 6: {"name": "Коледж №2", "kind": "college"}
}

institution_types = {"school", "college", "texnikum"}

def add_student(student_id, institution_id):
    if institution_id not in institutions:
        print("Неіснуючий заклад.")
        return
    students[student_id] = {
        "institution_id": institution_id
    }
    educational_name = institutions[institution_id]["name"]
    educational_kind = institutions[institution_id]["kind"]
    print(f"{student_id} додано до {educational_name} ({educational_kind})")

def sum_school_students():
    count = 0
    for student in students.values():
        educational_id = student["institution_id"]
        if educational_id in institutions and institutions[educational_id]["kind"] == "school":
            count += 1
    print(f"\nКількість учнів у школах: {count}")

choice = input("Введіть 1, щоб додати учнів, або 0, щоб вивести уже записані дані: ")

if choice == "1":
    print("\nВведіть дані учнів. Щоб завершити, напишіть стоп, коли вписуватимете ім'я учня, якого додаватимете.")
    while True:
        student_id = input("\nВведіть ім’я учня: ")
        if student_id == "стоп":
            break
        try:
            institution_id = int(input("Введіть ID закладу (номер від 1 до 6): "))
            add_student(student_id, institution_id)
        except ValueError:
            print("Неіснуючий заклад.")

print("\nНавчальні заклади:")
for educational_id, info in institutions.items():
    print(f"- {info['name']} ({info['kind']})")

print("\nУчні навчальних закладів:")
for name, data in students.items():
    educational_id = data["institution_id"]
    educational_name = institutions[educational_id]["name"]
    print(f"- {name} навчається у {educational_name}")

sum_school_students()


