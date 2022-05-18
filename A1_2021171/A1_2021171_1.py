print(
    "1.Right-angled triangle\n"
    "2.Isoceles Triangle\n"
    "3.Kite\n"
    "4.Half Kite\n"
    "5.X\n"
)
triangle = input()
n = int(input())
if triangle == "1":
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")
if triangle == "4":
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print("")
    for i in range(1, n):
        for j in range(1, n + 1 - i):
            print(j, end=" ")
    print("")
if triangle == "2" and n % 2 == 0:
    for i in range(n):
        z = 0
        for j in range(1, (2 * n)):
            if n - i <= j <= n + i:
                z += 1
                print(z, end="")
            else:
                print(" ", end="")
        print("")
if triangle == "3" and n % 2 == 0:
    for i in range(n):
        z = 0
        for j in range(1, (2 * n)):
            if n - i <= j <= n + i:
                z += 1
                print(z, end="")
            else:
                print(" ", end="")
        print("")
    for i in reversed(range(n - 1)):
        z = 0
        for j in range(1, (2 * n)):
            if n - i <= j <= n + i:
                z += 1
                print(z, end="")
            else:
                print(" ", end="")
        print("")
if triangle == "5" and n % 2 == 0:
    for i in reversed(range(n)):
        z = 0
        for j in range(1, (2 * n)):
            if n - i <= j <= n + i:
                z += 1
                print(z, end="")
            else:
                print(" ", end="")
        print("")
    for i in range(1, n):
        z = 0
        for j in range(1, (2 * n)):
            if n - i <= j <= n + i:
                z += 1
                print(z, end="")
            else:
                print(" ", end="")
        print("")
