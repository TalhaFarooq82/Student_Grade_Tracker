students_grades = {}

while True:
    student_name = input("Enter the student's name (or 'exit' to finish): ")
    
    if student_name.lower() == 'exit':
        break
    
    if student_name not in students_grades:
        students_grades[student_name] = {}
    
    while True:
 
        subject = input(f"Enter subject for {student_name} (or 'exit' to stop adding subjects): ")
        if subject.lower() == 'exit':
            break

        grade = float(input(f"Enter grade for {subject}: "))
        
        
        students_grades[student_name][subject] = grade

students_averages = {}

for student, grades in students_grades.items():
    average = sum(grades.values()) / len(grades)
    students_averages[student] = average

    for student, grades in students_grades.items():
        print(f"\nGrades for {student}:")
        for subject, grade in grades.items():
            print(f"{subject}: {grade}")
        
        print(f"Average: {students_averages[student]:.2f}")
