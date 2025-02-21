import csv

grade_average = []
with open('grades.csv', 'r') as file:
    read = list(csv.DictReader(file))
    subjects = {x['Subject'] for x in read}
    subjects = list(subjects)
    for subject in subjects:
        grade_sum = 0
        count = 0
        for x in read:
            if x['Subject'] == subject:
                count += 1
                grade_sum += int(x['Grade'])
        grade_average.append({"Subject":subject, "Average grade" : grade_sum/count})

with open('average_grades.csv', 'w', newline='') as file:
    fieldnames = ['Subject', 'Average grade']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(grade_average)


