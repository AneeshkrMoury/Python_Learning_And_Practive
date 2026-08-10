# No classes, no inheritance, no external modules, no pandas.

students = {
    "Aman": [78, 85, 92],
    "Riya": [91, 88, 95],
    "Rahul": [65, 72, 70],
    "Neha": [88, 90, 84]
}


'''average_score(scores)
Takes a list of scores.
Returns the average.'''

def average_score(score):
    total_score = 0
    avg = 0
    for n in score:
        total_score = total_score + n
        avg = total_score / len(score)
        r_avg = round(avg, 2)

    return r_avg

'''student_report(name, scores)
Prints something like:
Aman -> Average: 85.0, Highest: 92, Lowest: 78'''

def student_report(name, scores):
    Highest = scores[0]
    Lowest = scores[0]
    for n in scores:
        if Highest < n:
            Highest = n

        if Lowest > n:
            Lowest = n

    print(f"{name} -> Average: {average_score(scores)}, Highest: {Highest}, Lowest: {Lowest}")


'''top_student(students)
Finds the student with the highest average.
Don't use sorted() or max(..., key=...).
Do it using the concepts you've learned'''

def top_student(students):
    t_student = None
    h_average = 0
    for name, marks in students.items():
        avg = average_score(marks)
        if h_average < avg:
            h_average = avg
            t_student = name

    print(f" student name : {t_student} toped with highest average : {h_average} ")

'''
passed_students(students)
Return a list containing students whose average is at least 75'''

def passed_students(students):
    passed = []

    for name, marks in students.items():
        avg = average_score(marks)
        if avg >= 75:
            passed.append(name)

    return passed


'''In the main part of your program:
Print every student's report.
Print the top student.
Print the list of passed students.'''

print(f"------- Score Card -------")
for names,scores in students.items():
    student_report(names, scores)

print()
print(f"------- Top Student -------")
top_student(students)
print()
print(f"------- Passed Student -------")
print(passed_students(students))

'''
🔥 Optional bonus
Add a function:
add_student(students, name, scores)
It should add a new student to the dictionary.
'''

def add_student(students, name, scores):
    students[name] = scores

add_student(students, "Vikash", [82, 76, 89])


print(f"------- Score Card -------")
for names,scores in students.items():
    student_report(names, scores)
