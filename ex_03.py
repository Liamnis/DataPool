import json

class Budget:

    def __init__(self, json_file=None):
        self.transactions = {}

        if json_file:
            self.load_from_json(json_file)

    def load_from_json(self, json_file):
        with open(json_file, 'r') as file:
            data = json.load(file)

        for transaction in data.get("transactions", []):
            category = transaction["category"]
            values = transaction["value"]
            # Vérifie la catégorie n'existe pas déjà, elle l'a crée
            if category not in self.transactions:
                self.transactions[category] = []

            self.transactions[category].extend(values)

    def get_categories(self):
        return list(self.transactions.keys())
#Retourne la liste ou se situe les clés du dictionnaire
    def print_sorted_transactions(self, category=None):
        if category:
            transactions = self.transactions.get(category, [])
        else:
            transactions = [amount for amounts in self.transactions.values() for amount in amounts]

        sorted_transactions = sorted(transactions)
        for i in sorted_transactions:
            if i > 0:
                print(f"You received {i} euros")
            elif i < 0:
                i = abs(i)
                print(f"You spent {i} euros")

    def print_transactions(self, category=None):
        if category:
            transactions = self.transactions.get(category, [])
        else:
            transactions = [amount for amounts in self.transactions.values() for amount in amounts]

        for i in transactions:
            if i > 0:
                print(f"You received {i} euros")
            elif i < 0:
                i = abs(i)
                print(f"You spent {i} euros")

myBudget = Budget("C:/Users/liamn/Desktop/DataPool/path.json")
for category in myBudget.get_categories():
    myBudget.print_sorted_transactions(category)
myBudget.print_transactions()
