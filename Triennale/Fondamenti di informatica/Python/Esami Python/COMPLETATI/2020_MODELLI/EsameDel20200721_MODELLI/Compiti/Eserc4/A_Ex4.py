from tester import tester_fun

def A_Ex4(file1,file2):
    obj = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    for ln in f1:
        dati = ln.strip().split(",")
        nome = dati[0]
        ogg = dati[1]
        prezzo = int(dati[2])
        obj[ogg] = obj.get(ogg, [])
        obj[ogg].append(nome)
        obj[ogg].append(prezzo)
    f1.close()
    off = {}
    f2 = open(file2, "r", encoding ="UTF-8")
    for ln in f2:
        dati = ln.strip().split(",")
        nome = dati[0]
        ogg = dati[1]
        prezzo = int(dati[2])
        nomeVenditore = obj[ogg][0]
        print(dati, nome, nomeVenditore)
        if prezzo > obj[ogg][1]:
            off[nome] = off.get(nome, [0,0])
            off[nomeVenditore] = off.get(nomeVenditore, [0,0])
            obj[ogg] = [nome, prezzo]
            off[nome][0] += 1
            off[nome][1] -= prezzo
            off[nomeVenditore][0]  -= 1
            off[nomeVenditore][1]  += prezzo
            print(off)
    return off
            
        
    
                       

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['oggetti1.csv','offerte1.csv'],{'Paolo': [-1, 21], 'Francesco': [0, 4], 'Gianni': [1, -25]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti1.csv','offerte2.csv'],{'Paolo': [-2, 51], 'Francesco': [0, 4], 'Gianni': [2, -55]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti2.csv','offerte3.csv'],{'Paolo': [-2, 50], 'Francesco': [0, 4], 'Gianni': [2, -54]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti2.csv','offerte4.csv'],{'Paolo': [-3, 102], 'Francesco': [0, 4], 'Gianni': [2, -55], 'Piero': [1, -51]})
counter_test_positivi += tester_fun(A_Ex4, ['oggetti3.csv','offerte5.csv'],{'Paolo': [-3, 102], 'Francesco': [0, 4], 'Gianni': [2, -55], 'Piero': [0, 1], 'Giovanna': [1, -52]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
