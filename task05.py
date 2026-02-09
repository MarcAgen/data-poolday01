##
## EPITECH PROJECT, 2026
## data-poolday01
## File description:
## task04
##
import json

class Budget:
    def __init__(self, json_path = None)->None:
        self._transactions:dict[str, list[int | float]] = {"income":[], "misc":[], "transportation":[]}

        if json_path:
            with open(json_path, "r") as json_file:
                 data:dict = json.loads(json_file)
            if "transactions" not in data.keys:
                raise ValueError
            if type(data["transactions"]) != list:
                raise ValueError
            for i in data["transactions"]:
                if type(i) != dict:
                    raise ValueError
            if "category" not in data.keys or "values" not in data.keys:
                raise ValueError
            if type(data["transactions"]["values"]) != list[int | float] or type(data["transactions"]["category"]) != str:
                raise ValueError
        self.add_transactions(data["transactions"])
            
    def get_categories(self)->list[str]:
        return sorted(self._transactions.keys)

    def add_transactions(self, lst: list[dict[str, list[int | float]]]) -> None:
        for i in lst:
            for y in lst["values"]:
                if y != 0:
                    self._transactions[f"{i["category"]}"].append(y)

    def print_transactions(self, category:str=None):
        if category != None:
            print(f"[{i}]")
            for i in self._transactions[f"{category}"]:
                print(f"You spent {i:.2f} euros" if (i < 0) else f"You received {i:.2d} euros")
                print("")
        else:
            for i in self._transactions.keys:
                self.print_transactions(i)

    def print_sorted_transactions(self, category:str=None):
        if category != None:
            print(f"[{i}]")
            for i in sorted(self._transactions[f"{category}"]):
                print(f"You spent {i:.2f} euros" if (i < 0) else f"You received {i:.2d} euros")
                print("")
        else:
            for i in sorted(self._transactions.keys):
                self.print_transactions(i)
