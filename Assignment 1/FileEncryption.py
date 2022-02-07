# define main function
def main():
    codes = {
        "A": "%",
        "a": "9",
        "B": "@",
        "b": "#",
        "C": '"',
        "c": "4",
        "D": "6",
        "d": "8",
        "E": "0",
        "e": "3",
        "F": ")",
        "f": "4",
        "G": "5",
        "g": "[",
        "H": "]",
        "h": "{",
        "I": "}",
        "i": ",",
        "J": "*",
        "j": "///",
        "K": ">>",
        "k": "))",
        "L": "5",
        "l": ";",
        "M": "//",
        "m": "1",
        "N": "??",
        "n": "--",
        "O": "++",
        "o": "))",
        "Q": "(((",
        "q": "%/",
        "R": ",<",
        "r": ".>",
        "S": "{{",
        "s": "}}",
        "T": ")",
        "t": "`",
        "U": "~",
        "u": "0",
        "V": "||",
        "v": "+",
        "W": "&",
        "w": "7",
        "X": "|",
        "x": "2",
        "Y": "1",
        "y": "^",
        "Z": "9",
        "z": "4",
    }

    encryption(codes)


# define encryption
def encryption(codes):
    # open and read info_security file
    file = open("info_security.txt", "r")
    read_file = file.read()
    # create file to decrypted message
    encrypt_file = open("newfile.txt", "w")

    # Read each character in file
    for character in read_file:
        if character in codes:
            encrypt_file.write(codes[character])
        else:
            encrypt_file.write(character)
    # close the file
    encrypt_file.close()


# call the main function
main()
