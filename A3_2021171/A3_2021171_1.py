import math


def scale(x, y, z, sx, sy, sz):
    x1 = []
    y1 = []
    z1 = []
    for i in range(4):
        x1.append(x[i] * sx)
        y1.append(y[i] * sy)
        z1.append(z[i] * sz)
    return x1, y1, z1


def translate(x, y, z, tx, ty, tz):
    x1 = []
    y1 = []
    z1 = []
    for i in range(4):
        x1.append(x[i] + tx)
        y1.append(y[i] + ty)
        z1.append(z[i] + tz)
    return x1, y1, z1


def rotate(x, y, z, axis, phi):
    x1 = []
    y1 = []
    z1 = []
    if axis == "x":
        for i in x:
            x1.append(i)
        for i in y:
            y1.append(math.cos(phi) * i)
            z1.append(math.sin(phi) * i)
        for i in z:
            y1.append(math.sin(phi) * i)
            z1.append(math.cos(phi) * i)
    if axis == "z":
        for i in z:
            z1.append(i)
        for i in x:
            x1.append(math.cos(phi) * i)
            y1.append(math.sin(phi) * i)

        for i in y:
            x1.append(-math.sin(phi) * i)
            y1.append(math.cos(phi) * i)

    if axis == "y":
        for i in y:
            y1.append(i)
        for i in x:
            x1.append(math.cos(phi) * i)
            z1.append(-math.sin(phi) * i)
        for i in z:
            x1.append(math.sin(phi) * i)
            z1.append(math.cos(phi) * i)
    return x1, y1, z1


def matmul(A, B):
    ans = []
    if len(A[0]) == len(B):
        for i in range(len(A)):
            ans.append([])
            for j in range(len(B[0])):
                ans[i].append(0)
                for k in range(len(B)):
                    ans[i][j] += A[i][k] * B[k][j]
        return ans
    else:
        return ("Matrices are not multiplicable")
