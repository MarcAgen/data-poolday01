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
        for i in data["transactions"]:
            self.add_transactions(i["values"], i["category"])


    def get_categories(self)->list[str]:
        return sorted(self._transactions.keys)


    def add_transactions(self, values: list[int | float], category: str) -> None:
        if (all(val == 0 for val in values)):
            return
        if category not in self._transactions.keys:
            self._transactions[f"{category}"] = []
        for i in values:
            if i != 0:
                self._transactions[f"{category}"].append(i)


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

    def save_transactions(self, output_path: str):
        with open(output_path, "w") as f:
            f.write("{\n\t\"transaction\": [\n")
            for i in range (len(self._transactions.keys)):
                if self._transactions[f"{self._transactions.keys[i]}"] == []:
                    continue
                f.write("\t\t " + "{" + f" \"category\": \"{self._transactions.keys[i]}\", \"values\": {self._transactions[f"{self._transactions.keys[i]}"]} " + "},\n")
            f.write("\t]\n}")
