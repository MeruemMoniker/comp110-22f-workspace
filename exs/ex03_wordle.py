"""OKAY"""
__author__: str(123456789)

def main() -> None:
    """The entrypoint of the program and main game loop"""
    real_secret: str = "mines"
    turn: int = 1
    while turn < 7:
        print(f"=== Turn {turn}/6 ===")
        xx: str = input(f"Enter a {len(real_secret)} character word: ")
        w: str = input_guess(xx)
        print(emojified(w, real_secret))
        if xx == real_secret:
            return print(f"You won in {turn}/6 tries!")
        else:
            turn +=1
    return print("X/6 - Sorry, try again tomomrrow!")

def contains_char(guess: str = (""), i: str = "") -> bool:
    """Define characaters contained in guess word"""
    assert len(i) == 1
    contains_char: bool = False
    t: int = 0
    while contains_char == False and t < len(guess):
        if i == guess[t]:
            contains_char = True
        else:
            t += 1
    if contains_char == True:
        return True
    else:
        return False

def emojified(guessi: str = "", secret: str = "") -> str:
    """Emoji translator"""
    assert len(guessi) == len(secret)
    emoji: str = ""
    white: str = "\U00002B1C"
    green: str = "\U0001F7E9"
    yellow: str = "\U0001F7E8"
    ii: int = 0
    while ii < len(secret):
        if guessi[ii] == secret[ii]:
            emoji += green
        else:
            x: bool = contains_char(secret, guessi[ii])
            if x == True:
                emoji += yellow
            else:
                emoji += white
        ii += 1
    return emoji

def input_guess(char_length: int = "") -> str:
    """Input clearance"""
    real_secret: str = "mines"
    if len(char_length) == len(real_secret):
        return char_length
    else:        
        while len(char_length) != len(real_secret):
            char_length: str = input(f"That was not {len(real_secret)} letters! Try again: ")
        return char_length

if __name__ == "__main__":
    main()