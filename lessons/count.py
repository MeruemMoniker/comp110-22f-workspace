"""Learning how to use the count function"""


message = "hellohooohhooo"
print(message.count("h"), "instance(s) of h")

print(message.find("h",4,4))
print(len(message))

name: str = input("Enter a 5-Character word: ")
user_name: str = input("Enter a single character: ")
print("Searching for " + user_name + " in " + name)
inda: str = name.find(user_name)
print(inda)
print(len("codes"))
