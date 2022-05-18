class Person:
    def __init__(self, firstname, lastname, age):
        self.fn = firstname
        self.ln = lastname
        self.age = age

    def object_info(self, q):
        if q == "firstname":
            return self.fn
        if q == "lastname":
            return self.ln
        if q == "age":
            return int(self.age)

    def info(self):
        return [self.fn, self.ln, self.age]


def sort_attribute(out):
    for j in sorted(out):
        print(*out[j])


wish = "Y"
while wish == "Y":
    print("Welcome to the Application!\n")

    n = input("Enter number of persons and queries: ").split()
    all = []
    for i in range(1, int(n[0])+1):
        l = input(f"Enter space separated details of person {i}: ").split()
        obj = Person(l[0], l[1], l[2])
        all.append(obj)
    for i in range(int(n[1])):
        q = input("Enter query: ")
        out = {}
        for j in range(int(n[0])):
            h = all[j].object_info(q)
            v = all[j].info()
            out[h] = v

        sort_attribute(out)

    wish = input("Do you wish to restart, Y/N: ")
