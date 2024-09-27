total = 0
num_labs = int(input("how many labs did you do?"))
lab_weight = 0.2
if num_labs > 6:
   num_labs = 6
total = total + (num_labs/6  * lab_weight) * 100

num_quizzes = int(input("how many quizzes did you do?"))
quiz_weight = 0.15
if num_quizzes > 6: 
   num_quizzes = 6
total = total + (num_quizzes/6 * quiz_weight) * 100 

assignment_1 = int(input("what did you get on assignment 1?"))
assignment_1_weight = 0.04
total = total + (assignment_1 * assignment_1_weight)

assignment_2 = int(input("what did you get on assignment 2?"))
assignment_2_weight = 0.04
total = total + (assignment_2 * assignment_2_weight)

assignment_3 = int(input("what did you get on assignment 3?"))
assignment_3_weight = 0.04
total = total + (assignment_3 * assignment_3_weight)

assignment_4 = int(input("what did you get on assignment 4?"))
assignment_4_weight = 0.04
total = total + (assignment_4 * assignment_4_weight)

midterm_1 = int(input("what did you get on midterm 1?"))
midterm_1_weight = 0.125
total = total + (midterm_1 * midterm_1_weight)

midterm_2 = int(input("what did you get on midterm 2?"))
midterm_2_weight = 0.125
total = total + (midterm_2 * midterm_2_weight)

final_exam = int(input("what did you get on the final exam?"))
final_exam_weight = 0.18
total = total + (final_exam * final_exam_weight)

final_preperations = int(input("what did you get on the midterm and final preperations?"))
final_preperations_weight = 0.06
total = total + (final_preperations * final_preperations_weight)

print(f"Your grade is: {total}") 




