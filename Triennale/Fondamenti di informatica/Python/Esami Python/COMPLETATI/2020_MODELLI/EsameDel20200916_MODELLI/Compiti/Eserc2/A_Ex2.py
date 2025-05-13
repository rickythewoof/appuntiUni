from tester import tester_fun

def A_Ex2(M):
    medie = [0 for i in range(len(M[0]))]
    voti = {}
    for studente in range(len(M[0])):
        voti[studente] = []
        for voto in range(len(M)):
            voti[studente].append(M[voto][studente])
    for studente in voti:
        media = 0
        numeroVoti = 0
        for voto in voti[studente]:
            if voto != 0:
                media += voto
                numeroVoti+=1
        if numeroVoti == 0:
            medie[studente] = 0
            continue
        media = round(media/numeroVoti, 2)
        medie[studente] = media
    return medie 
            
            
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, [[[24, 30, 0], [22, 0, 28], [23, 29, 0], [18, 0, 0]]],[21.75, 29.50, 28.0])
counter_test_positivi += tester_fun(A_Ex2, [[[0, 26, 30, 0], [0, 24, 30, 18]]],[0, 25.0, 30.0, 18.0])
counter_test_positivi += tester_fun(A_Ex2, [[[0, 26], [0, 24],[19, 23],[20, 0]]],[19.5, 24.33])
counter_test_positivi += tester_fun(A_Ex2, [[[18], [19], [20], [21], [0], [22]]],[20])
counter_test_positivi += tester_fun(A_Ex2, [[[25, 28, 30, 26], [27, 30, 30, 24], [25, 28, 30, 26]]],[25.67, 28.67, 30.0, 25.33])

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)


