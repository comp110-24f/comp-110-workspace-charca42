"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730391230"


# this calls the other functions in the order i want so its not annoying
def main():
    contains_char(word=input_word(), letter=input_letter())


def input_word() -> str:
    # no parameters so this needs to get an input from user
    # i need to define the word local variable and assign it an input
    word: str = str(input("Enter a 5-character word:"))
    if (len(word) > 5) or (len(word) < 5):
        print("Error: Word must contain 5 characters.")
        # add the exit here after the error message
        exit()
        return word
    # need a way to check word length and determine if it is appropriate, as well as
    #  return it
    else:
        return word


def input_letter() -> str:
    # local variable str, gonna call it letter. it should ask the user for a single
    # character. i need to make it be able to store this and return errors if not 1
    #  character long
    letter: str = str(input("Enter a single character:"))
    if (len(letter) > 1) or (len(letter) < 1):
        print("Error: Character must be a single character.")
        exit()
        return letter
    else:
        return letter


def contains_char(word: str, letter: str) -> None:
    # this has to take the input word from input_word and the character from
    # input_character. this will be in a call within the call
    print("Searching for " + letter + " in " + word)
    # define count as a local variable to count the number of matching variables.
    count: int = 0
    # i think this could work through setting it equal to itself plus 1 for "then"
    # phrases after each match
    if word[0] == letter:
        # have to run through each character and use the index to assess it
        # make sure to fix this so it checks each value independently
        print(letter + " found at index 0")
        count = count + 1
        # not going to return anything here, just print the message
        # i was having issues b/c the instruction called the local var letter
        # while i called it character. gonna change it to letter
        # it worked but it kept searching if the character was more than 1. need to fix
    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1
    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1
    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1
    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    # now that i have made a way to add counts, i need a if/then to give different
    # responses based on count total
    if count == 0:
        print("No instances of " + letter + " found in " + word)
        # to fix the plurality i need a way to determine 1 vs 2
    elif count == 1:
        print(str(count) + " instance of " + letter + " found in " + word)
    else:
        print(str(count) + " instances of " + letter + " found in " + word)


# this makes the program runnable as a module and it makes it possible for other
# modules to import and reuse functions
if __name__ == "__main__":
    main()
