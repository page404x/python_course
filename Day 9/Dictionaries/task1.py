student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades ={}

for name in student_scores:
    if student_scores[name] > 90:
        student_grades[name] = "Outstanding"
    elif student_scores[name] > 80 and student_scores[name] <= 90:
        student_grades[name] = "Exceeds Expectation"
    elif student_scores[name] > 70 and student_scores[name] <= 80:
        student_grades[name] = "Acceptable"
    else:
        student_grades[name] = "Fail"

print(student_grades)