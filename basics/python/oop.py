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
    def __init__(self, salaryempl,manager):
        super().__init__(fname, secname, salary, exp, manager)
        self.salaryempl=salaryempl
        





developer = employee("Vasia", "Petrov", 300, 3, "manager")
designer = employee("Petia", "Ivanov", 350, 5, "manager")
manager = employee("Ivan", "Sidorov", 500, 6, "manager")
#department = employee()

def departsalary(emp):
    return (emp.fname+" "+emp.secname+' got salary:'+ str(emp.salary))



#"@firstName@ @secondName@: got salary: @salaryValue@")
print (departsalary(designer), departsalary (developer), departsalary (manager))
