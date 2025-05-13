from tester import tester_fun

def C_Ex4(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    for ln in f:
        numeri = ln.strip().split(",")
        for numero in numeri:
            num = int(numero)
            d[num] = d.get(num,0)
            d[num] += 1
    maxNum = []
    freq = 0
    for key in d:
        if d[key] < freq:
            continue
        elif d[key] > freq:
            maxNum.clear()
            freq = d[key]
        maxNum.append(key)
    maxNum.sort()
    return maxNum
   

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex4, ['ruota1.csv'],[14,50])
counter_test_positivi += tester_fun(C_Ex4, ['ruota2.csv'],[2,14])
counter_test_positivi += tester_fun(C_Ex4, ['ruota3.csv'],[2])
counter_test_positivi += tester_fun(C_Ex4, ['ruota4.csv'],[24,43,47,50])
counter_test_positivi += tester_fun(C_Ex4, ['ruota5.csv'],[])

print('La funzione',C_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
