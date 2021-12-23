filename = 'poll.txt'
poll = []

while True:
    print("\nWhy do you like programming?")
    answer = input("(Type 'q' in order to stop): ")
    if answer == 'q':
        break
    poll.append(answer)

with open(filename, 'w') as file_object:
    file_object.write("REASONS WHY PEOPLE LIKE PROGRAMMING:\n")
    if poll != []:
        for response in poll:
            file_object.write(f"{response}\n")
    else:
        file_object.write("Nobody took the poll!\n")