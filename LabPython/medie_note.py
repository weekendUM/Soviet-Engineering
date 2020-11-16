def calcul_medie (note):
    medie = 0.0
    medie_ponderata = 0.0
    total = 0
    for i in range(0, len(note)):
        #print(i)
        total = total + note[i][1]
    medie = total / len(note)
    counter = 0
    total = 0
    for i in range(len(note)):
        total = total + (note[i][1] * note[i][2])
        #print(total)
        counter = counter + note[i][2]
        #print(counter)
    medie_ponderata = total / counter
    
    return medie, medie_ponderata
