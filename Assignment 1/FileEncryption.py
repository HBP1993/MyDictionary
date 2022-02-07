def main():
    codes =  {'A':'%', 'a':'9', 'B':'@', 'b':'#', 'C':'1', 'c':'2', 'D':'3', 'd':'4', \
    'E':'5', 'e':'6', 'F':'7', 'f':'8', 'G':'0', 'g':'}', 'H':'{', 'h':']', 'I':'[', 'i':',', \
        'J':'.', 'j':'>', 'K':'<', 'k':'/', 'L':'0', 'l':'\-', 'M':'\"', 'm':':', 'N':';', \
         'n':'+', 'O':'$', 'o':'-', 'Q':'$', 'q':'%', 'R':'^', 'r':'&', 'S':'*', \
         's':'(','T':')', 't':'~', 'U':'`', 'u':'5', 'V':'\\', 'v':'+', 'W':'=', 'w':'7', \
         'X':'~', 'x':')', 'Y':'2', 'y':'*', 'Z':']', 'z':'8'}
    
    encyrption(codes)

def encyrption(codes):
    file = open('info_security.txt', 'r')
    read_file = file.read()
    encrypt_file = open('newfile.txt','w')
    for character in read_file:
        if character in codes:
            encrypt_file.write(codes[character])
        else:
            encrypt_file.write(character)
    encrypt_file.close()

main()
        