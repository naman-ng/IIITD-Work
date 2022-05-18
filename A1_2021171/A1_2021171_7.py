l = [float(i) for i in input().split()]
a = int(input())
b = int(input())
d = int(input())


def calculate_area(l, a, b, d):
    final = 0
    fx = 0
    fy = 0
    fxy = 0
    for i in range(int((b-a)/d)):
        for j in l:
            fx += a**j
            fy += (a+d)**j
            fxy += ((a+a+d)/2)**j
        a += d
    final += (d/6)*(fx + 4*fxy + fy)
    return (final)


if (b-a) % d == 0:
    print(calculate_area(l, a, b, d))
