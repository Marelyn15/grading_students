student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.

student_grades = dict()

# TODO-2: Write your code below to add the grades to student_grades.👇

#Saving names in an list
student_name = []
for index, element in enumerate(student_scores.keys()):
    student_name.append(element)


#Saving scores in a list
scoring_criteria = []
for index, element in enumerate(student_scores.values()):
    if element > 90:
        scoring_criteria.append('Outstanding')
    elif element > 80 and element < 91:
        scoring_criteria.append("Exceeds Expectations")
    elif element > 70 and element < 81:
        scoring_criteria.append("Acceptable")
    else:
        scoring_criteria.append("Fail")


#Joining both lists in a dict
student_grades = dict(zip(student_name, scoring_criteria))

# 🚨 Don't change the code below 👇
print(student_grades)