class LaundryService:
    def __init__(self, noc, coc, email, toc, branded, season):
        self.noc = noc
        self.coc = coc
        self.email = email
        self.toc = toc
        self.branded = branded
        self.season = season
        global id1
        id1 += 1
        self.id1 = id1

    def customerDetails(self):
        print("The customer specific details: ")
        print("")
        print("Customer id: ", self.id1)
        print("Customer Name: ", self.noc)
        print("Customer Contact Number: ", self.coc)
        print("Customer E-mail: ", self.email)
        print("Type of Cloth: ", self.toc)
        print("Branded or not: ", self.branded)

    def calculateCharge(self):
        charge = 0
        rate = {"Cotton": 50, "Silk": 30, "Woolen": 90, "Polyster": 20}
        charge += rate[self.toc]
        if self.branded:
            charge *= 1.5
        if self.season == "Winter":
            charge *= 0.5
        else:
            charge *= 2
        return round(charge, 2)

    def finalDetails(self):
        self.customerDetails()
        a = float(self.calculateCharge())
        print("Total charge: ", a)
        if a > 200:
            print("To be returned in 4 days")
        else:
            print("To be returned in 7 days")


id1 = 0
flag = True
while flag:
    noc = str(input("Name of customer: "))
    coc = int(input("Contact Number: "))
    email = str(input("Email: "))
    # dash = True
    # while dash:
    #     if email.isalnum():
    #         dash = False
    #     else:
    #         email = str(input("Email: "))
    toc = str(input("Type of cloth (“Cotton”, “Silk”, “Woolen” or “Polyester”) : "))
    branded = bool(int(input("Branded? (0/1): ")))
    season = str(input("Season: "))
    print("")
    obj = LaundryService(noc, coc, email, toc, branded, season)
    obj.finalDetails()
    a = input("Do you want to continue (y/n): ")
    if a == "y":
        flag = True
    else:
        flag = False
    print("")
