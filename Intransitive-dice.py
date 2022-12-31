def comparison(sez1, sez2):
    count = 0
    p = []
    sez1.sort()
    sez2.sort()
    for i in range(len(sez1)):
        for j in range(len(sez2)):
            if sez1[i] > sez2[j]: 
                count += 1
        p.append(count) 
        count = 0 
    return p

testni_primer1 = [[2, 2, 4, 4, 9, 9], [1, 1, 6, 6, 8, 8], [3, 3, 5, 5, 7, 7]]
testni3 = [[24, 31, 34, 38, 44, 45], [3, 7, 27, 40, 44, 46], [9, 10, 21, 27, 30, 39]]
testni_primer2 = [[2, 2, 4, 4, 9, 9], [1, 1, 6, 6, 8, 8], [3, 3, 5, 5, 7, 7], [1, 1, 5, 5, 9, 9]]

def intransitive(dice):
    numb_of_dice = len(dice)
    lst_of_probs = []
    for i in range(numb_of_dice - 1):
        comparison(dice[i], dice[i+1])
        lst_of_probs.append((sorted(dice[i]), sorted(dice[i + 1]), sum(comparison(dice[i], dice[i+1]))))
    lst_of_probs.append((sorted(dice[numb_of_dice-1]), sorted(dice[0]), sum(comparison(dice[numb_of_dice-1], dice[0]))))
    prob = 100 #določena zgornja meja za minimum, ki ne bo presežena
    for i in range(len(lst_of_probs)):
        prob = min(prob, lst_of_probs[i][2])
    return prob, dice

import random

def generator_list(m, sides): #naredi seznam različnih naravnih števil, izbira jih slučajno na intervalu 1,...,m, dolžina seznama pa je enaka številu stranic kocke
    st = set()
    while len(st) < sides:
        random_num = random.randint(1, m)
        st.add(random_num)
    return list(st)

def krovna(n, m, sides, num_of_dice): #generira m ponovitev z num_of_dice kockami, ki imajo sides stranic, zgornja meja za generator seznama pa je n 
    lst = []
    while len(lst) < m: 
        dice = []
        for i in range(num_of_dice):
            dice.append(generator_list(n, sides))
        lst.append(intransitive(dice))
    max_prob = 0
    for i in range(len(lst)):
        if max_prob < lst[i][0]:
            max_prob = lst[i][0]
            lst_with_max = lst[i][1]
    return max_prob, lst_with_max

for i in range(100): #krovna funkcija se požene 100-krat in vrne rezultate v stringu, zaradi lepšega izpisa
   func = krovna(100000000, 10000, 6, 3)
   print(i, f"{func[0]}" + "/36", func[1]) #21/36=7/12, kar je približno 0,5833
   #print(i, f"{func[0]}" + "/25", func[1]) #15/25=3/5, kar je 0,6
   #print(i, f"{func[0]}" + "/16", func[1]) #9/16, kar je 0,5625
   #print(i, f"{func[0]}" + "/9", func[1]) #5/9, kar je približno 0,5556
   #print(i, f"{func[0]}" + "/36", func[1]) #20/36=5/9, kar je približno 0,5556


