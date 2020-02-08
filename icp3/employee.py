import self as self


class employee:
    count = 0
    salaries = []

    def __init__(self, name, familyname, salary, department):
        self.name = name
        self.familyname = familyname
        self.salary = salary
        self.department = department

        employee.salaries.append(self.salary)
        employee.count = employee.count + 1

    def averagesalary(self, salaries):
        totalsalary = 0
        salcount = len(salaries)
        for salary in salaries:
            totalsalary = totalsalary + salary
        avgsalary = totalsalary / salcount
        print("Average salary is", avgsalary)




class fulltimeEmployee(employee):

    def __init__(self, name, familyname, salary, department):
        employee.__init__(self, name, familyname, salary, department)



employee1 = employee("Sahithya", "Gadde", 100000, "CS")
employee2= fulltimeEmployee("Roshna","Toke", 239478,"CS")
employee3= employee("Bharani", "Yellanki", 105000,"CS")
employee4= fulltimeEmployee("Alekhya","Thangellapelly", 160341,"CS")
print("Total Number of employees ",employee.count)
print("Names of the employers are")
print(employee1.name)
print(employee2.name)
print(employee3.name)
print(employee4.name)
employee1.averagesalary(employee.salaries)

