import numpy as np

doc_size = 1095
tfidf_matrix = np.zeros((1095, 12291))

# create a matrix recording normal vector of each doc by using the result of hw2
for i in range(1,1096):
    f = open("C:\\Users\\asdfg\\OneDrive\\桌面\\IRTM_hw2_result\\"+str(i)+".txt",'r') 
    # remove title
    next(f)
    next(f)
    vec = np.array([0.0]*12291)
    for x in f.readlines():
        temp = x.strip().split("\t")
        vec[int(temp[0])-1] = float(temp[1])   
        # temp[0] is term index
        # temp[1] is tfidf
    tfidf_matrix[i-1] = vec

# in order to create a matrix recording similarity
# existence = 1 means exist
def cos_sim(dx, dy):
    return (tfidf_matrix[dx]*tfidf_matrix[dy]).sum()

sim_matrix = np.zeros((doc_size, doc_size))
existence = np.zeros(doc_size)
for i in range(doc_size):
    for j in range(doc_size):
        sim_matrix[i][j] = cos_sim(i, j)
    existence[i] = 1


# HAC
# complete link
def find_max_sim(sim_matrix, existence):
    max_sim = -1
    index_i = -1
    index_j = -1
    for i in range(doc_size):
        if existence[i] == 1:
            for j in range(doc_size):
                if existence[j] == 1 and j != i:
                    if max_sim < sim_matrix[i][j]:
                        max_sim = sim_matrix[i][j]
                        index_i = i
                        index_j = j
    return max_sim, index_i, index_j


record = []
for x in range(doc_size - 1):
    max_sim, i, j = find_max_sim(sim_matrix, existence)
    record.append([i ,j])
    for k in range(doc_size):
        sim_matrix[i][k] = min(cos_sim(i, k), cos_sim(j, k))
        sim_matrix[k][i] = sim_matrix[i][k]
    existence[j] = 0
'''
    if x % 100 == 0:
        print(str(x*100//doc_size) + '%')
'''

def write_cluster(cluster_dict, K):
    with open(str(K) + '.txt', 'w') as cluster_file:
        for key, l in cluster_dict.items():
            doc_list = np.sort(l)
            for doc_id in doc_list:
                cluster_file.write(str(doc_id+1) + '\n')
            cluster_file.write('\n')

cluster_dict = {}
for i in range(doc_size):
    cluster_dict[str(i)] = [i]

for i, j in record:
    temp = cluster_dict[str(j)]
    cluster_dict.pop(str(j), None)
    cluster_dict[str(i)] += temp
    if len(cluster_dict) == 20:
        write_cluster(cluster_dict, 20)
    elif len(cluster_dict) == 13:
        write_cluster(cluster_dict, 13)
    elif len(cluster_dict) == 8:
        write_cluster(cluster_dict, 8)