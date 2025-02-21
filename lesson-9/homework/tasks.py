import json
import csv

def total_tasks(tasks):
    return len(tasks)

def completed_tasks(tasks):
    comleted = 0
    for task in tasks:
        if task['completed']:
            comleted += 1

    return comleted

def pending_tasks(tasks):
    pending = 0
    for task in tasks:
        if not task['completed']:
            pending += 1

    return pending

def avg_priority(tasks):
    priority_sum = 0
    for task in tasks:
        priority_sum += task['priority']

    return priority_sum/len(tasks)

def convert_to_csv(tasks):
    with open('tasks.csv', 'w', newline='') as file:
        fieldnames = ['id', 'task', 'completed', 'priority']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(tasks)
        

with open('tasks.json', 'r') as file:
    tasks = json.load(file)
    print("Total tasks:", total_tasks(tasks))
    print("Completed tasks:", completed_tasks(tasks))
    print("Pending tasks:", pending_tasks(tasks))
    print("Average Priority level:", avg_priority(tasks))
    convert_to_csv(tasks)


