n = int(input("Input size of matrix: "))
matrix = {}
for i in range(n):
    matrix[i] = input().split()
# print(matrix)
print(
    "1) Normal traversal\n"
    "2) Alternating traversal\n"
    "3) Spiral traversal from outer to inwards\n"
    "4) Boundary traversal.\n"
    "5) Diagonal traversal from right to left\n"
    "6) Diagonal traversal from left to right.\n"
    "7) EXIT \n"
)


def f1():
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
    print("")


def f2():
    b = 0
    for i in range(n):
        b += 1
        for j in range(n):
            if b % 2 != 0:
                print(matrix[i][j], end=" ")
            else:
                print(matrix[i][n - j - 1], end=" ")
    print("")


def f3():
    a = n - 1
    b = 0
    x = n - 1
    h = 0
    if n % 2 == 0:
        y = int(n / 2)
    else:
        y = int(n / 2) + 1
    for j in range(y):
        h = j
        for i in range(x + 1):
            print(matrix[b][h], end=" ")
            h += 1
        h = j
        for i in range(x):
            h += 1
            print(matrix[h][a], end=" ")
        h = j
        for i in range(x):
            h += 1
            print(matrix[a][n - 1 - h], end=" ")
        h = j
        for i in range(x - 1):
            h += 1
            print(matrix[n - 1 - h][b], end=" ")
        x -= 2
        a -= 1
        b += 1
    print("")


def f4():
    a = n - 1
    b = 0
    x = n - 1
    h = 0
    j = 0
    for i in range(x + 1):
        print(matrix[b][h], end=" ")
        h += 1
    h = j
    for i in range(x):
        h += 1
        print(matrix[h][a], end=" ")
    h = j
    for i in range(x):
        h += 1
        print(matrix[a][n - 1 - h], end=" ")
    h = j
    for i in range(x - 1):
        h += 1
        print(matrix[n - 1 - h][b], end=" ")
    print("")


def f5():
    dic = {}
    for i in range(2 * (n - 1) + 1):
        for j in range(n):
            for k in range(n):
                if (j + k) == i:
                    dic[j] = k
        for j in dic:
            block = matrix[j][dic[j]]
            print(block, end=" ")
        dic = {}
    print("")


def f6():
    x = n
    y = 0
    h = n
    for i in range(2 * n):
        if x == 0:
            y += 1
        else:
            x -= 1
        if i < n:
            f = x
            g = y
            for j in range(i + 1):
                block = matrix[g][f]
                print(block, end=" ")
                g += 1
                f += 1
        else:
            f = x
            g = y
            h -= 1
            for j in range(h):
                block = matrix[g][f]
                print(block, end=" ")
                g += 1
                f += 1
    print("")


flag = True
while flag:
    choice = int(input("Choose traversal no. from above menu: "))
    if choice == 1:
        f1()
    if choice == 2:
        f2()
    if choice == 3:
        f3()
    if choice == 4:
        f4()
    if choice == 5:
        f5()
    if choice == 6:
        f6()
    if choice == 7:
        flag = False
