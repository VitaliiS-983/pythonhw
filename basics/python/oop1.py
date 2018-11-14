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

class team(employee):
    def __init__(self, countmem, countdev):
       # super().__init__(fname, secname, salary, exp, manager)	
        self.countmem=countmem
        self.countdev=countdev
		
developer = developer("Vasia", "Petrov", 300, 3, manager)
designer = designer("Petia", "Ivanov", 350.0, 7, "manager", 0.7)
manager = manager("Ivan", "Sidorov", 500, 6, "manager", 1)
#department = department()
team = team( 2, 1)

def departsalary(self):
    return (self.fname+" "+self.secname+' got salary:'+ str(self.salary))

def designersalary(self):
     return (self.salary+(self.salary * self.effcoeff))
 
def expemloye(self):
    if self.exp > 2:
	    sum = (self.salary+200)
	    return (sum)
    elif self.exp > 5:
	    sum = ((self.salary*1.2)+500)
	    return (sum)
		
#def managerbonus(self):
    if self.countmem > 5:
	    managsal = (self.salary+200)
	    return (managsal)
    elif self.countmem > 10:
	    managsal = (self.salary+300)
	    return (managsal)
		
print ("Depart employee:")
print (departsalary(designer), departsalary (developer), departsalary (manager))

print ("Designer salary:")
print (designersalary(designer))

print ("Salary exp:")
print (expemloye(designer))

#print ("Salary manager bonus:")
#print (managerbonus(team))



