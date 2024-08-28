"""Practice With Functions"""

from random import randint


# Define a function
def sum(num1: int, num2: int) -> int:
    """Return num1 + num2."""
    return num1 + num2


# Call a function
# print(sum(num1=1, num2=10))  # 1 and 10 are arguments
print(sum(num1=randint(1, 10), num2=randint(1, 10)))
