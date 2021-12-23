def list_types(filename):
    """List the types of cats and dogs in two files.""" 
    try:
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # print(f"Sorry, the file {filename} does not exist.")
        pass
    else:
        # Prints out the text in the files.
        print(f"Types of animal in {filename}:")
        print(f"{contents}\n")       

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    list_types(filename)