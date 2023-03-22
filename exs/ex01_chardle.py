"""EX01 - Chardle - A cute stp toward World."""

name: str = input("Enter a 5-Character word: ")
if len(name) != int(5):
    print("Error: Word must contain 5 characters")
    exit()
user_name: str = input("Enter a single character: ")
if len(user_name) != int(1):
    print("Error: Character must be a single character.")
    exit()
print("Searching for " + user_name + " in " + name)
finda: str = name.find(user_name)
findb: str = name.find(user_name,1)
findc: str = name.find(user_name,2)
findd: str = name.find(user_name,3)
finde: str = name.find(user_name,4)
if finda == int(0):
    print(user_name + " found at index " + str(finda))
if findb == int(1):
    print(user_name + " found at index " + str(findb))
if findc == int(2):
    print(user_name + " found at index " + str(findc))
if findd == int(3):
    print(user_name + " found at index " + str(findd))
if finde == int(4):
    print(user_name + " found at index " + str(finde))
print(name.count(user_name), "instance(s) of " + user_name + " found in " + name)
