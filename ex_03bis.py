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

            if category not in self.transactions:
                self.transactions[category] = []

            self.transactions[category].extend(values)

    def get_categories(self):
        return list(self.transactions.keys())

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

    def add_transactions(self, values, category):
        if category not in self.transactions:
            self.transactions[category] = []
        
        self.transactions[category].extend(values)

    def save_to_json(self, json_file):
        data = {"transactions": []}

        for category, transactions in self.transactions.items():
            for value in transactions:
                data["transactions"].append({"category": category, "value": value})

        with open(json_file, 'w') as file:
            json.dump(data, file, indent=4)


myBudget = Budget("C:/Users/liamn/Desktop/DataPool/path.json")
myBudget.add_transactions([-12, -102.13], "corn for poney")
myBudget.save_to_json("data.json")

for category in myBudget.get_categories():
    myBudget.print_transactions(category)
