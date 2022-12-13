def intransitive(lists):
    lst = []
    for list in lists:
        for element in list:
            lst.append(element)
    p1, p2, p3 = 0, 0, 0
    for i in range(6): #izračun števila kombinacij, kjer velja A>B, B>C in C>A 
        for j in range(6): 
            if lst[i] > lst[6+j]:
                p1 += 1
            if lst[6+i] > lst[12 + j]:
                p2 += 1
            if lst[12 + i] > lst[j]:
                p3 += 1
    return min(p1, p2, p3)/36 #min treh verjetnosti, da verjetnost, da med danimi tremi kockami velja tranzitivnost 

testni_primer = [[2, 2, 4, 4, 9, 9], [1, 1, 6, 6, 8, 8], [3, 3, 5, 5, 7, 7]]

import random

def generator_list(m):
    lst = []
    random_num = None
    while len(lst) < 6:
        random_num = random.randint(1, m)
        if random_num not in lst:
            lst.append(random_num)
        else:
            continue
    return lst
        
def glavna(n, m): 
    lst = []
    while len(lst) < m:
        first = generator_list(n)
        second = generator_list(n)
        third = generator_list(n)
        lst.append((intransitive(([first, second, third])), [first, second, third]))
    maxp = 0
    for i in range(len(lst)):
        maxp = max(maxp, lst[i][0])
        lst_with_max = lst[i][1]
    return maxp, lst_with_max

for i in range(100):
   print(f"{int(list(zip(glavna(100000000, 10000)))[0][0] * 36)}" + "/36")
