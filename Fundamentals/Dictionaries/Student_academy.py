from statistics import mean # sredno

n = int(input())

grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = [grade]
    else:
        grades[name].append(grade)

filtered_grades = {}
for student_name, marks in grades.items():
    avg_grade = mean(marks)
    if avg_grade >= 4.5:
        filtered_grades[student_name] = avg_grade

sorted_best_students = sorted(filtered_grades.items(), key=lambda kvp: -kvp[1])

# понеже е лист от тюпъли не ползваме .items()
for student_name, marks in sorted_best_students:
    print(f"{student_name} -> {marks: .2f}")