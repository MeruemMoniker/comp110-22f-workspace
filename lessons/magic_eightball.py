"""Unsure..."""

from random import randint 

question: str = input("What is your yes/no question? ")
response: int = randint(0,21)
 
if response == 0:
    print("It is certain.")
elif response == 1:
    print("It is decidedly so.")
elif response == 2:
    print("Without a doubt.")
elif response == 3:
    print("Yes definetly.")
elif response == 4:
    print("Yes of course.")
elif response == 5:
    print("You may rely on it.")
elif response == 6:
    print("As I see it, yes")
elif response == 7:
    print("Most likely.")
elif response == 8:
    print("Outlook good.")
elif response == 9:
    print("Yes.")
elif response == 10:
    print("Signs point to yes.")
elif response == 11:
    print("Reply hazy, try again.")
elif response == 12:
    print("Ask again later.")
elif response == 13:
    print("Better not tell you now.")
elif response == 14:
    print("Cannot predict now.")
elif response == 15:
    print("Concentrate and ask again.")
elif response == 16:
    print("Don't count on it.")
elif response == 17:
    print("My reply is no.")
elif response == 18:
    print("My sources say no.")
elif response == 19:
    print("Outlook not so good.")
elif response == 20:
    print("Very doubtful.")
else:
    print("Mayhaps.")