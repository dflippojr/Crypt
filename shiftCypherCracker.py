file = open("cypherText.txt", "r")
cypherText = ""
# build string from file
for line in file:
    cypherText += line
file.close()
# make a single line and remove spaces
cypherText = cypherText.replace("\n", "")
cypherText = cypherText.replace(" ", "")
# define the alphabet
alph = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
        'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]
# shift 25 times
for i in range(1, 26):
    plainText = ""
    for j in range(len(cypherText)):
        if (cypherText[j] != ' '):
            x = alph.index(cypherText[j])
            plainText += alph[(x+i) % 26]
        else:
            plainText += ' '
    print(str(i) + " " + plainText + "\n")