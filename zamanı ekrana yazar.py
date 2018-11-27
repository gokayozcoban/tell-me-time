import datetime
t = datetime.datetime.now()
soru = input("Do you want to know the time? ")
if (soru == "e") or (soru == "E") or (soru == "Y") or (soru == "y"):
    print("")
    print(t)
elif (soru == "h") or (soru == "H") or (soru == "N") or (soru == "n"):
    print("")
    print("Okey, see you at another time.")
else:
    print("")
    print("Sorry. I only created to tell time.")






