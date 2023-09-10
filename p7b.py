class Employee:
    def __init__(self,name,id,dept,salary):
        self.name=name
        self.id=id
        self.dept=dept
        self.salary=salary
    def updatesal(self,dept,insa):
        if self.dept==dept:
            self.salary *=(1 + insa / 100)

employees=[]
nofe=int(input("enter emp"))
for i in range(nofe):
    print( i+1,"th employee detail")
    name=input()
    id=int(input())
    dept=input()
    salary=int(input())
    employees.append(Employee(name,id,dept,salary))
print("emp name\t emp id\t emp dept \t emp sal\n")
for emp in employees:
    print(emp.name,"\t",emp.id,"\t",emp.dept,"\t",emp.salary,"\n")


depttt=input("enter the dept to increase sal")


for emp in employees:
    if emp.dept==depttt:
        emp.updatesal(dept,10)
for emp in employees:
    print(emp.name,emp.salary)
