# List to store student records
students = []

def find_student(student_name):
    """
    Finds a student by name.

    :param student_name: The name of the student to be found.
    :return: Student record if found, None otherwise.
    """
    if not student_name.strip():
        return None
    for student in students:
        if student["name"].lower() == student_name.lower():
            return student
    return None

def add_student():
    """
    Adds a new student to the list if they don't already exist.
    """
    student_name = input("Enter student name: ")
    if not student_name.strip():
        print("Name cannot be empty.")
        return
    if find_student(student_name) is None:
        students.append({"name": student_name, "grades": []})
    else:
        print("Student already exists.")

def check_grade(grade):
    """
    Validates the grade input.

    :param grade: The grade input as a string.
    :return: Validated grade as an integer, or None if invalid.
    """
    try:
        grade = int(grade)
        if not 0 <= grade <= 100:
            raise ValueError("Grade must be between 0 and 100.")
        return grade
    except ValueError:
        print("Error: enter a valid grade.")
        return None

def input_grades():
    """
    Allows inputting grades for a specific student.
    """
    student_name = input("Enter student name: ")
    student = find_student(student_name)
    if student:
        while True:
            grade = input("Enter a grade (or 'done' to finish): ")
            if grade.lower() == "done":
                break
            checked_grade = check_grade(grade)
            if checked_grade is not None:
                student["grades"].append(checked_grade)
    else:
        print("Student doesn't exist.")

def get_average_grade(grades):
    """
    Calculates the average grade from a list of grades.

    :param grades: List of grades.
    :return: Average grade as a float, or None if no grades.
    """
    try:
        return round(sum(grades) / len(grades), 2)
    except ZeroDivisionError:
        return 'N/A'

def get_list_of_averages():
    """
    Generates a list of average grades for all students.

    :return: List of average grades for students with grades.
    """
    return [get_average_grade(student["grades"]) for student in students if student["grades"]]

def get_max_average_grade():
    """
    Gets the maximum average grade from all students.

    :return: Maximum average grade as a float, or None if no students.
    """
    averages = get_list_of_averages()
    return max(averages) if averages else None

def get_min_average_grade():
    """
    Gets the minimum average grade from all students.

    :return: Minimum average grade as a float, or None if no students.
    """
    averages = get_list_of_averages()
    return min(averages) if averages else None

def get_overall_average_grade():
    """
    Calculates the overall average grade from all students.

    :return: Overall average grade as a float, or None if no students.
    """
    averages = get_list_of_averages()
    return round(sum(averages) / len(averages), 2) if averages else None

def generate_report():
    """
    Generates a report of all students and their average grades.
    """
    if not students:
        print("There are no students.")
    else:
        print("\n--- Student Report ---:")
        for student in students:
            average = get_average_grade(student["grades"])
            print(student["name"] + "'s average grade is " + str(average))
        print("_________________________")

        max_avg = get_max_average_grade()
        min_avg = get_min_average_grade()
        overall_avg = get_overall_average_grade()

        print("Max Average: " + (str(max_avg) if max_avg is not None else "No grades"))
        print("Min Average: " + (str(min_avg) if min_avg is not None else "No grades"))
        print("Overall Average: " + (str(overall_avg) if overall_avg is not None else "No grades"))

def find_top_performer():
    """
    Finds and displays the student(s) with the highest average grade.
    """
    if not students:
        print("There are no students.")
        return
    students_with_grades = [student for student in students if student["grades"]]
    if not students_with_grades:
        print("There are no students with grades.")
        return
    top_performer = max(students_with_grades, key=lambda student: get_average_grade(student["grades"]))
    print(f"The student with the highest average grade is {top_performer['name']} with a grade of {get_average_grade(top_performer['grades'])}.")

def main():
    """
    Main function to run the student grade analyzer program.
    """
    while True:
        print("\n--- Student Grade Analyzer ---:"
              "\n1. Add a new student"
              "\n2. Add a grades for a student"
              "\n3. Generate a full report"
              "\n4. Find the top student"
              "\n5. Exit program")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                add_student()
            elif choice == 2:
                input_grades()
            elif choice == 3:
                generate_report()
            elif choice == 4:
                find_top_performer()
            elif choice == 5:
                print("Exiting program.")
                break
            else:
                print("Wrong choice. Enter the number from 1 to 5.")
        except ValueError:
            print("Error: enter the number.")

if __name__ == "__main__":
    main()