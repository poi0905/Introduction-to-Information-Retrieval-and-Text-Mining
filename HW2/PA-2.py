from nltk.stem import PorterStemmer

# load the txt
txt = []
for i in range(1,1096):
    f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM\\IRTM\\"+str(i)+".txt", "r")
    words = f.read()
    txt.append(words)

# split the text roughly
token = []
for i in range(1095):
    a = txt[i].split(' ')
    token.append(a)

# remove punctuation marks
for i in range(len(token)):
    token[i] = [j.strip(".,?:'!`_") for j in token[i]]

# remove "\n" & "'" from abbreviation
for i in range(len(token)):
    for j in range(len(token[i])):
        if "\n" in token[i][j]:
            token[i][j] = token[i][j][1:]
        if "'" in token[i][j]:
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p] + token[i][j][p+1]

# Lowercasing everything
for i in range(len(token)):
    token[i] = [j.lower() for j in token[i]]
