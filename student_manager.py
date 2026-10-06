
import re

FILE_NAME = "students.txt"


# Validate email using Regex
def validate_email(email):
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


# Add Student
def add_student():
    try:
        student_id = input("Enter Student ID: ").strip()
        name = input("Enter Student Name: ").strip()
        email = input("Enter Email: ").strip()

        if not student_id or not name or not email:
            raise ValueError("All fields are required!")

        if not validate_email(email):
            raise ValueError("Invalid email format!")

        # Save student data to file
        with open(FILE_NAME, "a") as file:
            file.write(f"{student_id},{name},{email}\n")

        print("Student added successfully!")

    except ValueError as e:
        print("Error:", e)

    except Exception as e:
        print("Something went wrong:", e)


# Read Student Data
def read_students():
    try:
        with open(FILE_NAME, "r") as file:
            students = file.readlines()

            if not students:
                print("No student records found.")
                return

            print("\n--- Student Records ---")

            for student in students:
                student = student.strip()

                if student:
                    data = student.split(",")

                    print("ID    :", data[0])
                    print("Name  :", data[1])
                    print("Email :", data[2])
                    print("----------------------")

    except FileNotFoundError:
        print("No student file found. Add a student first.")

    except Exception as e:
        print("Error reading file:", e)


# Main Menu
def main():
    while True:
        print("\n===== STUDENT RECORD MANAGER =====")
        print("1. Add Student")
        print("2. Read Student Data")
        print("3. Exit")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()

            elif choice == 2:
                read_students()

            elif choice == 3:
                print("Thank you!")
                break

            else:
                raise ValueError("Please enter 1, 2, or 3.")

        except ValueError as e:
            print("Invalid input:", e)


# Start program
if __name__ == "__main__":
    main()


