import json
import os

# Data store karne ke liye JSON file ka naam
FILE_NAME = "students.json"

# Agar file exist nahi karti to nayi khali list ke sath banayein
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, 'w') as file:
        json.dump([], file)

# File se data read karne ke liye function
def load_data():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading data: {e}")
        return []

# File mein data save karne ke liye function
def save_data(data):
    try:
        with open(FILE_NAME, 'w') as file:
            json.dump(data, file, indent=4)
    except Exception as e:
        print(f"Error saving data: {e}")

# 1. CREATE Operation
def create_student():
    roll_no = input("Enter Roll No: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    
    data = load_data()
    # Check if student already exists
    if any(student['roll_no'] == roll_no for student in data):
        print("Student with this Roll No already exists!")
        return

    data.append({"roll_no": roll_no, "name": name, "course": course})
    save_data(data)
    print("Student added successfully!")

# 2. READ Operation
def read_students():
    data = load_data()
    if not data:
        print("No student records found.")
        return
    
    print("\n--- Student Records ---")
    for student in data:
        print(f"Roll No: {student['roll_no']}, Name: {student['name']}, Course: {student['course']}")

# 3. UPDATE Operation
def update_student():
    roll_no = input("Enter Roll No of student to update: ")
    data = load_data()
    
    for student in data:
        if student['roll_no'] == roll_no:
            print(f"Current Name: {student['name']}, Current Course: {student['course']}")
            student['name'] = input("Enter new Name (or press Enter to skip): ") or student['name']
            student['course'] = input("Enter new Course (or press Enter to skip): ") or student['course']
            save_data(data)
            print("Student record updated successfully!")
            return
            
    print("Student not found!")

# 4. DELETE Operation
def delete_student():
    roll_no = input("Enter Roll No of student to delete: ")
    data = load_data()
    
    new_data = [student for student in data if student['roll_no'] != roll_no]
    
    if len(data) == len(new_data):
        print("Student not found!")
    else:
        save_data(new_data)
        print("Student deleted successfully!")

# Main Menu function
def main():
    while True:
        print("\n--- Student Record Management System ---")
        print("1. Add Student (Create)")
        print("2. View Students (Read)")
        print("3. Update Student (Update)")
        print("4. Delete Student (Delete)")
        print("5. Exit")
        
        try:
            choice = input("Enter your choice (1-5): ")
            
            if choice == '1':
                create_student()
            elif choice == '2':
                read_students()
            elif choice == '3':
                update_student()
            elif choice == '4':
                delete_student()
            elif choice == '5':
                print("Exiting program...")
                break
            else:
                print("Invalid choice! Please select between 1-5.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
