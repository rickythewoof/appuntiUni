from tester import tester_fun

def B_Ex4(file):
    d = {}
    sol = {}
    f = open(file, "r", encoding = "UTF-8")
    ln = f.readline().strip().split(",")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        prod = ln[0]
        qt = int(ln[1])
        d[prod] = d.get(prod, 0)
        if qt < 0 and d[prod] < abs(qt):
            diff = abs(qt) - d[prod]
            d[prod] = 0
            sol[prod] = sol.get(prod, 0) + diff
        else:
            d[prod] = d.get(prod, 0) + qt
        ln = f.readline().strip().split(",")
    for key in d:
        if d[key] < 0:
            sol[key] = abs(d[key])
    return sol
    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['file1.csv'],{'Lavatrice':3,'Televisore':1})
counter_test_positivi += tester_fun(B_Ex4, ['file2.csv'],{'Frigorifero':3,'PS4':3})
counter_test_positivi += tester_fun(B_Ex4, ['file3.csv'],{})
counter_test_positivi += tester_fun(B_Ex4, ['file4.csv'],{'Televisore':3,'Frigorifero':1})
counter_test_positivi += tester_fun(B_Ex4, ['file5.csv'],{'Decoder':50,'Frigorifero':1,'Forno':1})

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
