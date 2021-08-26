import random

names_string = input("Give me everybody's names according to the given format. (e.g.-name, name, name) \n")
names = names_string.split(", ") # Split string method

# random_num = random.randint(0,len(names)-1)
# random_person = names[random_num]
# print(random_person +", is the lucky person to pay the bill.")

print(names[random.randint(0,len(names)-1)]+", is the lucky person to pay the bill.")