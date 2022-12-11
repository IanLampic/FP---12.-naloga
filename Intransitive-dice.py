def intranzitivnost(seznam):
    lst = []
    for list in seznam:
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
    return min(p1, p2, p3)/36 #min treh verjetnosti, da spodnjo omejitev za verjetnost, da med danimi tremi kockami ne velja tranzitivnost

testni_primer = [[2, 2, 4, 4, 9, 9], [1, 1, 6, 6, 8, 8], [3, 3, 5, 5, 7, 7]]

print(intranzitivnost(testni_primer) == 5/9)
