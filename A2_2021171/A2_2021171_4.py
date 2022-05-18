with open("F:\\CODE\\A2_2021171\\Q4\\Q4\\Admin\\RegisteredStudents.txt") as file:
    lines = file.readlines()
    student = {}
    for line in lines:
        x = line.strip().split(" ")
        student[x[0]] = x[1]

with open("F:\\CODE\\A2_2021171\\Q4\\Q4\\Admin\\AnswerKey.txt") as file:
    ak = []
    lines_ak = file.readlines()
    for line in lines_ak:
        y = line.strip().split(" ")
        ak.append(y)

scores = []
for key in student:
    with open(f"F:\\CODE\\A2_2021171\\Q4\\Q4\\Student\\{key}_{student[key]}.txt") as file:
        line_stud = file.readlines()
        score = 0
        lol = -1
        for line in line_stud:
            lol += 1
            x = line.strip().split(" ")
            if x[1] == "-":
                score += 0
            elif x[1] == ak[lol][1]:
                score += 4
            elif x[1] != ak[lol][1]:
                score -= 1
        scores.append(score)

with open("F:\\CODE\\A2_2021171\\Q4\\Q4\\Admin\\FinalReport.txt", mode="w") as file:
    f = -1
    for key in student:
        f += 1
        file.write(f"{key} {student[key]} {scores[f]}\n")
