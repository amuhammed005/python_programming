import datetime

# ---------------------------- GLOBAL COURSES ---------------------------- #
courses = {
    "DCIT 418": "Cybersecurity", 
    "DCIT 401": "Programming I", 
    "DCIT 427": "Computer Networks",
    "CBAS 210": "Academic Writing",
}

# ---------------------------- ADD STUDENT ---------------------------- #
def add_student(id):
    print("\n🟢 Add a student to the database")

    # Name Input
    while True:
        first_name = input("First Name: ").strip().capitalize()
        if first_name.isalpha():
            break
        print("⚠️ Use letters only.")

    while True:
        last_name = input("Last Name: ").strip().capitalize()
        if last_name.isalpha():
            break
        print("⚠️ Use letters only.")

    name = f"{first_name} {last_name}"

    # Course Input
    print("\n📚 Available Courses:")
    for code, title in courses.items():
        print(f"{code}: {title}")

    registered_courses = {}
    while True:
        print("\nEnter course codes (e.g., DCIT 418, DCIT 427):")
        selected = input("Courses: ").upper().split(",")

        for code in selected:
            course_code = code.strip()
            if course_code in courses:
                registered_courses[course_code] = courses[course_code]
            else:
                print(f"❌ Course {course_code} not found.")

        if registered_courses:
            break
        print("⚠️ Please enter at least one valid course.")

    # DOB Input
    while True:
        birth_input = input("DOB (DD-MM-YYYY): ").strip()
        try:
            birth_year = int(birth_input.split("-")[-1])
            age = datetime.datetime.today().year - birth_year
            if 0 < age <= 120:
                break
            print("⚠️ Age not realistic.")
        except:
            print("⚠️ Invalid date format.")

    return {
        "id": id,
        "name": name,
        "age": age,
        "registered_courses": registered_courses,
        "scores": {}
    }

# ---------------------------- SCORE STUDENT ---------------------------- #
def score_student(id, students):
    student = students.get(id)
    if not student:
        print("❌ Student not found.")
        return

    print(f"\n✍️ Scoring {student['name']} ({id})")
    for code, title in student['registered_courses'].items():
        while True:
            try:
                score = float(input(f"Enter score for {code} ({title}): "))
                if 0 <= score <= 100:
                    student['scores'][code] = score
                    break
                else:
                    print("⚠️ Score must be between 0 and 100.")
            except ValueError:
                print("⚠️ Invalid score.")

# ---------------------------- SHOW STUDENT INFO ---------------------------- #
def show_student_info(id, students):
    student = students.get(id)
    if not student:
        print("❌ Student not found.")
        return

    print(f"\n👁️ Student ID: {student['id']}")
    print(f"👤 Name: {student['name']}")
    print(f"🎂 Age: {student['age']}")
    print("📚 Courses:")
    for code, title in student['registered_courses'].items():
        print(f"   {code}: {title}")
    print("📝 Scores:")
    if student['scores']:
        for code, score in student['scores'].items():
            print(f"   {code}: {score}")
    else:
        print("   No scores yet.")

# ---------------------------- UPDATE STUDENT ---------------------------- #
def update_student_info(id, students):
    student = students.get(id)
    if not student:
        print("❌ Student not found.")
        return

    print(f"\n🛠️ Updating student {student['name']}")

    new_name = input("New name (leave blank to keep current): ").strip()
    if new_name:
        student["name"] = new_name

    print("Update DOB? (current age will be recalculated)")
    dob_input = input("New DOB (DD-MM-YYYY) or leave blank: ").strip()
    if dob_input:
        try:
            birth_year = int(dob_input.split("-")[-1])
            student["age"] = datetime.datetime.today().year - birth_year
        except:
            print("⚠️ Invalid DOB format. Age not updated.")

    print("✅ Student info updated.")

# ---------------------------- DELETE STUDENT ---------------------------- #
def delete_student(id, students):
    if id in students:
        confirm = input(f"Are you sure you want to delete student {id}? (y/n): ").strip().lower()
        if confirm == "y":
            del students[id]
            print(f"🗑️ Student {id} deleted.")
    else:
        print("❌ Student not found.")





