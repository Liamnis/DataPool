def print_transactions(valeur):
    for i in valeur:
        if(i >0):
            print("You received", i,"euros")
        if(i <0):
            i = i *-1
            print("You spent", i,"euros")

        


print_transactions([-10, -600, 700, 20])
