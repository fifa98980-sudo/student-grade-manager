import json
import os

DATA_FILE = "grades.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_subject(data):
    name = input("Subject name: ").strip()
    if name in data:
        print("Subject already exists.")
        return

    grade = get_valid_grade()
    if grade is None:
        return

    data[name] = grade
    save_data(data)
    print("Subject added successfully.")


def edit_subject(data):
    name = input("Subject name to edit: ").strip()
    if name not in data:
        print("Subject not found.")
        return

    grade = get_valid_grade()
    if grade is None:
        return

    data[name] = grade
    save_data(data)
    print("Grade updated successfully.")


def delete_subject(data):
    name = input("Subject name to delete: ").strip()
    if name not in data:
        print("Subject not found.")
        return

    del data[name]
    save_data(data)
    print("Subject deleted successfully.")


def show_subjects(data):
    if not data:
        print("No subjects found.")
        return

    print("\nSubjects:")
    for name, grade in data.items():
        print(f"- {name}: {grade}")


def calculate_gpa(data):
    if not data:
        print("No data to calculate GPA.")
        return

    average = sum(data.values()) / len(data)
    print(f"\nGPA (average): {average:.2f}")


def get_valid_grade():
    try:
        grade = float(input("Grade (0 - 100): "))
        if not 0 <= grade <= 100:
            raise ValueError
        return grade
    except ValueError:
        print("Invalid grade.")
        return None


def main():
    data = load_data()

    while True:
        print("\n--- Student Grade Manager ---")
        print("1. Add subject")
        print("2. Edit subject")
        print("3. Delete subject")
        print("4. Show subjects")
        print("5. Calculate GPA")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_subject(data)
        elif choice == "2":
            edit_subject(data)
        elif choice == "3":
            delete_subject(data)
        elif choice == "4":
            show_subjects(data)
        elif choice == "5":
            calculate_gpa(data)
        elif choice == "6":
            print("Goodbye.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()

