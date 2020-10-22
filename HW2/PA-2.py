from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import numpy as np
import math
import re


# Tokenize
def tokenize(txt):
    token = []
    for i in range(1095):
        a = re.split("/|,|'|`|-| |\n", txt[i])
        token.append(a)

    # Lowercasing & remove punctuation marks & "." & ""(produce after strip)
    for i in range(len(token)):
        token[i] = [j.lower() for j in token[i]]
        token[i] = [j.strip('><1234567890!@#$%^&*()_=+[]\|?:;"{}~.') for j in token[i]]
        for j in range(len(token[i])):
            if "." in token[i][j]:
                token[i][j] = ""
        while "" in token[i]:
            token[i].remove("")

    # Create a stop words list in order to eliminate them
    stopwordlist = stopwords.words('english')
    for i in range(len(token)):
        token[i] = [a for a in token[i] if a not in stopwordlist]

    # Stemming using Porter’s algorithm.
    ps = PorterStemmer()
    for i in range(len(token)):
        for j in range(len(token[i])):
            token[i][j] = ps.stem(token[i][j])

    return token


def produce_dictionary(list):
    # Remove duplicates to get df
    def remove_duplicates(x):
        return sorted(set(x), key=x.index)

    for i in range(len(df_token)):
        df_token[i] = remove_duplicates(df_token[i])

    # Put all tokens into one list
    totaltoken = []
    for i in range(len(df_token)):
        totaltoken.append(df_token[i])

    # Build a dict
    df_dict = {}
    for i in range(len(totaltoken)):
        for key in df_token[i]:
            df_dict[key] = df_dict.get(key, 0) + 1

    return df_dict


# Cosine similarity
def cosine(dx, dy):
    f1 = open(dx, "r")
    f2 = open(dy, "r")

    # there are 12291 terms in the dict
    vec_x = np.zeros(12291)
    vec_y = np.zeros(12291)

    # first and second rows are useless.
    # temp[0] is index, temp[1] is tf-idf
    for x in f1.readlines()[2:]:
        temp = x.strip().split("\t")
        vec_x[int(temp[0])-1] = float(temp[1])
    for x in f2.readlines()[2:]:
        temp = x.strip().split("\t")
        vec_y[int(temp[0])-1] = float(temp[1])

    sim = np.dot(vec_x, vec_y)

    return sim

# Load the txt
txt = []
for i in range(1, 1096):
    f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM\\IRTM\\"+str(i)+".txt", "r")
    words = f.read()
    txt.append(words)

token = tokenize(txt)
df_token = tokenize(txt)
df_dict = produce_dictionary(df_token)

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

    for key in sorted(df_dict.keys()):
        t_index += 1
        if key in token[i]:
            t_index_list.append(t_index)
            n += 1
            tf = token[i].count(key)
            tfidf = tf * df_dict[key]
            tfidf_list.append(tfidf)

    tfidf_list = np.array(tfidf_list)
    norm = np.linalg.norm(tfidf_list)
    tfidf_list = tfidf_list / norm
'''
    with open(str(i+1)+".txt", "w") as output:
        output.write(str(n)+"\n")
        output.write("t_index"+"\t"+"tf-idf"+"\n")
        for j in range(len(tfidf_list)):
            output.write(str(t_index_list[j])+"\t"+str(tfidf_list[j])+"\n")
'''
document1 = "C:\\Users\\asdfg\\OneDrive - g.ntu.edu.tw\\NTU\\109-1\\109-1IRTM\\Introduction-to-Information-Retrieval-and-Text-Mining\\HW2\\1.txt"
document2 = "C:\\Users\\asdfg\\OneDrive - g.ntu.edu.tw\\NTU\\109-1\\109-1IRTM\\Introduction-to-Information-Retrieval-and-Text-Mining\\HW2\\2.txt"

sim = cosine(document1, document2)
print("The cosine similarity of document1 and document2 is: " + str(sim))
