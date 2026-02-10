##
## EPITECH PROJECT, 2026
## data-poolday01
## File description:
## task03
##

class Budget:
    def __init__(self)->None:
        self._transactions:list[int | float] = []
    
    def add_transactions(self, lst: list[int | float]) -> None:
        for i in lst:
            if i != 0:
                self._transactions.append(i)
    def print_transactions(self):
        for i in self._transactions:
            if i == 0:
                continue
            print(f"You spent {abs(i):.2f} euros" if (i < 0) else f"You received {i:.2f} euros")

    def print_sorted_transactions(self):
        for i in sorted(self._transactions):
            if i == 0:
                continue
            print(f"You spent {abs(i):.2f} euros" if (i < 0) else f"You received {i:.2f} euros")

