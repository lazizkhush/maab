class Employee:
    def __init__(self, employee_id, name, position, salary):
        self.employee_id = employee_id
        self.name = name
        self.position = position
        self.salary = salary            

    def get_info(self):
        return f'{self.employee_id}, {self.name}, {self.position}, {self.salary}'
    


class EmployeeManager:

    def __init__(self):
        self.employee_ids = []
        print("""Welcome to the Employee Records Manager!
1. Add new employee record
2. View all employee records
3. Search for an employee by Employee ID
4. Update an employee's information
5. Delete an employee record
6. Exit""")

    def add_employee(self):
        eid = int(input('Enter employee id: '))
        if eid in self.employee_ids:
            print("Employee with this id already exists")
        else:
            self.employee_ids.append(eid)
            name = input('Enter name: ')
            position = input('Enter position: ')
            salary = int(input('Enter salary: '))
            new = Employee(eid, name, position, salary)
            with open('employee.txt', 'a') as f:
                f.write(new.get_info()+'\n')
                print('Employee added successfully')

    def view_employees(self):
        do_sort = input("Would you like to sort employees.('y' for yes, 'n' for no): ")
        if do_sort.lower() == 'y':
            sortby = int(input('By what you would like to sort employees: (1 - id, 2 - name, 3 - salary)'))
            with open('employee.txt', 'r') as f:
                lines = f.readlines()
                if sortby == 1:
                    lines.sort(key=lambda line: int(line.split(',')[0].strip()))
                elif sortby == 2:
                    lines.sort(key=lambda line: line.split(',')[1])
                elif sortby == 3:
                    lines.sort(key=lambda line: int(line.split(',')[-1]))
                print('Employee records: ')
                for line in lines:
                    print(line, end='')
        else:
            with open('employee.txt', 'r') as f:
                lines = f.readlines()
                for line in lines:
                    print(line, end='')          

    def search_employee(self):
        employee_id = int(input("Enter employee id to search: "))
        with open('employee.txt', 'r') as f:
            lines = f.readlines()
            for line in lines:
                fields = line.split(',')
                print(fields)
                if int(fields[0]) == employee_id:
                    print('Employee found:')
                    print(line, end="")


    def update_employee(self):
        employee_id = input('Enter the id of the employeee you want to update: ')
        with open('employee.txt', 'r') as f:
            lines = f.readlines()
            new_lines = []
            for l in lines:
                fields = l.strip().split(',')
                if fields[0] != employee_id:
                    new_lines.append(l)
                else:
                    eid = int(input('Enter employee id: '))
                    name = input('Enter name: ')
                    position = input('Enter position: ')
                    salary = int(input('Enter salary: '))
                    updated = Employee(eid, name, position, salary)
                    new_lines.append(updated.get_info())
                        
        with open('employee.txt', 'w') as f:
            f.writelines(new_lines)

    def delete_employee(self):
        employee_id = input('Enter the id of the employee you want to delete: ')
        with open('employee.txt', 'r') as f:
            lines = f.readlines()
            new_lines = []
            for l in lines:
                fields = l.strip().split(',')
                if fields[0] != employee_id:
                    new_lines.append(l)
                else:
                    self.employee_ids.remove(employee_id)

        with open('employee.txt', 'w') as f:
            f.writelines(new_lines)



manager = EmployeeManager()
while True:
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print("Invalid input!!!")

    if choice == 1:
        manager.add_employee()
    elif choice == 2:
        manager.view_employees()
    elif choice == 3:
        manager.search_employee()
    elif choice == 4:
        manager.update_employee()
    elif choice == 5:
        manager.delete_employee()
    elif choice == 6:
        print("Good bye!")
        break


        