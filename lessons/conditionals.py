"""conditionals"""


def less_than_10(num: int) -> None:
    """tells if num < 10"""
    if num < 10:  # this is the "if" block that checks if num<10
        print("Big number")  # then block
    else:  # dont forget colon
        print("Small number")  # then block for the else response
    print("This is the end of the function")


def wake_up(alarm: bool) -> str:
    """returns a message based on if alarm is going off"""
    if alarm is True:
        return "Wake up!"
    else:
        return "Keep sleeping."


def check_first_letter(word: str, letter: str) -> str:
    """this checks if the first letter of word matches letter"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


def six(num: int) -> str:
    """testing if if-else can be nested in either the then or else block"""
    if num >= 5:
        if num == 6:
            return "six"
        else:
            return "not six"
    else:
        return "not six"


def get_weather_report() -> str:
    """asks user what the weather is and saves it as local var, then gives a response
    depending on the input"""
    weather: str = input("What is the weather?")
    if weather == "cold" or weather == "rainy":
        print("Bring a jacket!")
    elif weather == "hot":
        print("Keep cool out there!")
    else:
        print("I don't recognize this weather")
    return weather
