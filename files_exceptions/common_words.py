filename = 'pride_and_prejudice.txt'
word = 'the'

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    matches = contents.lower().count(word)
    print(f"The word '{word}' appears approximately {matches} times in {filename}.")