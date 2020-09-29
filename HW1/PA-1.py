'''
And Yugoslav authorities are planning the arrest of eleven coal miners 
and two opposition politicians on suspicion of sabotage, that's in 
connection with strike action against President Slobodan Milosevic. 
You are listening to BBC news for The World.
'''
from nltk.stem import PorterStemmer

# Tokenization
token = []
for i in range(4):
    a = input().split(' ')
    for j in range(len(a)):
        token.append(a[j])

for i in range(len(token)):
    try:
        token.remove('')
    except:
        break

# remove duplicates
def my_function(x):
  return list(dict.fromkeys(x))

token = my_function(token)

# remove commas and dots
token = [i.strip('.,') for i in token]

for i in range(len(token)):
    if "'" in token[i]:
        p = token[i].find("'")
        token[i] = token[i][:p] + token[i][p+1]

# Lowercasing everything
token = [i.lower() for i in token]

# Stemming using Porter’s algorithm.
ps = PorterStemmer()
pstoken = []

for w in token:
    pstoken.append(ps.stem(w))

# Create a stop words list and eliminate them
stopwordlist = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
for i in range(len(stopwordlist)):
    for j in range(len(pstoken)):
        try:
            if stopwordlist[i] == pstoken[j]:
                pstoken.remove(pstoken[j])
        except:
            continue

with open("result.txt", "w") as output:
    output.write(str(pstoken))