from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
import math
import re


# Tokenize
def tokenize(txt):
    token = []
    a = re.split("/|,|'|`|-| |\n", txt)
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

    # Use stop words list in order to eliminate them
    stopwordlist = stopwords.words('english')
    for i in range(len(token)):
        token[i] = [a for a in token[i] if a not in stopwordlist]

    # Stemming using Porter’s algorithm.
    ps = PorterStemmer()
    for i in range(len(token)):
        for j in range(len(token[i])):
            token[i][j] = ps.stem(token[i][j])

    return token


# Load training data
train = []  # 13*15
training_doc_id = []
f = open("C:\\Users\\asdfg\\OneDrive - g.ntu.edu.tw\\NTU\\109-1\\109-1IRTM\\Introduction-to-Information-Retrieval-and-Text-Mining\\HW3\\class.txt", "r")
words = f.read().splitlines()
for i in range(13):
    temp = words[i].strip().split(" ")
    temp.pop(0)
    train.append(temp)
for c in train:
    for docID in c:
        training_doc_id.append(int(docID))

# Store info of training data
class_doc_token = []
terms = {}
for c in train:
    doc_token = []
    for docID in c:
        # Load the text of training doc
        f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM\\IRTM\\"+str(docID)+".txt", "r")
        text = f.read()
        # Tokenize the training doc
        temp = tokenize(text)  # 2D-list: [['a','b',...]]
        token = []
        for j in temp[0]:
            token.append(j)    # 1D-list: ['a','b',...]
        # create a dict for each term
        for k in token:
            if k not in terms.keys():
                terms[k] = []
        doc_token.append(token)
    class_doc_token.append(doc_token)

# LLR
for term in terms.keys():
    for classnum1 in range(len(class_doc_token)):
        n11 = 0  # on topic & present
        n10 = 0  # on topic & absent
        n01 = 0  # off topic & present
        n00 = 0  # off topic & absent
        for classnum2 in range(len(class_doc_token)):
            # on topic
            if classnum2 == classnum1:
                for token in class_doc_token[classnum1]:
                    if term in token:   # present
                        n11 += 1
                    else:   # absent
                        n10 += 1
            # off topic
            else:
                for token in class_doc_token[classnum2]:
                    if term in token:   # present
                        n01 += 1
                    else:   # absent
                        n00 += 1

        n = n11+n10+n01+n00
        # hypothesis 1(the prob. of the occurence of the term & the class is independant)
        pt = (n11+n01)/n    # on/off topic & present
        # hypothesis 2(the prob. of the occurence of the term & the class is dependant)
        p1 = n11/(n11+n10)  # on topic & present
        p2 = n01/(n01+n00)  # off topic & absent
        LH1 = (pt**n11)*((1-pt)**n10)*(pt**n01)*((1-pt)**n00)
        LH2 = (p1**n11)*((1-p1)**n10)*(p2**n01)*((1-p2)**n00)
        LLR = (-2)*math.log10(LH1/LH2)
        terms[term].append(LLR)

# build the new dict to store LLR of each term
# use average LLR to select feature term
terms_scored = {}
for term in terms.keys():
    terms_scored[term] = sum(terms[term])/len(terms[term])

count = 0
feature_term = {}
terms_scored = sorted(terms_scored, key=terms_scored.get, reverse=True)  # from big to small
for term in terms_scored:
    if count < 250:  # tested
        count += 1
        feature_term[term] = []

# store only feature term
for i in range(len(class_doc_token)):
    for j in range(len(class_doc_token[i])):
        for k in range(len(class_doc_token[i][j])):
            if class_doc_token[i][j][k] not in feature_term.keys():
                class_doc_token[i][j][k] = ""
        while "" in class_doc_token[i][j]:
            class_doc_token[i][j].remove("")

# Multi-Nominal NB Classification - Training Phase
voc = 250  # extract vocabulary
prior = 1/13
for term in feature_term.keys():
    for c in class_doc_token:
        alldoc_num = 0
        term_appear = 0
        for doc in c:
            alldoc_num += len(doc)   # concatenate text of all docs in class
            for token in doc:
                if term == token:
                    term_appear += 1
        condprob = (term_appear+1)/(alldoc_num+voc)
        feature_term[term].append(condprob)

# Multi-Nominal NB Classification - Training Phase
ans = []
for docID in range(1, 1096):
    if docID not in training_doc_id:
        c_map = [math.log10(prior)]*13
        f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM\\IRTM\\"+str(docID)+".txt", "r")
        text = f.read()
        temp = tokenize(text)
        token = []
        for i in temp[0]:
            token.append(i)
        for term in token:
            if term in feature_term.keys():
                for x in range(13):
                    c_map[x] += math.log10(feature_term[term][x])
        ans.append(docID)
        ans.append(c_map.index(max(c_map))+1)

# Output
answer = open("B07302230_250", "w")
for i in range(0, len(ans), 2):
    answer.write(str(ans[i]))
    answer.write("\t")
    answer.write(str(ans[i+1]))
    answer.write("\n")
