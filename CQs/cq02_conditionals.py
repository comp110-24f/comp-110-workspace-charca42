"""CQ02. this prompts the user to enter a number, which is then compared to the secret
 number and a response is given"""

__author__ = "730391230"


def guess_a_number() -> None:
    secret: int = 7
    number: int = int(input("Guess a number:"))
    print("Your guess was " + str(number))
    if number == secret:
        print("You got it!")
    elif number < secret:
        print("Your guess was too low! The secret number is " + str(secret))
    else:
        print("Your guess was too high! The secret number is " + str(secret))
    return None


if __name__ == "__main__":
    guess_a_number()
