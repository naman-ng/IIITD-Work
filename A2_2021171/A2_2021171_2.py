# from cmath import pi
import math
n = int(input("Number of vertices the 3D shape has: "))
x = [float(i) for i in input("x= ").split()]
y = [float(i) for i in input("y= ").split()]
z = [float(i) for i in input("z= ").split()]
q = int(input("Number of transformation queries to apply: "))

final_x = x
final_y = y
final_z = z
x1 = []
y1 = []
z1 = []


def scaling():
    global query
    global final_x
    global final_y
    global final_z
    for i in range(n):
        final_x[i] *= float(query[1])
        final_y[i] *= float(query[2])
        final_z[i] *= float(query[3])


def translating():
    global query
    global final_x
    global final_y
    global final_z
    for i in range(n):
        final_x[i] += float(query[1])
        final_y[i] += float(query[2])
        final_z[i] += float(query[3])


def rotation():
    global query
    global final_x
    global final_y
    global final_z
    global x1
    global y1
    global z1
    angle = float(query[2])  # Angle in Radian
    x1 = final_x
    y1 = final_y
    z1 = final_z
    final_x = []
    final_y = []
    final_z = []
    for i in range(n):
        final_x.append(0)
        final_y.append(0)
        final_z.append(0)
    if query[1] == "x":
        a = 0
        for i in x1:
            final_x[a] += i
            a += 1
        a = 0
        for i in y1:
            final_y[a] += math.cos(angle) * i
            final_z[a] += math.sin(angle) * i
            a += 1
        a = 0
        for i in z1:
            final_y[a] -= math.sin(angle) * i
            final_z[a] += math.cos(angle) * i
            a += 1
    if query[1] == "z":
        a = 0
        for i in z1:
            final_z[a] += i
            a += 1
        a = 0
        for i in x1:
            final_x[a] += math.cos(angle) * i
            final_y[a] += math.sin(angle) * i
            a += 1
        a = 0
        for i in y1:
            final_x[a] -= math.sin(angle) * i
            final_y[a] += math.cos(angle) * i
            a += 1
    if query[1] == "y":
        a = 0
        for i in y1:
            final_y[a] += i
            a += 1
        a = 0
        for i in x1:
            final_x[a] += math.cos(angle) * i
            final_z[a] -= math.sin(angle) * i
            a += 1
        a = 0
        for i in z1:
            final_x[a] += math.sin(angle) * i
            final_z[a] += math.cos(angle) * i
            a += 1


for i in range(q):
    query = input("Input a query: ").split()
    if query[0] == "S":
        scaling()
    if query[0] == "T":
        translating()
    if query[0] == "R":
        rotation()

# print(*final_x)  #For space seperated answer
# print(*final_y)
# print(*final_z)
print(final_x)
print(final_y)
print(final_z)

with open("F:\\CODE\\A2_2021171\\Q2_Final_Matrix.txt", mode="w") as file:
    file.write("x= ")
    for i in range(n):
        file.write(str(final_x[i]))
        file.write(" , ")
    file.write("\n")
    file.write("y= ")
    for i in range(n):
        file.write(str(final_y[i]))
        file.write(" , ")
    file.write("\n")
    file.write("z= ")
    for i in range(n):
        file.write(str(final_z[i]))
        file.write(" , ")
