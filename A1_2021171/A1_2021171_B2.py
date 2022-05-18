e = [float(i) for i in input("The origin of light ray is-->").split()]
d = [float(i) for i in input("The direction of light ray is-->").split()]
c = [float(i) for i in input("Center of the Circle-->").split()]
r = float(input())
for t in range(1001):
    final = [(e[i] + d[i] * t) for i in range(3)]
    if (
        (final[0] - c[0]) ** 2 + (final[1] - c[1]) ** 2 + (final[2] - c[2]) ** 2
    ) == r**2:
        print(f"Yes line intersects sphere at point {final} on step {t} ")
        continue
    if (
        (final[0] - c[0]) ** 2 + (final[1] - c[1]) ** 2 + (final[2] - c[2]) ** 2
    ) > r**2:
        if t == 0:
            flag = False
        b = final
        if flag == True:
            flag = False
            print(
                f"Yes line intersects sphere between points {a} at t = {t-1} and {b} at {t} "
            )
    if (
        (final[0] - c[0]) ** 2 + (final[1] - c[1]) ** 2 + (final[2] - c[2]) ** 2
    ) < r**2:
        if t == 0:
            flag = True
        a = final
        if flag == False:
            flag = True
            print(
                f"Yes line intersects sphere between points {b} at t = {t-1} and {a} on step {t} "
            )

print("exit")
