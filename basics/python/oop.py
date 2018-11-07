#https://www.journaldev.com/15911/python-super
class employee(object):
    def __init__(self, fname, secname, salary, exp, manager):
        self.fname=fname
        self.secname=secname
        self.salary=salary
        self.exp=exp
        self.manager=manager

class developer(employee):
    def __init__(self, fname, secname, salary, exp, manager):
    super().__init__(fname, secname, salary, exp, manager)

class designer(employee):
    def __init__(self, fname, secname, salary, exp, manager, effcoeff):
    super().__init__(fname, secname, salary, exp, manager)
    self.effcoeff=effcoeff

class manager(employee):
    def __init__(self, fname, secname, salary, exp, manager, team):
    super().__init__(fname, secname, salary, exp, manager)
    self.team=team
class department(employee):
    def __init__(self, salaryempl,managert):
    super().__init__(fname, secname, salary, exp, manager)
    self.salaryempl=salaryempl
    self.salaryempl=salaryempl



developer = employee("Vasia", "Petrov", 300, 3, "manager", 0)
designer = employee("Petia", "Ivanov", 350, 5, "manager", 1)
manager = employee("Ivan", "Sidorov", 500, 6, "manager", 0)
department = employee("", "", 0, 0, manager, 0)

#    def departsalary( fname, secname, salary):
#       "This prints a department how to give salary"
#       print ("Name: ", fname + " " + secname)
#       print ("Salary: ", salary)
#       return

# Now you can call printinfo function
#departsalary ( fname = (employee[0]), secname = (employee[1]), salary = (employee[2]) )


print (designer.fname)


