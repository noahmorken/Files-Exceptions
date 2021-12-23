filename = 'dragon_quest_xi.txt'

# with open('dragon_quest_xi.txt') as file_object:
#     contents = file_object.read()
# print(contents)

print("\n")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

    
print("\n")
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    new_line = line.replace('Hero', 'Luminary')
    print(new_line.rstrip())