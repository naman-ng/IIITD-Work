initial_cost = int(input("Initial cost: "))
depreciation = int(input("Depreciation rate: "))
cost_of_owning = 0
value = 50 * 6000
cost = initial_cost
for i in range(1, 16):
    value *= 1.1
    if i <= 5:
        cost -= i * (initial_cost / 100) + depreciation * (initial_cost / 100)
    else:
        cost -= (5 * (initial_cost / 100) * 1.5 * (i - 5)) + depreciation * (
            initial_cost / 100
        )
    if float(cost) <= float(value):
        print(f"Year is {i} ")
        break
