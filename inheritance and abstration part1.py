class person:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber


    def display(self):
        print("name:  "+self.name)
        print("idnumber:  "+self.idnumber)
class employee(person):
    def __init__(self,name,idnumber,salary,post):
        super().__init__(name,idnumber)
        self.salary=salary
        self.post=post
emp=employee("hardik","32332","54000","manager")
emp.display()

print("salary:  "+emp.salary)
print("post:   "+emp.post)
