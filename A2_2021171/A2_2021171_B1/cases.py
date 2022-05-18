import random

n = 0
number = 0
outputs = []
inputs = []


def function1(a):
    global outputs
    operation = a**2
    outputs.append(operation)


def generateData():
    global n
    global inputs
    global outputs
    global number
    n = int(input("Number of input-output pairs: "))
    for i in range(1, n + 1):
        a = random.randint(-100, 100)
        inputs.append(a)
        with open(f"F:\\CODE\\A2_2021171\\A2_2021171_B1\\Input_{i}.txt", mode="w") as file:
            file.write(str(a))
        function1(a)
    for i in outputs:
        number += 1
        with open(f"F:\\CODE\\A2_2021171\\A2_2021171_B1\\Output_{number}.txt", mode="w") as file:
            file.write(str(i))


generateData()
