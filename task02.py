##
## EPITECH PROJECT, 2026
## data-poolday01
## File description:
## task02
##

def print_sorted_transactions(lst: list[int | float]) -> None:
    for i in sorted(lst):
        if i == 0:
            continue
        print(f"You spent {abs(i):.2f} euros" if (i < 0) else f"You received {i:.2d} euros")

