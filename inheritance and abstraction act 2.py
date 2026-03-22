class person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def printname(self):
        print("fullname:  "+self.fname+" "+self.lname)
class student(person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.year=year

    def display(self):
        self.printname()
        print("graduation year:  "+self.year)

stu=student("hardik","kalita","2026")

stu.display()
    
