def intransitive(lists, sides, num_of_dice):
    lst = []
    for list in lists:
        for element in list:
            lst.append(element)
    prob = []
    for i in range(num_of_dice):#narejen začetni verjetnostni vektor, kjer je komponent toliko, kolikor kock primerjaš
        prob.append(0)
    for i in range(sides): #izračun števila kombinacij, kjer velja A>B, B>C in C>A (oziroma A>B, B>C, C>D in D>A)
        for j in range(sides):
            if num_of_dice == 4: 
                if lst[i] > lst[sides+j]:
                    prob[0] += 1
                if lst[sides+i] > lst[sides*2 + j]:
                    prob[1] += 1
                if lst[sides*2 + i] > lst[sides*3 + j]:
                    prob[2] += 1
                if lst[sides*3 + i] > lst[j]:
                    prob[3] += 1
            elif num_of_dice == 3:
                if lst[i] > lst[sides+j]:
                    prob[0] += 1
                if lst[sides+i] > lst[sides*2 + j]:
                    prob[1] += 1
                if lst[sides*2 + i] > lst[j]:
                    prob[2] += 1
    return min(prob)/(sides**2) #min treh/štirih paroma verjetnosti kock, da med danimi kockami ne velja tranzitivnost 

testni_primer1 = [[2, 2, 4, 4, 9, 9], [1, 1, 6, 6, 8, 8], [3, 3, 5, 5, 7, 7]]
testni_primer2 = [[2, 2, 4, 4, 9, 9], [1, 1, 6, 6, 8, 8], [3, 3, 5, 5, 7, 7], [1, 1, 5, 5, 9, 9]]

import random

def generator_list(m, sides): #naredi seznam različnih naravnih števil, izbira jih slučajno na intervalu 1,...,m, dolžina seznama pa je enaka številu stranic kocke
    lst = []
    random_num = None
    while len(lst) < sides:
        random_num = random.randint(1, m)
        if random_num not in lst:
            lst.append(random_num)
        else:
            continue
    return lst
        
def glavna(n, m, sides, num_of_dice): #generira m ponovitev z num_of_dice kockami, ki imajo 4 ali 3 stranice, zgornja meja za generator seznama pa je n 
    lst = []
    while len(lst) < m: 
        first = generator_list(n, sides)
        second = generator_list(n, sides)
        third = generator_list(n, sides)
        fourth = generator_list(n, sides)
        if num_of_dice == 3:
            lst.append((intransitive(([first, second, third]), sides, 3), [first, second, third]))
        elif num_of_dice == 4:
            lst.append((intransitive(([first, second, third, fourth]), sides, 4), [first, second, third, fourth]))
    maxp = 0
    for i in range(len(lst)):
        maxp = max(maxp, lst[i][0])
        lst_with_max = lst[i][1]
    return maxp, lst_with_max

#for i in range(1000): #glavna funkcija se požene 100-krat in vrne rezultate v stringu, zaradi lepšega izpisa
   #print(i, f"{int(list(zip(glavna(100000000, 10000, 6, 3)))[0][0] * 36)}" + "/36") #21/36=7/12, kar je približno 0,5833
   #print(i, f"{int(list(zip(glavna(100000000, 10000, 5, 3)))[0][0] * 25)}" + "/25") #15/25=3/5, kar je 0,6
   #print(i, f"{int(list(zip(glavna(100000000, 10000, 4, 3)))[0][0] * 16)}" + "/16") #9/16, kar je 0,5625
   #print(i, f"{int(list(zip(glavna(100000000, 10000, 3, 3)))[0][0] * 9)}" + "/9") #5/9, kar je približno 0,5556
   #print(i, f"{int(list(zip(glavna(100000000, 10000, 4, 3)))[0][0] * 36)}" + "/36") #20/36=5/9, kar je približno 0,5556

