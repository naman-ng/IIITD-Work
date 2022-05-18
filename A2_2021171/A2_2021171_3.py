super = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
flag = True


def decimal_to_binary(n):
    a = ""
    while n > 0:
        a += str(n % 2)
        n = int(n / 2)
    print(a[::-1])


def binary_to_decimal(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    for i in str(a):
        if i in super[:2]:
            c += int(i) * 2**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        print(c)


def decimal_to_hexadecimal(n):
    a = ""
    l = ["A", "B", "C", "D", "E", "F"]
    while n > 0:
        b = n % 16
        if b > 9:
            b = l[b - 10]
        a += str(b)
        n = int(n / 16)
    print(a[::-1])


def hexadecimal_to_decimal(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    l = ["A", "B", "C", "D", "E", "F"]
    for i in str(a):
        if i in super[:16]:
            if i in l:
                i = l.index(i) + 10
            c += int(i) * 16**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        print(c)


def decimal_to_octal(n):
    a = ""
    while n > 0:
        a += str(n % 8)
        n = int(n / 8)
    print(a[::-1])


def octal_to_decimal(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    for i in str(a):
        if i in super[:8]:
            c += int(i) * 8**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        print(c)


def binary_to_hexadecimal(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    for i in str(a):
        if i in super[:2]:
            c += int(i) * 2**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        l = ["A", "B", "C", "D", "E", "F"]
        while c > 0:
            b = c % 16
            if b > 9:
                b = l[b - 10]
            z += str(b)
            c = int(c / 16)
        print(z[::-1])


def hexadecimal_to_binary(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    l = ["A", "B", "C", "D", "E", "F"]
    for i in str(a):
        if i in super[:16]:
            if i in l:
                i = l.index(i) + 10
            c += int(i) * 16**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        while c > 0:
            z += str(c % 2)
            c = int(c / 2)
        print(z[::-1])


def binary_to_octal(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    for i in str(a):
        if i in super[:2]:
            c += int(i) * 2**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        while c > 0:
            z += str(c % 8)
            c = int(c / 8)
        print(z[::-1])


def octal_to_binary(n):
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    for i in str(a):
        if i in super[:8]:
            c += int(i) * 8**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        while c > 0:
            z += str(c % 2)
            c = int(c / 2)
        print(z[::-1])


def hexadecimal_to_octal(n):
    a = str(n)[::-1]
    flag = True
    b = 0
    c = 0
    l = ["A", "B", "C", "D", "E", "F"]
    for i in str(a):
        if i in super[:16]:
            if i in l:
                i = l.index(i) + 10
            c += int(i) * 16**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        while c > 0:
            z += str(c % 8)
            c = int(c / 8)
        print(z[::-1])


def octal_to_hexadecimal(n):
    a = str(n)[::-1]
    b = 0
    c = 0
    flag = True
    for i in str(a):
        if i in super[:8]:
            c += int(i) * 8**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        l = ["A", "B", "C", "D", "E", "F"]
        while c > 0:
            b = c % 16
            if b > 9:
                b = l[b - 10]
            z += str(b)
            c = int(c / 16)
        print(z[::-1])


def radixA_to_radixB(n):
    global radixA
    global radixB
    flag = True
    a = str(n)[::-1]
    b = 0
    c = 0
    alpha = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in str(a):
        if i in super[:radixA]:
            if i in alpha:
                i = alpha.index(i) + 10
            c += int(i) * radixA**b
            b += 1
        else:
            print("Enter correct number")
            flag = False
            break
    if flag:
        z = ""
        while c > 0:
            b = c % radixB
            if b > 9:
                b = alpha[b - 10]
            z += str(b)
            c = int(c / radixB)
        print(z[::-1])


print('''1) Convert decimal to binary
2) Conver binary to decimal
3) Convert decimal to hexadecimal
4) Convert hexadecimal to decimal 
5) Convert decimal to octal.
6) Convert octal to decimal. 
7) Convert binary to hexadecimal.
8) Convert hexadecimal to binary.
9) Convert binary to octal.
10) Convert octal to binary.
11) Convert hexadecimal to octal.
12) Convert octal to hexadecimal.
13) Convert number with radix A to radix B. Here A,B <= 36.
14) Exit''')
slag = True
while slag:
    x = int(input("Choose option number from above menu: "))
    if x == 1:
        n = input("Enter the number: ")
        decimal_to_binary(int(n))
    elif x == 2:
        n = input("Enter the number: ")
        binary_to_decimal(int(n))
    elif x == 3:
        n = input("Enter the number: ")
        decimal_to_hexadecimal(int(n))
    elif x == 4:
        n = input("Enter the number: ")
        hexadecimal_to_decimal(n)
    elif x == 5:
        n = input("Enter the number: ")
        decimal_to_octal(int(n))
    elif x == 6:
        n = input("Enter the number: ")
        octal_to_decimal(int(n))
    elif x == 7:
        n = input("Enter the number: ")
        binary_to_hexadecimal(int(n))
    elif x == 8:
        n = input("Enter the number: ")
        hexadecimal_to_binary(n)
    elif x == 9:
        n = input("Enter the number: ")
        binary_to_octal(int(n))
    elif x == 10:
        n = input("Enter the number: ")
        octal_to_binary(int(n))
    elif x == 11:
        n = input("Enter the number: ")
        hexadecimal_to_octal(n)
    elif x == 12:
        n = input("Enter the number: ")
        octal_to_hexadecimal(int(n))
    elif x == 13:
        radixA = int(input("Enter value of A: "))
        radixB = int(input("Enter value of B: "))
        n = input("Enter the number: ")
        radixA_to_radixB(n)
    elif x == 14:
        slag = False
    else:
        print("Input correct menu number")
