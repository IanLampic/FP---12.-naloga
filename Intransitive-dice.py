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

#for i in range(25): #krovna funkcija se požene 100-krat in vrne rezultate v stringu, zaradi lepšega izpisa
#   func0 = krovna(1000000, 100000, 6, 8)
#   print(i, func0[0])
   #func1 = krovna(100000000, 10000, 5, 3)
   #func2 = krovna(100000000, 10000, 4, 3)
   #func3 = krovna(100000000, 10000, 3, 3)
   #func4 = krovna(100, 10000, 6, 4)
   #print(f"{i}.", "Verjetnost, da ne velja tranzitivnost je enaka " + f"{func0[0]}" + "/36" + "," + " za dane kocke:" + "\n" + f"{func0[1][0]}" + "\n" + f"{func0[1][1]}" + "\n" + f"{func0[1][2]}" + "\n") #21/36=7/12, kar je približno 0,5833
   #print(f"{i}.", "Verjetnost, da ne velja tranzitivnost je enaka " + f"{func1[0]}" + "/25" + "," + " za dane kocke:" + "\n" + f"{func1[1][0]}" + "\n" + f"{func1[1][1]}" + "\n" + f"{func1[1][2]}" + "\n") #15/25=3/5, kar je 0,6
   #print(f"{i}.", "Verjetnost, da ne velja tranzitivnost je enaka " + f"{func2[0]}" + "/16" + "," + " za dane kocke:" + "\n" + f"{func2[1][0]}" + "\n" + f"{func2[1][1]}" + "\n" + f"{func2[1][2]}" + "\n") #9/16, kar je 0,5625
   #print(f"{i}.", "Verjetnost, da ne velja tranzitivnost je enaka " + f"{func3[0]}" + "/9" + "," + " za dane kocke:" + "\n" + f"{func3[1][0]}" + "\n" + f"{func3[1][1]}" + "\n" + f"{func3[1][2]}" + "\n") #5/9, kar je približno 0,5556
   #print(f"{i}.", "Verjetnost, da ne velja tranzitivnost je enaka " + f"{func4[0]}" + "/36" + "," + " za dane kocke:" + "\n" + f"{func4[1][0]}" + "\n" + f"{func4[1][1]}" + "\n" + f"{func4[1][2]}" + "\n" + f"{func4[1][3]}" + "\n") #20/36=5/9, kar je približno 0,5556
   #print(f"{i}.", "Verjetnost, da ne velja tranzitivnost je enaka " + f"{func0[0]}" + "/9" + "," + " za dane kocke:" + "\n" + f"{func0[1][0]}" + "\n" + f"{func0[1][1]}" + "\n" + f"{func0[1][2]}" + "\n" + f"{func0[1][3]}" + "\n"+ f"{func0[1][4]}" + "\n"+ f"{func0[1][5]}" + "\n"+ f"{func0[1][6]}" + "\n"+ f"{func0[1][7]}" + "\n"+ f"{func0[1][8]}" + "\n"+ f"{func0[1][9]}" + "\n") #5/9, kar je približno 0,5556
##3 kocke
#stranost: 3:5/9, 4:9/16, 5:15/25, 6:21/36, 7:28/49, 8:36/64, 9:45/81, 10: 56/100
##6 strane kocke
#število kock: 3: 21/36, 4: 20/36 , 5: 19/36, 6: 19/36, 7:19/36(18?),8:18/36 9:18/36 10: 17/36

