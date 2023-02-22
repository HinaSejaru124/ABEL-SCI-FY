import string
# TRANSLATION_TABLE = str.maketrans(
#     string.ascii_uppercase + string.ascii_lowercase,
#     string.ascii_uppercase[-1:] + string.ascii_uppercase[:-1] +
#     string.ascii_lowercase[-1:] + string.ascii_lowercase[:-1]
# )
encode = ""


def rot13(s):
    """Return the rot-13 encoding of s."""
    global encode
    for i in range(len(s)):
        encode += s[i].translate(str.maketrans(
            string.ascii_uppercase + string.ascii_lowercase,
            string.ascii_uppercase[(i+1) % 26:] + string.ascii_uppercase[:(i+1) % 26] +
            string.ascii_lowercase[(i+1) % 26:] +
            string.ascii_lowercase[:(i+1) % 26]
        ))
    encoder = encode
    encode = ""
    return encoder


if __name__ == "__main__":
    """rot-13 encode the input files, or stdin if no files are provided."""
    ans = input("Will you enter text from the console or from a file? (Enter 'c' for console and 'f' for file)\n")
    while ans != 'c' and ans != 'f':
        ans = input("There is no option for this. Enter 'c' or 'f':\n")
    if ans == 'c':
        import fileinput
        print("Then enter your text already\n")
        for line in fileinput.input():
            if line == "":
                exit()
            else:
                print(rot13(line), end="")
    else:
        textName = input("Then enter the file's name\n")
        f = open(textName, 'r')
        for line in f.readlines():
            if line == "":
                exit()
            else:
                print(rot13(line), end="")
        f.close()
