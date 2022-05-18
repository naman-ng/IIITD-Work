def f1():
    list1 = [True, False]
    for b1 in list1:
        for b2 in list1:
            if (b1 and not b1):
                print("satisfiable")
                print(b1, b2)
                return
    print("unsatisfiable")


def f2():
    list1 = [True, False]
    for b1 in list1:
        for b2 in list1:
            for b3 in list1:
                if (b1 or b2) and (b2 or not b3):
                    print("satisfiable")
                    print(b1, b2, b3)
                    return
    print("unsatisfiable")


f1()
f2()
