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
1 = Subject 2  # for this one we can use same loop then we use another loop to find which subject have highest marks then add it to a dic if in similary for other subject then compare and return the one comes hoghest times 
etc.
Handle students with the same name correctly.
For example, there are two "Aman" records. Don't accidentally overwrite one just because you're using a dictionary.
'''
student = [
    {"name": "Aman", "marks": [78, 85, 92, 67]},
    {"name": "Riya", "marks": [91, 88, 95, 90]},
    {"name": "Karan", "marks": [55, 62, 58, 70]},
    {"name": "Neha", "marks": [88, 76, 84, 91]},
    {"name": "Aman", "marks": [82, 79, 88, 85]},
]

def analyze_students(students):

    h_average = None
    l_average = None
    h_a_student = None
    l_a_student = None 

    avg_list = []
    c_subject = {}
    
    print(f"---- Average Marks of Each Student ----")
    for i in student: # this point to first student that is now dict {} 

        #our 1st taks is to find average of each student 
        # now i got it was not reuired another look here we can use i directly that was my mistake lets complee first part 
        avg = sum(i['marks']) / len(i['marks'])   
        s_name = i['name']
        print(f"{s_name}: {avg}") 

        #using same loop for 2nd and 3rd 
        if h_average is None or avg > h_average:
            h_average = avg
            h_a_student = s_name

        if l_average is None or avg < l_average:
            l_average = avg
            l_a_student = s_name

        # checking if avegrae is >= 80 if yes add to list
        if avg >= 80:
            avg_list.append(s_name)


        #find best subject for each student 
        sub_list = i["marks"]
        b_subject = sub_list[0]     
        b_marks = 0 # here we will be using positon as 0 is subject 1
        for i in range(len(sub_list)): # from this we got our best subject now lets add it to dic 
            if sub_list[i] > b_marks:
                b_subject = i
                b_marks = sub_list[i]


        if b_subject not in c_subject: # it check if subject not present add it and assign value 1 else increase value by 1 
            c_subject[b_subject] = 1
        else:
            c_subject[b_subject] += 1


    print()
    #2nd part
    #student with highest averga and 3rd lowest 
    print(f"---- Highest Avergae Achiver----")
    print(f"{h_a_student}: {h_average}")
    print()
    print(f"---- Lowest Avergae Achiver----")
    print(f"{l_a_student}: {l_average}")
    print()

    #4th part
    print(f"---- Student with >= 80 score ----")
    for i in avg_list:
        print(i)
    print()

    #5th common subject
    most_cb_subject = None
    for i in c_subject:
        
        if most_cb_subject is None or c_subject[i] > most_cb_subject:
            most_cb_subject = i
    print(f"--- most common subject position where students scored their highest mark ---")
    print(f"Subject -> {most_cb_subject + 1}")
    print()



analyze_students(student)












