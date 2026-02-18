"""
Welcome to Rosy Dhakal's Student Grading System
Description: Automated evaluation mapping numerical scores to performance benchmarks.
"""

# Initial dataset containing student performance metrics
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99, 
    "Draco": 74,
    "Neville": 62,
}

# Initialize a data structure to store categorized performance evaluations
student_grades = {}

# Iterate through dataset to map numerical scores to performance benchmarks
for student in student_scores:
    score = student_scores[student]
    
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

# Output the processed evaluation results
print(student_grades)