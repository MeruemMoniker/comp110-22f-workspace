"""EX02 - Glarble - World world world world World."""

secret: str = "python"
guess: str = input("What is your 6-letter guess? ")

while len(guess) != len(secret):
    guess: str = (input("That was not 6 letters! Try again: "))

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"
i: int = 0
emoji: str = ""
checker: str = secret[i]
untrue: bool = False 
alt: int = 0

while i < len(secret):
    if secret[i] == guess[i]:
        emoji = emoji + green
    else:
        if secret[i] != guess[i]:
            while untrue is not True and alt < len(secret):
                if secret[alt] == guess[i]:
                    untrue: True
                    emoji = emoji + white
                else:
                    emoji = emoji + yellow
                alt = alt + 1        
    i = i + 1

print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    if len(guess) == len(secret):
        print("Not quite. Play again soon!") 
