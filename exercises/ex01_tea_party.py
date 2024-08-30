"""Asks the user for the number of guests, then calculates the number of tea bags and
 treats needed, as well as the expected cost."""

__author__: str = "730391230"


# need a function to bring previous ones together through calls and produces a print
#  output
def main_planner(guests: int) -> None:
    """This is the entrypoint of the program"""
    # does not return value, it prints an output. no return statement
    print("A Cozy Tea Party for " + str(guests) + " People!")
    # convert the values into strings to add them together
    # how to convert guest input into people. oh wait you can just put guests
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    # need 2 arguments for cost. maybe call function inside of that function
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))


# need a function to compute the number of bags based on guests
def tea_bags(people: int) -> int:
    """This defines the function 'tea_bags' as an integer"""
    # plan for everyone to drink 2 cups of tea
    return people * 2


# need a function to compute the number of 'treats'
# based on the number of tea
def treats(people: int) -> int:
    """This defines 'treats' as 1.5 * the number of tea bags"""
    # this has to return the input of tea bag as an int. it needs a keyword argument
    return int(tea_bags(people=people) * 1.5)


# need a function to assign cost to the functions, and to sum cost
def cost(tea_count: int, treat_count: int) -> float:
    """This returns the cost of the tea and treats given how many there are"""
    # make a sum of the parameters
    return tea_count * 0.5 + treat_count * 0.75


# this bit here makes the program run and prompt an input if correct user
if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
