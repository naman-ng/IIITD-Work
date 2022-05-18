def noteCreate():
    global major_scale
    global minor_scale
    with open("scaleMajor.txt", mode="w") as file:
        for i in major_scale:
            for j in i:
                file.write(j)
                file.write(" ")
            file.write("\n")
    with open("scaleMinor.txt", mode="w") as file:
        for i in minor_scale:
            for j in i:
                file.write(j)
                file.write(" ")
            file.write("\n")


def majorNotes(root):
    with open("scaleMajor.txt") as file:
        lines = file.readlines()
        for line in lines:
            x = []
            x = line.strip().split(" ")
            if x[0] == root_note:
                print(*x)


def minorNotes(root):
    with open("scaleMinor.txt") as file:
        lines = file.readlines()
        for line in lines:
            x = []
            x = line.strip().split(" ")
            if x[0] == root_note:
                print(*x)


root_note = input("Enter the root note: ")
scale_type = input("Enter the type of scale (Major/Minor): ")

l = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
major_scale = []
minor_scale = []
mas = [0, 2, 4, 5, 7, 9, 11, 12]
mis = [0, 2, 3, 5, 7, 8, 10, 12]
for a in range(12):
    scale = []
    for i in range(a, a + 12):
        majorsc = []
        minorsc = []
        scale.append(l[i % 12])
    ho = l[a] + "'"
    scale.append(ho)
    for i in mas:
        majorsc.append(scale[i])
    for i in mis:
        minorsc.append(scale[i])
    major_scale.append(majorsc)
    minor_scale.append(minorsc)
# print(major_scale)
# print(minor_scale)
noteCreate()
if scale_type == "Major":
    majorNotes(root=root_note)
if scale_type == "Minor":
    minorNotes(root=root_note)
