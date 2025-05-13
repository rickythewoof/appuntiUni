from tester import tester_fun

def A_Ex4(file1,file2):
    d = {}
    f = open(file1, "r", encoding = "UTF-8")
    ln = f.readline().strip().split(",")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        user = ln[0]
        money = int(ln[1])
        d[user] = [money,0,0]
        ln = f.readline().strip().split(",")
    f.close()
    f = open(file2, "r", encoding = "UTF-8")
    ln = f.readline().strip().split(",")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        sender = ln[0]
        receiver = ln[1]
        sent = int(ln[2])
        bankSender = d[sender][0]
        bankReceiver = d[receiver][0]
        print(sender, bankSender, receiver, bankReceiver, "INVIO", sent)
        if sent < bankSender:
            print("PRIMA", sender, d[sender], receiver, d[receiver])
            d[sender][1] = max(sent,d[sender][1])
            d[receiver][2] = max(sent,d[receiver][2])
            d[sender][0] -= sent
            d[receiver][0] += sent
            print("DOPO", sender, d[sender], receiver, d[receiver])
        else:
            print("FALLITO!")
        ln = f.readline().strip().split(",")
    return d
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['utenti1.csv','trasferimenti1.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1400, 0, 500], 'Federica': [1800, 700, 0]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti2.csv','trasferimenti2.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1400, 0, 500], 'Federica': [1700, 700, 0], 'Paolo': [200, 0, 100]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti3.csv','trasferimenti3.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1900, 0, 500], 'Federica': [700, 700, 0], 'Paolo': [600, 500, 100]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti4.csv','trasferimenti4.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1700, 200, 500], 'Federica': [700, 700, 0], 'Paolo': [600, 500, 100], 'Sandra': [200, 0, 200]})
counter_test_positivi += tester_fun(A_Ex4, ['utenti5.csv','trasferimenti5.csv'] ,{'Marta': [1550, 150, 700], 'Gianni': [1900, 0, 500], 'Federica': [500, 700, 0], 'Paolo': [600, 500, 100], 'Sandra': [200, 0, 200], 'Irene': [0, 0, 0]})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