# ---------------------------- COURSE MANAGEMENT ---------------------------- #
def manage_courses(courses, students):
    while True:
        print("\n📚 COURSE MANAGEMENT")
        print("1. Add a new course")
        print("2. Update a course title")
        print("3. Delete a course")
        print("4. Clear all courses")
        print("5. Remove a course from a specific student")
        print("6. Show all courses")
        print("7. Back to Main Menu")

        choice = input("Select an option (1–7): ").strip()

        if choice == "1":
            code = input("Enter new course code (e.g., DCIT 499): ").upper().strip()
            if code in courses:
                print("❌ Course already exists.")
                continue
            title = input("Enter course title: ").strip().title()
            courses[code] = title
            print(f"✅ Course {code} added.")

        elif choice == "2":
            code = input("Enter course code to update: ").upper().strip()
            if code not in courses:
                print("❌ Course not found.")
                continue
            new_title = input("Enter new course title: ").strip().title()
            courses[code] = new_title
            print(f"✅ Course {code} updated.")

        elif choice == "3":
            code = input("Enter course code to delete: ").upper().strip()
            if code in courses:
                del courses[code]
                print(f"🗑️ Course {code} deleted.")

                for student in students.values():
                    if code in student["registered_courses"]:
                        del student["registered_courses"][code]
                        if code in student["scores"]:
                            del student["scores"][code]
                print("✅ Removed from all student records.")
            else:
                print("❌ Course not found.")

        elif choice == "4":
            confirm = input("⚠️ Are you sure you want to clear ALL courses? (y/n): ").strip().lower()
            if confirm == "y":
                courses.clear()
                for student in students.values():
                    student["registered_courses"].clear()
                    student["scores"].clear()
                print("🧹 All courses cleared from system and all students.")
            else:
                print("Cancelled.")

        elif choice == "5":
            try:
                sid = int(input("Enter student ID: "))
                student = students.get(sid)
                if not student:
                    print("❌ Student not found.")
                    continue

                print("📚 Registered Courses:")
                for code in student["registered_courses"]:
                    print(f"{code}: {student['registered_courses'][code]}")

                course_code = input("Enter course code to remove: ").upper().strip()
                if course_code in student["registered_courses"]:
                    del student["registered_courses"][course_code]
                    student["scores"].pop(course_code, None)
                    print(f"✅ Course {course_code} removed from student.")
                else:
                    print("❌ Student is not registered for that course.")
            except ValueError:
                print("⚠️ Invalid student ID.")
        
        elif choice == "6":
            print("\n📚 Available Courses:")
            for code, title in courses.items():
                print(f"{code}: {title}")


        elif choice == "7":
            break

        else:
            print("❌ Invalid choice.")

# ---------------------------- MAIN PROGRAM ---------------------------- #
def main():
    students = {}
    student_id = 100001

    while True:
        print("\n📋 MENU")
        print("1. Add Student")
        print("2. Score Student")
        print("3. Show Student Info")
        print("4. Update Student Info")
        print("5. Delete Student")
        print("6. List All Students")
        print("7. Manage Courses")
        print("8. Exit")

        choice = input("Select an option (1–8): ").strip()

        if choice == "1":
            student = add_student(student_id)
            students[student_id] = student
            print(f"✅ Student {student_id} added successfully!")
            student_id += 1

        elif choice == "2":
            try:
                id = int(input("Enter student ID: "))
                score_student(id, students)
            except ValueError:
                print("⚠️ Invalid ID.")

        elif choice == "3":
            try:
                id = int(input("Enter student ID: "))
                show_student_info(id, students)
            except ValueError:
                print("⚠️ Invalid ID.")

        elif choice == "4":
            try:
                id = int(input("Enter student ID: "))
                update_student_info(id, students)
            except ValueError:
                print("⚠️ Invalid ID.")

        elif choice == "5":
            try:
                id = int(input("Enter student ID: "))
                delete_student(id, students)
            except ValueError:
                print("⚠️ Invalid ID.")

        elif choice == "6":
            print("\n📦 All Students:")
            for sid, student in students.items():
                print(f"ID: {sid}, Name: {student['name']}, Age: {student['age']}")

        elif choice == "7":
            manage_courses(courses, students)

        elif choice == "8":
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid option.")

if __name__ == "__main__":
    main()
