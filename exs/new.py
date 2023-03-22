"""EX02 - Glarble - World world world world World."""

secret: str = "pythons"
guess: str = input(f"What is your {len(secret)}-letter guess? ")

while len(guess) != len(secret):
    guess: str = (input(f"That was not {len(secret)} letters! Try again: "))

white: str = "\U00002B1C"
green: str = "\U0001F7E9"
yellow: str = "\U0001F7E8"
i: int = 0
emoji: str = ""
checker: str = secret[i]
untrue: bool = False 
alt: int = 0

while i < len(secret):
    if guess[i] == secret[i]:
        emoji = emoji + green
    else:
        match: bool = False
        t: int = 0
        while match == False and t < len(secret):
            if secret[t] == guess[i]:
                match = True
            else:
                t += 1
        if match == True:
            emoji += yellow
        else:
            emoji+= white
    i = i + 1
print(emoji)

if guess == secret:
    print("Woo! You got it!")
else:
    if len(guess) == len(secret):
        print("Not quite. Play again soon!") 
