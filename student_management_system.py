import datetime
import time
import json

courses = {
    "DCIT 200": "Internship",
    "DCIT 201": "Programming I",
    "DCIT 216": "Computer Networks",
    "DCIT 207": "Data Structures",
    "DCIT 217": "Software Evolution",
}

# dcit 200, dcit 216, dcit 201, dcit 546

def add_student(id):
    print("📜 Register student")
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

    while True:
        birth_year = input("Enter DOB (DD-MM-YY): ").strip()
        try:  
            birth_year = int(birth_year.split("-")[-1])
            # print("⚠️ Enter a valid date e.g DD-MM-YY")
            age = int(datetime.datetime.today().year) - birth_year
            if 0 < age <= 130:
                break
            print("⚠️ Please enter a reasonable age")
        except ValueError:
            print("⚠️ Invalid date format. Enter DD-MM-YY")
    print(age)

    print("📚 Available Courses")
    for code, title in courses.items():
        print(f"{code}: {title}")
    
    course_list = []
    # print(course_list)
    while True:
        print("Add courses to {id} separated by comma (e.g. DCIT 111, DCIT 420)")
        course_input = input("Enter course/courses: ").strip().upper().split(",")
        # print('Course Input: ',course_input)

        invalid_courses = []
        for course in course_input:
            course = course.strip()
            # print('Course: ',course)
            if course in courses:
                course_list.append(course)
            else:
                invalid_courses.append(course)
        # print("Course list: ", course_list)

        if invalid_courses:
            print("❌These courses are not available")
            for c in invalid_courses:
                print(f"   - {c}")
        if course_list:
            print("✅ Valid courses added")
            for c in course_list:
                print(f"   - {c}")

        registered_courses = {}
        for course in course_list:
            registered_courses[course] = courses[course]
        # print(registered_courses)

        add_more_courses = input("Add more courses (y/n): ").strip().lower()
        if not add_more_courses == "y":
            break

    
    return {
        "id": id,
        "name": name,
        "age": age,
        "registered_courses": registered_courses,
        "scores": {}
    }


def update_student_info(id, students):
    student = students.get(id)
    if not student:
        print(f"❌ Student {id} not found")
        return
    
    print(f"🛠️ Update student {student['name']}")
    while True:
        new_first_name = input("First Name (Press enter to skip changes): ").strip().capitalize()
        if not len(new_first_name):
            new_first_name = student['name'].split(" ")[0]
            break
        if new_first_name.isalpha():
            break
        print("⚠️ Use letters only.")

    while True:
        new_last_name = input("Last Name (Press enter to skip changes): ").strip().capitalize()
        if not len(new_last_name):
            new_last_name = student['name'].split(" ")[-1]
            break
        if new_last_name.isalpha():
            break
        print("⚠️ Use letters only.")
    
    new_name = f"{new_first_name} {new_last_name}"
    if new_name:
        student['name'] = new_name


def score_student(id, students):
    student = students.get(id)
    if not student:
        print("❌ Student not found")
        return
    # print(student['registered_courses'])
    print(f"✍ Scoring {student['name']} ({id})")
    for code, title in student['registered_courses'].items():
        if code in student['scores']:
            print(f"✅ {code} already scored ({student['scores'][code]}). Skipping...")
            continue

        while True:
            score_input = input(f"Enter score for {code} ({title}) or q to Quit: ").strip()
            if score_input.lower() == "q":
                print("Skipping...")
                time.sleep(1)
                print(f"↪️ Skipped scoring for {code}")
                break
            try:
                score = float(score_input)
                if 0 <=  score <=100:
                    student['scores'][code] = score
                    print("Scoring...")
                    time.sleep(1)
                    print(f"✅ Score for {code} saved")
                    break
                else:
                    print("⚠️ Score must be between 0 and 100.")
            except ValueError:
                print("❌ Invalid score. Enter a number between 0–100 or 'q' to skip.")


def show_student_info(id, students):
    student = students.get(id)
    if not student:
        print("❌ Student not found")
        return
    
    print(f"\n*** Information about Student. ***")
    print(f"👁️ Student ID: {student['id']}")
    print(f"👤 Name: {student['name']}")
    print(f"🎂 Age: {student['age']}")
    # print(f" Registered Courses: {student['registered_courses']}")
    print(f"📚 Registered Courses:")
    for code, title in student['registered_courses'].items():
        print(f"     {code}: {title}")
    print(f"✅ Scores:")
    if student['scores']:
        for code, score in student['scores'].items():
            print(f"     {code}: {score}")
        print()
    else:
        print("     Student not yet scored")

    
def delete_student(id, students):
    student = students.get(id)
    if student:
        confirm = input(f"⚠️ Are you sure you want to delete student {id} ({student['name']})? (y/n): ").strip().lower()
        if confirm != "y":
            return
        print("Deleting...")
        del students[id]
        time.sleep(1)
        print(f"🚮 Student {id} deleted successfully")


def all_students(id, students):
    print(f"*** All students ***")

    if not students:
        print("No students found in DB. Proceed to add students!\n")
    else:
        for id, student in students.items():
            print(f"ID: {id}: Name: {student['name']} Age: {student['age']}")
    

def clear_students_data(students):
    students = students
    confirm = input("⚠️ Are you sure you want to clear all students? (y/n): ").strip().lower()
    if confirm != "y":
        return
    students.clear()
    time.sleep(1)
    print(f"🚮 Students data cleared successfully")    
    

def save_to_file(students):
    with open("students.json", "w") as f:
        json.dump(students, f, indent=4)
    print("💾 Data saved to students.json")

def load_from_file():
    try:
        with open("students", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}
def load_from_file():
    try:
        with open("students.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}


def main():
    print("*** Welcome to the student management system ***")

    students = load_from_file()
    student_id = max(map(int, []), default=1000) + 1
        
    while True:
        print("***** MENU *****")
        print("1: Add student")
        print("2: Score student")
        print("3: Show student info")
        print("4: Update student info")
        print("5: List all students")
        print("6: Delete a student")
        print("7: Delete all students")
        print("8: Save to file and Quit")

        choice = input("Select an option: ").strip()

        if choice == "1":
            student = add_student(student_id)
            students[student_id] = student
            print(f"✅ Student added successfully.")
            student_id += 1
        elif choice == "2":
            try:
                id = int(input("Enter student ID: ").strip())
                score_student(id, students)
            except ValueError:
                print("⚠️ Invalid input")
        elif choice == "3":
            try:
                id = int(input("Enter student ID: ").strip())
                show_student_info(id, students)
            except ValueError:
                print("⚠️ Invalid input")
        elif choice == "4":
            try:
                id = int(input("Enter student ID: ").strip())
                update_student_info(id, students)
            except ValueError:
                print("⚠️ Invalid input")
        elif choice == "5":
            all_students(student_id , students)
        elif choice == "6":
            try:
                id = int(input("Enter student ID: ").strip())
                delete_student(id, students)
            except ValueError:
                print("⚠️ Invalid input")
        elif choice == "7":
            clear_students_data(students)
        elif choice == "8":
            save_to_file(students)
            break


if __name__ == "__main__":
    main()