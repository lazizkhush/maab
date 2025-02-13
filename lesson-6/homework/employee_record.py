while True:
    print("""1. Add new employee record
    2. View all employee records
    3. Search for an employee by Employee ID
    4. Update an employee's information
    5. Delete an employee record
    6. Exit
    """)
    option = int(input('Enter your chocie [from 1 to 6] '))

    # def find_employees(emp_id):


    if option == 1:
        record = input('Enter employee record in the following format:\nEmployee ID, Name, Position, Salary')
        with open('employees.txt', 'a') as f:
            f.write(record+'\n')

    elif option == 2:
        with open('employees.txt') as f:
            read = f.read()
            print(read)

    elif option == 3:
        emp_id = input('Enter employee ID: ')
        with open('employees.txt') as f:
            lines = f.readlines()
            for l in lines:
                fields = l.split(',')
                if fields[0] == emp_id:
                    print(l)

    elif option == 4:
        emp_id = input('Enter employee ID: ')
        with open('employees.txt', 'r') as f:
            lines = f.readlines()
            new_lines = []
            for l in lines:
                fields = l.strip().split(',')
                if fields[0] != emp_id:
                    new_lines.append(l)
                else:
                    updated = input('Input new info')
                    new_lines.append(updated+'\n')
        
        with open('employees.txt', 'w') as f:
            f.writelines(new_lines)

    elif option == 5:
        emp_id = input('Enter employee ID: ')
        with open('employees.txt', 'r') as f:
            lines = f.readlines()
            new_lines = []
            for l in lines:
                fields = l.strip().split(',')
                if fields[0] != emp_id:
                    new_lines.append(l)

        with open('employees.txt', 'w') as f:
            f.writelines(new_lines)

    else:
        break