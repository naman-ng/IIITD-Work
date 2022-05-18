from cmath import pi

n = int(input("No. of students-->"))
for _ in range(n):
    print(
        "1.Square\n"
        "2.Rectangle\n"
        "3.Rhombus\n"
        "4.Parallelogram\n"
        "5.Circle\n"
        "6.Cube\n"
        "7.Cuboid\n"
        "8.Right circular cone\n"
        "9.Hemisphere\n"
        "10.Sphere\n"
        "11.Solid Cylinder\n"
        "12.Hollow Cylinder\n"
        "13.EXIT"
    )
    dimension = input("2D or 3D\n")
    if dimension == "2D":
        print(
            "1.Square\n" "2.Rectangle\n" "3.Rhombus\n" "4.Parallelogram\n" "5.Circle\n"
        )
    elif dimension == "3D":
        print(
            "6.Cube\n"
            "7.Cuboid\n"
            "8.Right circular cone\n"
            "9.Hemisphere\n"
            "10.Sphere\n"
            "11.Solid Cylinder\n"
            "12.Hollow Cylinder\n"
            "13.EXIT"
        )
    shape = int(input("Select any shape from the chosen dimension.-->"))
    if shape == 13:
        continue
    if shape == 1:
        l = int(input("Side Length-->"))
        perimeter = 4 * l
        area = l * l
        print(f"Perimeter is {perimeter}m\nArea is {area}sq.m")
    if shape == 2:
        l = int(input("Side Length-->"))
        b = int(input("Side Breadth-->"))
        perimeter = 2 * (l + b)
        area = l * b
        print(f"Perimeter is {perimeter}m\nArea is {area}sq.m")
    if shape == 3:
        l = int(input("Side Length-->"))
        d1 = int(input("1st Diagonal-->"))
        d2 = int(input("2nd Diagonal-->"))
        if d1 <= 2 * l and d2 <= 2 * l:
            perimeter = 4 * l
            area = d1 * d2 * 1 / 2
            print(f"Perimeter is {perimeter}m\nArea is {area}sq.m")
    if shape == 4:
        l = int(input("Side Length-->"))
        b = int(input("Side breadth-->"))
        h = int(input("Height-->"))
        perimeter = 2 * (l + b)
        area = b * h
        print(f"Perimeter is {perimeter}m\nArea is {area}sq.m")
    if shape == 5:
        l = int(input("Radius-->"))
        perimeter = 2 * pi * l
        area = pi * l * l
        print(f"Perimeter is {perimeter}m\nArea is {area}sq.m")
    if shape == 6:
        l = int(input("Side Length-->"))
        csa = l * l * 4
        tsa = l * l * 6
        vol = l * l * l
        print(f"CSA is {csa}, TSA is {tsa} and Volume is {vol} ")
    if shape == 7:
        l = int(input("Length-->"))
        b = int(input("Breadth-->"))
        h = int(input("Height-->"))
        csa = (b + l) * 2 * h
        tsa = (b * h + l * h + l * b) * 2
        vol = l * b * h
        print(f"CSA is {csa}, TSA is {tsa} and Volume is {vol} ")
    if shape == 8:
        r = int(input("Radius-->"))
        h = int(input("Height-->"))
        l = (h * h + r * r) ** 1 / 2
        csa = pi * r * l
        tsa = pi * r * (r + l)
        vol = 1 / 3(pi * r * r * h)
        print(f"CSA is {csa}, TSA is {tsa} and Volume is {vol} ")
    if shape == 9:
        l = int(input("Radius-->"))
        csa = r * r * pi * 2
        tsa = r * r * pi * 3
        vol = r * r * pi * 2 / 3 * r
        print(f"CSA is {csa}, TSA is {tsa} and Volume is {vol} ")
    if shape == 10:
        l = int(input("Radius-->"))
        csa = r * r * pi * 4
        tsa = r * r * pi * 4
        vol = r * r * pi * 4 / 3 * r
        print(f"CSA and TSA is {tsa} and Volume is {vol} ")
    if shape == 11:
        r = int(input("Radius-->"))
        h = int(input("Height-->"))
        csa = pi * h * r * 2
        tsa = r * pi * 2 * (r + h)
        vol = pi * r * r * h
        print(f"CSA is {csa}, TSA is {tsa} and Volume is {vol} ")
    if shape == 12:
        r = int(input("Inner Radius-->"))
        R = int(input("Outer Radius-->"))
        h = int(input("Height-->"))
        csa = pi * h * (r + R) * 2
        tsa = (h * pi * 2 * (r + R)) + 2 * pi * (R**2 - r**2)
        vol = pi * (R**2 - r**2) * h
        print(f"CSA is {csa}, TSA is {tsa} and Volume is {vol} ")
    if shape == 13:
        continue
