def getReverse(n):
    a = str(n)
    b = ""
    for i in a:
        b = i + b
    return b


def checkPalindrome(n):
    for i in range(len(str(n))):
        if str(n)[i] == str(n)[-(i + 1)]:
            flag = True
        else:
            flag = False
            break
    if flag:
        print("True")
    else:
        print("False")


def checkNarcissistic(n):
    b = len(str(n))
    a = 0
    for i in str(n):
        a += int(i) ** int(b)
    if a == int(n):
        print("True")
    else:
        print("False")


def findDigitSum(n):
    b = 0
    while len(str(n)) != 1:
        a = 0
        for i in str(n):
            a += int(i)
        b += a
        n = a
    return b


def findSquareDigitSum(n):
    b = 0
    while len(str(n)) != 1:
        a = 0
        for i in str(n):
            a += int(i) ** 2
        b += a
        n = a
    return b


flag = True
while flag == True:
    print(
        "Hello User, Welcome to the Application. Please select one of the following operations.\n"
        "1. Find reverse of a number\n"
        "2. Check whether a number is a palindrome or not.\n"
        "3. Check whether a number is a Narcissistic number or not.\n"
        "4. Find the sum of digits of a number\n"
        "5. Find the sum of squares of digits of a number.\n"
        "6. Select 6 to exit the application.\n"
    )
    m = int(input("Select the operation number --> "))
    if m == 1 or m == 2 or m == 3 or m == 4 or m == 5:
        n = abs(int(input("Input a number --> ")))
    if m == 1:
        print(getReverse(n))
    if m == 2:
        checkPalindrome(n)
    if m == 3:
        checkNarcissistic(n)
    if m == 4:
        print(findDigitSum(n))
    if m == 5:
        print(findSquareDigitSum(n))
    else:
        flag = False
