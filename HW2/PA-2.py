from nltk.stem import PorterStemmer

# load the txt
txt = []
for i in range(1,1096):
    f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM\\IRTM\\"+str(i)+".txt", "r")
    words = f.read()
    txt.append(words)

print(txt[0])