"""Wordle"""

__author__ = "730391230"


def main(secret: str) -> None:
    """Contains the "game loop" of Wordle"""
    # main flow needs the following:
    # up to 6 turns
    # each turn, the player gets to input_guess of the same length
    # guess is compared with the secret and emojified boxes are output
    # if correct = game over
    # if incorrect, game loops back to the input
    # use input_guess to check the length of secret vs guess
    # could use input_guess as the guess parameter since it returns word
    turn: int = 1
    # counts the current turn
    state: int = 0
    # keeps track of game state. 0 = ongoing, 1 = end
    while state == 0:
        print(f"=== Turn {turn}/6 ===")
        # prints the turn number
        guess = input_guess(len(secret))
        # defines the guess as the output from input_guess
        print(emojified(guess, secret))
        # uses the guess and the secret in emojify
        if guess == secret:
            # check if the guess is the same as secret, then raises the state to 1 to
            # end the game
            state = state + 1
            print(f"You won in {turn}/6 turns!")
        elif turn == 6:
            # ends the game if turn = 6
            state = state + 1
            print("X/6 - Sorry, try again tomorrow!")
        else:
            # increases turn number and returns back to the guess input
            turn = turn + 1


def input_guess(s_word_len: int) -> str:
    """Checks if the inputted word matches the secret word length, and prompts
    otherwise"""
    # enter until a correct length guess is entered, that is specified by the parameter?
    # parameter holds the secret word length
    word: str = input(f"Enter a {s_word_len} character word:")
    while len(word) != s_word_len:
        word = input(f"That wasn't {s_word_len} chars! Try again:")
    return word


def contains_char(searched_str: str, target_char: str) -> bool:
    """tests each index of the first parameter str, checking if it matches the second
    parameter"""
    # bool since it returns true or false
    # has to work with words of any length so it will require variables
    assert len(target_char) == 1
    # expected that the caller doesnt mess this up
    index: int = 0
    while len(searched_str) > index:
        if searched_str[index] == target_char:
            # it stops now so return true
            return True
        index = index + 1
    return False


def emojified(guess: str, secret: str) -> str:
    """This compares the guess with the secret word, and gives back the emojis in a way
    expected of wordle"""
    # added this assertion since i can expect anyone to provide strings of equal length
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    # emoji definitions: white for none, yellow for wrong place, green for correct
    # build up a string using emoji concatenations for each index, then return it
    index: int = 0
    emoji_str: str = ""
    # loop tests each index of secret words, while using contains_char
    while index < len(guess):
        if guess[index] == secret[index]:
            # need a way to keep track of matches to add the string together
            emoji_str = emoji_str + GREEN_BOX
        # use the contains_char to check if the secret word has the target char
        # if there is a match, the yellow gets added to the emoji_str. if not, white
        elif contains_char(secret, guess[index]) is True:
            emoji_str = emoji_str + YELLOW_BOX
        else:
            emoji_str = emoji_str + WHITE_BOX
        index = index + 1
    return emoji_str


if __name__ == "__main__":
    main(secret="codes")
    # lets python run this as module, and lets other modules import these functions
