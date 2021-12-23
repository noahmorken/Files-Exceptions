filename = 'guest.txt'
guests = []

while True:
    print("\nPlease type the name of every guest attending.")
    guest = input("(Type 'q' in order to stop): ")
    if guest == 'q':
        break
    guests.append(guest)

with open(filename, 'w') as file_object:
    file_object.write("GUEST LIST:\n")
    if guests != []:
        for guest in guests:
            file_object.write(f"{guest.title()}\n")
    else:
        file_object.write("There are no guests.\n")