"""Deal with Errores(FileNotFoundError)"""

filename = 'alice.txt'

try:
    with open(filename) as f_obj:
        contents = f_obj.read()
except FileNotFoundError:
    msg = f"Sorry, the file {filename} does not exist."
    print(msg)
else:
    # Count approximate number of words in the file
    words = contents.split()
    num_words = len(words)
    msg = f"The file {filename} has about {num_words} words."
    print(msg)