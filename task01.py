##
## EPITECH PROJECT, 2026
## day01
## File description:
## task01
##

def print_transactions(lst: list[int | float]) -> None:
    for i in lst:
        if i == 0:
            continue
        print(f"You spent {abs(i):.2f} euros" if (i < 0) else f"You received {i:.2f} euros")
