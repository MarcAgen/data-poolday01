##
## EPITECH PROJECT, 2026
## data-poolday01
## File description:
## task04
##
import json

class Budget:
    def __init__(self, json_path = None)->None:
        self._transactions:list[int | float] = []

        if json_path:
            with open(json_path, "r") as json_file:
                 data:dict = json.loads(json_file)
            if "transactions" not in data.keys:
                raise ValueError
            if type(data["transactions"] != list):
                raise ValueError
        self.add_transactions(data["transactions"])
            
            

    def add_transactions(self, lst: list[int | float]) -> None:
        for i in lst:
            if i != 0:
                self._transactions.append(i)
    
    def print_transactions(self):
        for i in self._transactions:
            if i == 0:
                continue
            print(f"You spent {i:.2f} euros" if (i < 0) else f"You received {i:.2d} euros")

    def print_sorted_transactions(self):
        for i in sorted(self._transactions):
            if i == 0:
                continue
            print(f"You spent {i:.2f} euros" if (i < 0) else f"You received {i:.2d} euros")

