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
    token[i] = [j.strip(".%@(),?:'!+=`-_") for j in token[i]]
    token[i] = [j.strip('"') for j in token[i]]

# remove "\n" and "'" from abbreviation
for i in range(len(token)):
    for j in range(len(token[i])):
        if "\n" in token[i][j]:
            token[i][j] = token[i][j][1:]
        if "'" in token[i][j] and token[i][j][-1] == "s":
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-1] == "m":
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-2] == "r" and token[i][j][-1] == "e":
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]
        if "'" in token[i][j] and token[i][j][-1] == "t":
            p = token[i][j].find("'")
            token[i][j] = token[i][j][:p]

# Lowercasing everything
for i in range(len(token)):
    token[i] = [j.lower() for j in token[i]]

# Stemming using Porter’s algorithm.
ps = PorterStemmer()
for i in range(len(token)):
    for j in range(len(token[i])):
        token[i][j] = ps.stem(token[i][j])

# Create a stop words list and eliminate them
stopwordlist = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "doesn", "should", "now",""]
for i in range(len(token)):
    for j in stopwordlist:
        for k in token[i]:
            if k == j:
                token[i].remove(j)

# Remove duplicates to get df
df_token = token
def remove_duplicates(x):
    return sorted(set(x), key = x.index)

for i in range(len(df_token)):
    df_token[i] = remove_duplicates(df_token[i])

# Put all tokens into one list
totaltoken = []
for i in range(len(df_token)):
    totaltoken.append(df_token[i])

# build a dict and sort it
df_dict = {}
for i in range(len(totaltoken)):
    for key in token[i]:
        df_dict[key] = df_dict.get(key, 0) + 1

df_dict_items = df_dict.items()
sorted_items = sorted(df_dict_items)
df_dict = dict(sorted_items)

with open("result.txt", "w") as output:
    output.write(str(df_dict))

