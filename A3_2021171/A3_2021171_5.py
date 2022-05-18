class Student:
    def __init__(self, name, cgpa, branch):
        self.isPlaced = False
        self.name = name
        self.cgpa = cgpa
        self.branch = branch

    def isEligible(self, obj1):
        if self.cgpa >= obj1.rcgpa and (self.branch in obj1.rbranch) and not self.isPlaced:
            if not self.isPlaced:
                print(
                    f"Student {self.name} is eligible for Company {obj1.name}")
                self.apply(obj1)
            else:
                print(
                    f"Student {self.name} is not eligible for Company {obj1.name}")
        else:
            print(
                f"Student {self.name} is not eligible for Company {obj1.name}")

    def apply(self, obj1):
        obj1.appliedStudents[self.cgpa] = self.name

    def getsPlaced(self):
        self.isPlaced = True


class Company:
    def __init__(self, name, rcgpa, rbranch, positionOpen):
        self.appliedStudents = {}
        self.applicationOpen = True
        self.rcgpa = rcgpa
        self.rbranch = rbranch
        self.positionOpen = positionOpen
        self.name = name
        self.k = 0

    def hireStudents(self, alls):
        for i in sorted(self.appliedStudents, reverse=True):
            self.k += 1
            if self.k <= self.positionOpen:
                name_i = self.appliedStudents[i]
                print(name_i)
                for t in alls:
                    if t.name == name_i:
                        t.getsPlaced()
        self.closeApplication()

    def closeApplication(self):
        self.applicationOpen = False
        if self.k <= self.positionOpen:
            print(f"The company hired {self.k} students\n ")
        else:
            print(f"The company hired {self.k-1} students\n ")


n = int(input("Enter the number of students: "))
alls = []
for i in range(1, n+1):
    name = input(f"Enter name of Student {i}: ")
    cgpa = float(input(f"Enter cgpa of Student {i}: "))
    try:
        assert 0 < cgpa < 11, "The cgpa is invalid"
    except:
        print("The cgpa is invalid")
        continue
    branch = input(f"Enter branch of Student {i}: ")
    alls.append(Student(name, cgpa, branch))

m = int(input("Enter number of Companies: "))
# allc = []

for i in range(1, m+1):
    name = input(f"Enter name of Company {i}: ")
    rcgpa = float(input(f"Enter required cgpa of Company {i}: "))
    rbranch = input(f"Enter space separated branches of Company {i}: ").split()
    positionOpen = int(
        input(f"Enter number of postions Open of Company {i}: "))
    obj1 = Company(name, rcgpa, rbranch, positionOpen)
    for j in range(n):
        alls[j].isEligible(obj1)
    print(f"The company {name} has hired the following students:  ")
    obj1.hireStudents(alls)
