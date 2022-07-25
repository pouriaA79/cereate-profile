


import numpy as np
from itertools import combinations

number_of_sequence = int(input())
lisst = []

MSA = []
strr = ''
for i in range(number_of_sequence + 1):
    STR = input()
    strr += STR
    if i != number_of_sequence:
        MSA.append(STR)
    else:
        question = STR
lenn = len(MSA[0])
for i in range(lenn):
    lisst.append(i)
score_matrix = np.zeros((len(set(strr)), len(MSA[0])))
unique_charachters = list(set(strr))
words_dict = {}
for w in unique_charachters:
    words_dict[w] = 0
pseudocount = 2
for j in range(len(MSA[0])):
    for i in range(len(set(strr))):
        count = 0
        for t in range(number_of_sequence):
            if unique_charachters[i] == MSA[t][j]:
                count += 1
                words_dict[unique_charachters[i]] += 1
        score_matrix[i][j] = ((count + pseudocount) / (number_of_sequence + (len(unique_charachters) * pseudocount)))

for i in range(len(unique_charachters)):
    score_matrix[i][:] = score_matrix[i][:] / (sum(score_matrix[i][:]) / (len(MSA[0])))
score_matrix = np.log2(score_matrix)
best_score = -100
seen = []

for i in range(lenn):
    if i == 0:
        continue
    number_gap = lenn - i - 1
    comb = combinations(lisst, i)
    for j in range(len(question) - i ):
        if question[j: j + i + 1] in seen:
            continue
        else:
            seen.append(question[j: j + i + 1])
            strings = []
            for t in range(j, j + i + 1):
                strings.append(question[t])
            # print("********")
            # print(i)
            # print(strings)
            comb = combinations(lisst, i+1)

            for x in comb:
                score= 0
                to_find = ['-' for _ in range(lenn)]
                for t in range(len(strings)):
                    to_find[x[t]] = strings[t]
                # print(to_find)

                for t in range(len(to_find)):
                    score += score_matrix[unique_charachters.index(to_find[t])][t]
                if score > best_score:
                    best_score = score
                    best_match = "".join(to_find)

print(best_match)


