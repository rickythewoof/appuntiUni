def Ex2(file,s):
    num = 0
    m = []
    f = open(file, "r", encoding = "UTF-8") 
    for ln in f:
        ln = ln.strip()
        m.append(list(ln))
        if s in ln or s[::-1] in ln:
            num+= 1
            print(ln)
    for colonna in range(len(m[0])):
        string = ""
        for riga in range(len(m)):
            string += m[riga][colonna]
        if s in string or s[::-1] in string:
            num+=1
            print(string)
    return num            
        
            
        
            
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt','PORO'],3)
    counter_test_positivi += tester_fun(Ex2, ['testo1.txt','ATO'],1)
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','PORTO'],2)
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','PO'],6)
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','ROT'],2)
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt','POLTO'],2)
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt','TAT'],0)
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt','GT'],3)
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt','PPPP'],1)
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt','GP'],3)

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
