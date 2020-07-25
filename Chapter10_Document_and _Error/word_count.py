"""Use Many Files"""

def count_words(filename):
    """计算一个文件大致包含多少个单词"""
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        #msg = f"Sorry, the file {filename} does not exist."
        #print(msg)
        pass
    else:
        # Count approximate number of words in the file
        words = contents.split()
        num_words = len(words)
        msg = f"The file {filename} has about {num_words} words."
        print(msg)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dict.txt', 'little_women.txt']
for filename in filenames:
    count_words(filename)