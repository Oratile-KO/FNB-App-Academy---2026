#Create a lisst of dictionaries for 5 students with name and marks for three subjects
students = [{'name': 'Mosa', "math": 23, 'physics': 45, 'setswana': 76},
           {'name': 'Sli', "math": 18, 'physics': 78, 'setswana': 37},
           {'name': 'Thando', "math": 87, 'physics': 45, 'setswana': 92},
           {'name': 'Lisa', "math": 36, 'physics': 98, 'setswana': 45},
           {'name': 'Sunflower', "math": 87, 'physics': 37, 'setswana': 76},
           {'name': 'Kat', "math": 45, 'physics': 76, 'setswana': 67}]

results =  []

#Use a for loop to iterate over all students and calculate each student’s average
for student in students:
    average = (student['math'] + student['physics'] + student['setswana']) / 3

    #Assign a letter grade: A (80+), B (70-79), C (60-69), D (50-59), F (below 50) using if/elif/else
    if average > 79:
        grade = 'A'
    elif average > 69:
        grade = 'B'
    elif average > 59:
        grade = 'C'
    elif average > 49:
        grade = 'D'
    else: 
        grade = 'F'

    #Assign Pass status if the average is 50 or above, Fail otherwise
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"
    #Build a results list of dictionaries containing: name, average, grade, status
    result = {'name': student['name'], 'average': average, 'grade': grade, 'status': status}
    results.append(result)
print(results)

#Calculate: class average, highest mark, lowest mark
# total = 0
# for performance in students:
#     total += (performance['math'] + performance['physics'] + performance['setswana'])
# class_average = total / (len(students) * 3)

# #Calculate: class highest mark
# for highest in students:
#     marks = [highest['math'],
#              highest['physics'],
#              highest['setswana']]
#     #print(marks)
#     print(max(marks['math']))
#     # print(f"The highest math mark is {max(highest['math'])}")
