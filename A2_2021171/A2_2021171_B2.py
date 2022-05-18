pq = [int(i) for i in input(
    "Initial number of Grammys with Doja Dog and DJ Snack respectively: ").split()]
mn = [int(i) for i in input(
    "The FanVille city, units tall and number of skyscrapers respectively: ").split()]
fv = []
print("Input layout of Fanville below(with no space(like in sample input))")
for _ in range(mn[0]):
    fv.append(list(input()))

doja_dog = pq[0]
dj_snake = pq[1]
doja_dog_reputation = 0
dj_snake_reputation = 0
a = -1
b = -1
c = 0
l = []

for i in fv:
    b = -1
    a += 1
    for j in i:
        b += 1
        if j == "1":
            if b not in l:
                c += 1
                if c % 2 == 1:
                    doja_dog_reputation += (mn[0] - a) * doja_dog
                    for g in range(a, mn[0]):
                        fv[g][b] = "D"

                else:
                    dj_snake_reputation += (mn[0] - a) * dj_snake
                    for g in range(a, mn[0]):
                        fv[g][b] = "S"
                dj_snake += 1
                doja_dog += 1
                l.append(b)

print(f"{doja_dog_reputation} {dj_snake_reputation}")
for i in fv:
    for j in i:
        print(j, end="")
    print("")
