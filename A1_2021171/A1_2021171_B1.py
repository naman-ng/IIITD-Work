i1 = float(input("Price of Item1:  "))
i2 = float(input("Price of Item2:  "))
i3 = float(input("Price of Item3:  "))
print("<-------------------------------------------------------------->")
print("<-------------------------------------------------------------->")
print("Discount Details")
comboPack1 = float(input("Provide discount (in percentage) for the 1st saver combo:  "))
comboPack2 = float(input("Provide discount (in percentage) for the 2nd saver combo:  "))
comboPack3 = float(input("Provide discount (in percentage) for the 3rd saver combo:  "))
phn = input("Provide your 10 digit contact number:  ")
print("The resulting catalogue is:")
print("<-------------------------------------------------------------->")
print("<-------------------------------------------------------------->")
print("7 Days\n" "DSS-112, Sector 9-11\n" "Hisar, Haryana :: 125001")
print("<-------------------------------------------------------------->")
print("<-------------------------------------------------------------->")
cpd1 = (i1 + i2) * (100 - comboPack1) / 100
cpd2 = (i1 + i3) * (100 - comboPack2) / 100
cpd3 = (i2 + i3) * (100 - comboPack3) / 100
ss = 0.72 * (i1 + i2 + i3)
print(
    f"Item               Price(per Pack)\n"
    f"Item1              {i1}\n"
    f"Item2              {i2}\n"
    f"Item3              {i3}\n"
    f"ComboPack1         {cpd1}\n"
    f"ComboPack2         {cpd2}\n"
    f"ComboPack3         {cpd3}\n"
    f"SuperSaver         {ss}\n"
)
print("<-------------------------------------------------------------->")
print("<-------------------------------------------------------------->")
print(f"For home delivery, contact here: {phn}")
