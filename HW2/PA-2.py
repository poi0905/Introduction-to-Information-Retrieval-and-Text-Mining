from nltk.stem import PorterStemmer
import numpy as np
import math

# load the txt
txt = []
for i in range(1, 1096):
    f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM\\IRTM\\"+str(i)+".txt", "r")
    words = f.read()
    txt.append(words)

# split the text roughly
token = []
for i in range(1095):
    a = txt[i].split(' ')
    token.append(a)

# Lowercasing everything
for i in range(len(token)):
    token[i] = [j.lower() for j in token[i]]

# remove "\n"
for i in range(len(token)):
    for j in range(len(token[i])):
        if "\n" in token[i][j]:
            token[i][j] = token[i][j][1:]

# remove punctuation marks & ""(produce after strip)
for i in range(len(token)):
    token[i] = [j.strip('><1234567890!@#$%^&*()-_=+[]\|/.,?:;"{}`~') for j in token[i]]
    token[i] = [j.strip("><1234567890!@#$%^&*()-_=+[]\|/.,?:;'{}`~") for j in token[i]]
    while "" in token[i]:
        token[i].remove("")

# "'" from abbreviation
for i in range(len(token)):
    for j in range(len(token[i])):
        if "'" in token[i][j] and token[i][j][-1] == "s":   # eg: he's
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-1] == "m":   # eg: i'm
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-2] == "r" and token[i][j][-1] == "e":    # eg: they're
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-2] == "l" and token[i][j][-1] == "l":    # eg: i'll
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-2] == "v" and token[i][j][-1] == "e":    # eg: could've
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-1] == "d":   # eg: she'd
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-1] == "t":   # eg: don't
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]

# Create a stop words list and eliminate them
stopwordlist = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "doesn", "should", "now"]
for i in range(len(token)):
    token[i] = [a for a in token[i] if a not in stopwordlist]

# Stemming using Porter’s algorithm.
ps = PorterStemmer()
for i in range(len(token)):
    for j in range(len(token[i])):
        token[i][j] = ps.stem(token[i][j])

# Create an alphabet list in case the single alphabet exists
stopwordlist = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
for i in range(len(token)):
    token[i] = [a for a in token[i] if a not in stopwordlist]


# Remove duplicates to get df
def remove_duplicates(x):
    return sorted(set(x), key=x.index)

df_token = token

for i in range(len(df_token)):
    df_token[i] = remove_duplicates(df_token[i])

# Put all tokens into one list
totaltoken = []
for i in range(len(df_token)):
    totaltoken.append(df_token[i])

# Build a dict
df_dict = {}
for i in range(len(totaltoken)):
    for key in token[i]:
        df_dict[key] = df_dict.get(key, 0) + 1
'''
# Output a "dictionary.txt" file(sorted)
t_index = 1
with open("dictionary.txt", "w") as output:
    output.write("t_index"+"\t"+"term"+"\t"+"df"+"\n")
    for key in sorted(df_dict):
        string = str(t_index)+"\t"+str(key)+"\t"+str(df_dict[key])
        output.write(string+"\n")
        t_index += 1
'''
# Calculate each term's idf
for key in df_dict.keys():
    df_dict[key] = math.log10(1095/df_dict[key])

# Transfer each document into a tf-idf unit vector
for i in range(1095):
    t_index = 0
    t_index_list = []
    tfidf_list = []
    n = 0   # store the number of terms(required)
    length = 0    # for normalizing

    for key in sorted(df_dict.keys()):
        t_index += 1
        if key in token[i]:
            t_index_list.append(t_index)
            n += 1
            tf = token[i].count(key)
            tfidf = tf * df_dict[key]
            tfidf_list.append(tfidf)
            length += (tfidf)**2

    tfidf_list = [x / math.sqrt(length) for x in tfidf_list]
'''
    with open(str(i+1)+".txt", "w") as output:
        output.write(str(n)+"\n")
        output.write("t_index"+"\t"+"tf-idf"+"\n")
        for i in range(len(tfidf_list)):
            output.write(str(t_index_list[i])+"\t"+str(tfidf_list[i])+"\n")
'''

# Cosine similarity
def cosine(dx, dy):
    f1 = open(dx, "r")
    f2 = open(dy, "r")

    # there are 13,543 terms in the dict
    vec_x = np.zeros(13543)
    vec_y = np.zeros(13543)

    # first and second rows are useless.
    # temp[0] is index, temp[1] is tf-idf
    for x in f1.readlines()[2:]:
        temp = x.strip().split("\t")
        vec_x[int(temp[0])-1] = float(temp[1])

    for x in f2.readlines()[2:]:
        temp = x.strip().split("\t")
        vec_y[int(temp[0])-1] = float(temp[1])

    sim = np.inner(vec_x, vec_y)

    return(sim)

document1 = "C:\\Users\\asdfg\\OneDrive - g.ntu.edu.tw\\NTU\\109-1\\109-1IRTM\\Introduction-to-Information-Retrieval-and-Text-Mining\\HW2\\1.txt"
document2 = "C:\\Users\\asdfg\\OneDrive - g.ntu.edu.tw\\NTU\\109-1\\109-1IRTM\\Introduction-to-Information-Retrieval-and-Text-Mining\\HW2\\2.txt"
sim = cosine(document1, document2)
print("The cosine similarity of document1 and document2 is: " + str(sim))
