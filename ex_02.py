class Budget:

    def __init__(self):
        self._transactions = []

    def add_transactions(self, values):
        self._transactions.extend(values)

    def print_sorted_transactions(self):
        sorted_transactions = sorted(self._transactions)
        for i in sorted_transactions :
            if(i >0):
                print("You received", i,"euros")
        if(i <0):
            i = i *-1
            print("You spent", i,"euros")   

    def print_transactions(self):
        for i in self._transactions :
            if(i >0):
                print("You received", i,"euros")
        if(i <0):
            i = i *-1
            print("You spent", i,"euros")

myBudget = Budget()
myBudget.add_transactions([512, 42.08, -12])
myBudget.add_transactions([-9000])
myBudget.print_transactions()
myBudget.print_sorted_transactions()

       


        

    