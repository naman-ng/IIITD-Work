dop = int(input("Degree of the polynomial-->"))
list1 = []
for i in range(dop + 1):
    coeff = int(input(f"Coefficient {i+1} :"))
    list1.append(coeff)
lb = int(input("Lower bound for X-->"))
ub = int(input("Upper bound for X-->"))
inc = int(input("Steps in which you would vary X-->"))
print("<--------------------------------------------------->")
ans = 0
list2 = []
for j in range(lb, (ub + 1), inc):
    list2.append(j)
for k in list2:
    x = dop
    for i in list1:
        ans += int(i) * (k**x)
        if x >= 0:
            x -= 1
    ans1 = round(ans)
    if ans1 >= 0:
        for _ in range(ans1):
            print("*", end="")
        print("")
    else:
        print("")
    ans = 0
