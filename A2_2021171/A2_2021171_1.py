print("1. Display specific word count \n"
      "2. Display all unique words \n"
      "3. Display all word counts\n"
      "4. Replace word \n"
      "5. Quit \n")


def specific_word_count():
    word = input("Enter word: ")
    a = 0
    with open("question1_input.txt") as file:
        lines = file.readlines()
        for line in lines:
            x = line.strip().split(" ")
            for y in x:
                if y == word:
                    a += 1
        if a == 0:
            print("Word does not exist")
        else:
            print("Word count: ", a)


def Display_Unique_Words():
    with open("question1_input.txt") as file:
        lines = file.readlines()
        z = []
        for line in lines:
            x = line.strip().split(" ")
            for y in x:
                if y not in z:
                    z.append(y)
        print(*z, sep=" ; ")
    print("")


def Display_all_Word_Counts():
    with open("question1_input.txt") as file:
        lines = file.readlines()
        z = []
        for line in lines:
            x = line.strip().split(" ")
            for y in x:
                z.append(y)
        u = []
        for y in z:
            if y not in u:
                u.append(y)
                w = z.count(y)
                print(f"{y} : {w} ")


def repalce_word():
    word1 = input("Enter word to be replaced: ")
    word2 = input("Enter word that will replace it: ")
    with open("question1_input.txt") as file:
        lines = file.readlines()
        z = []
        for line in lines:
            x = line.strip().split(" ")
            for y in x:
                if y == word1:
                    a = x.index(y)
                    x[a] = word2
            z.append(x)
        l1 = []
        for i in z:
            t = " ".join(i)
            t += "\n"
            l1.append(t)
    with open("question1_input.txt", "w") as file1:
        file1.writelines(l1)


flag = True
while flag:
    option = int(input("Enter your choice: "))
    if option == 1:
        specific_word_count()
    if option == 2:
        Display_Unique_Words()
    if option == 3:
        Display_all_Word_Counts()
    if option == 4:
        repalce_word()
    if option == 5:
        flag = False
