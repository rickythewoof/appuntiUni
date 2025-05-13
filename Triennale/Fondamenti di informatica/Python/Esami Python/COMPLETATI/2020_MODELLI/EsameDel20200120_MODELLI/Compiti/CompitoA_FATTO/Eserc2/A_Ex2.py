from tester import tester_fun

def A_Ex2(file1,file2):
    oggetti = {}
    f1 = open(file1, "r", encoding = "utf-8")
    obj = f1.readline().strip().split(",")
    obj = f1.readline().strip().split(",")
    while obj != [""]:
        oggetto = obj[0]
        prezzo = int(obj[1])
        oggetti[oggetto] = prezzo
        obj = f1.readline().strip().split(",")
    f1.close()
    offerte = {}
    f2 = open(file2, "r", encoding = "utf-8")
    ln = f2.readline().strip().split(",")
    ln = f2.readline().strip().split(",")
    while ln != [""]:
        acquirente = ln[0]
        oggetto = ln[1]
        offerta = int(ln[2])
        if offerta >= oggetti[oggetto]:
            offerte[oggetto] = offerte.get(oggetto, [acquirente, offerta])
        elif oggetto in offerte and offerta > offerte[oggetto][1]:
            offerte[oggetto] = [acquirente, offerta]
        ln = f2.readline().strip().split(",")
    return offerte

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex2, ['oggetti1.csv','offerte1.csv'] ,{'Vaso': ['Giorgio', 120], 'Sedia': ['Mario', 100]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti2.csv','offerte2.csv'] ,{'Vaso': ['Giorgio', 120], 'Sedia': ['Mario', 100]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti3.csv','offerte3.csv'] ,{'Vaso': ['Giorgio', 120], 'Iphone': ['Giulia', 500]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti4.csv','offerte4.csv'] ,{'Sedia': ['Mario', 100], 'Iphone': ['Giulia', 500]})
counter_test_positivi += tester_fun(A_Ex2, ['oggetti5.csv','offerte5.csv'] ,{'Sedia': ['Mario', 100], 'Iphone': ['Giulia', 500], 'Tavolo': ['Mario', 210]})

print('La funzione',A_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
