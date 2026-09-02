'''
Write a function:

analyze_students(students)
that produces a report containing:
Average marks for every student.
The student with the highest average.
The student with the lowest average.
A list of students who have an average ≥ 80.
The most common subject position where students scored their highest mark.
0 = Subject 1
1 = Subject 2
etc.
Handle students with the same name correctly.
For example, there are two "Aman" records. Don't accidentally overwrite one just because you're using a dictionary.
'''

students = [
    {"name": "Aman", "marks": [78, 85, 92, 67]},
    {"name": "Riya", "marks": [91, 88, 95, 90]},
    {"name": "Karan", "marks": [55, 62, 58, 70]},
    {"name": "Neha", "marks": [88, 76, 84, 91]},
    {"name": "Aman", "marks": [82, 79, 88, 85]},
]

def analyze_students(students):
    Highest_Avg = None
    Lowest_Avg = None
    Ha_Student = None
    La_Student = None

    # for studnet list above 85%
    S_list = []
    #for getting most highest score subject 
    h_score_subject = {}
    
    # calculating average
    print(f"---- Average Marks of Each Student ----")
    for i in students:
        avg_marks = sum(i['marks']) / len(i['marks'])
        stud_name = i['name']
        print(f"{stud_name}: {avg_marks}...!")

        if avg_marks >= 80:
            S_list.append(stud_name)
        
        if Highest_Avg is None or Highest_Avg < avg_marks:
            Highest_Avg = avg_marks
            Ha_Student = stud_name

        if Lowest_Avg is None or avg_marks < Lowest_Avg:
            Lowest_Avg = avg_marks
            La_Student = stud_name

        #most commona highest score subject 
        mark_list = i["marks"]
        h_subject = None
        h_score = None
        for k in range(len(mark_list)):
            if h_score is None or mark_list[k] > h_score:
                h_subject = k  # as subject name is not given considering index name as subject name 
                h_score = mark_list[k]

        if h_subject not in h_score_subject:
            h_score_subject[h_subject] = 1
        else:
            h_score_subject[h_subject] += 1 

    print()
    print(f"---- tooper and bootm stundent ----")
    print(f"Topper : {Ha_Student} with Average {Highest_Avg}")
    print(f"Bottom : {La_Student} with Average {Lowest_Avg}")
    print()

    print(f"---- Student with avg >= 80% ----")
    for j in range(len(S_list)):
        print(f"{j+1}-> {S_list[j]}")
    print()

    print(f"---- highest-scoring subject ----")
    most_highest_score_sub = None
    highest_score = None

    for sub, score in h_score_subject.items():
        if highest_score is None or score > highest_score:
            highest_score = score
            most_highest_score_sub = sub
    
    print(f"Most common highest-scoring subject: Subject {most_highest_score_sub + 1}")
    print()
    
analyze_students(students)


#bonus 
def top_students(student):
    for i in student:
        avg_marks = sum(i['marks']) / len(i['marks'])
        if avg_marks >= 80:
            yield f"Student with average more then or equal to 80% :\n{i['name']} --> {avg_marks}"

obj = top_students(students)
print(next(obj))
print()
print(next(obj))
print()













