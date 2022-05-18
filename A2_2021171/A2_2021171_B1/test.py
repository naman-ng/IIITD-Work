import cases

verification = []


def function2(line):
    global verification
    verify = 0
    # Deliberately not used "Abs" function in line 11 so that I can get FAILED cases for negative nos.
    for _ in range(abs(line)):
        verify += line
    verification.append(verify)


def testing():
    w = []
    for i in range(1, cases.n + 1):
        with open(f"F:\\CODE\\A2_2021171\\A2_2021171_B1\\Input_{i}.txt") as file:
            line = file.readline()
            line = int(line.strip())
            function2(line)
    for i in range(1, cases.n + 1):
        with open(f"F:\\CODE\\A2_2021171\\A2_2021171_B1\\Output_{i}.txt") as file:
            line = file.readline()
            line = int(line.strip())
            w.append(line)
    for i in range(cases.n):
        if verification[i] == w[i]:
            print(f"{verification[i]} = {w[i]} SUCCESS ")
        if verification[i] != w[i]:
            print(f"{verification[i]} != {w[i]} FAILED ")


testing()
