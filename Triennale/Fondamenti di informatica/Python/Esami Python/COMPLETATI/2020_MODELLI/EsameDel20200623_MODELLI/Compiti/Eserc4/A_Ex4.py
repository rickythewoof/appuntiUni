from tester import tester_fun

def A_Ex4(file1,file2):
    prod = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    ln = f1.readline().strip().split(",")
    ln = f1.readline().strip().split(",")
    while ln != [""]:
        prod[ln[0]] = int(ln[1])
        ln = f1.readline().strip().split(",")
    print(prod)
    ris = {}
    ricevute = {}
    f2 = open(file2, "r", encoding = "utf-8")
    ln = f2.readline().strip().split(",")
    ln = f2.readline().strip().split(",")
    while ln != [""]:
        ricevuta = ln[0]
        prodotto = ln[1]
        quantita = int(ln[2])
        ris[ricevuta] = ris.get(ricevuta, 0)
        ricevute[prodotto] = ricevute.get(prodotto, [])
        if ricevuta not in ricevute[prodotto]:
            ricevute[prodotto].append(ricevuta)
            totCosto = prod[prodotto] * quantita
            ris[ricevuta] += totCosto
        ln = f2.readline().strip().split(",")
    return ris
    

            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute1.csv'],{'R1': 13, 'R2': 12, 'R3': 6})
counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute2.csv'],{'R1': 13, 'R2': 12, 'R3': 6} )
counter_test_positivi += tester_fun(A_Ex4, ['costi1.csv','ricevute3.csv'] ,{'R4': 6})
counter_test_positivi += tester_fun(A_Ex4, ['costi2.csv','ricevute4.csv'],{'R6': 8, 'R7': 410})
counter_test_positivi += tester_fun(A_Ex4, ['costi2.csv','ricevute1.csv'] ,{'R1': 8, 'R2': 14, 'R3': 12})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
