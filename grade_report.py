#Create a list of dictionaries for 5 students with name and marks for three subjects
students = [{'name': 'Mosa', "math": 23, 'physics': 45, 'setswana': 76},
           {'name': 'Sli', "math": 18, 'physics': 78, 'setswana': 37},
           {'name': 'Thando', "math": 87, 'physics': 45, 'setswana': 92},
           {'name': 'Lisa', "math": 36, 'physics': 98, 'setswana': 45},
           {'name': 'Sunflower', "math": 87, 'physics': 37, 'setswana': 76},
           {'name': 'Kat', "math": 15, 'physics': 76, 'setswana': 67}]

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

#Calculate: class average, highest mark, lowest mark
total = 0
for performance in results:
    total += performance['average']
class_average = total / len(students)

#Calculate: highest mark, lowest mark
highest = students[0]
lowest = students[0]

for learner in students:
    if learner['math'] > highest['math']:
        highest = learner

    if learner['math'] < lowest['math']:
        lowest = learner   

#Display a formatted class report showing individual results and class statistics
i = 0
while i <= 60:
    print("*", end='')
    i += 1

print(f"\n\t\t\tCLASS REPORT")

j = 0
while j <= 60:
    print("*", end='')
    j += 1
for student_report in students:
    for results_report in results:
        if student_report['name'] == results_report['name']:
            print(f"\n{student_report['name']}:")
            print(f"\tMATH:\t\t {student_report['math']}")
            print(f"\tPHYSICS:\t {student_report['physics']}")
            print(f"\tSETSWANA:\t {student_report['setswana']}")
            print(f"\tAVERAGE:\t {results_report['average']}")
            print(f"\tGRADE:\t\t {results_report['grade']}")
            print(f"\tSTATUS:\t\t {results_report['status']}")

x = 0
while x <= 60:
    print("*", end='')
    x += 1