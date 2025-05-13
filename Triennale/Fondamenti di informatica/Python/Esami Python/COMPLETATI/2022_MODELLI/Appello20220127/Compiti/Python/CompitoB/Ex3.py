def Ex3(file1,file2,n):
    d = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    for ln in f1:
        ln = ln.strip().split(",")
        nome = ln[0]
        qt = int(ln[1])
        prezzo = int(ln[2])
        d[nome] = [qt, prezzo]
    f1.close()
    print(d)
    sol = {}
    day = 1
    f2 = open(file2, "r", encoding = "UTF-8")
    for ln in f2:
        ln = ln.strip().split(",")
        giorno = int(ln[0])
        nome = ln[1]
        mov = int(ln[2])
        print(d[nome])
        prezzo = d[nome][1]
        if day <= n and giorno > n:
            return sol
        else:
            sol[nome] = sol.get(nome, [0,0])
            if mov > 0:
                d[nome][0] += mov
            else:
                if abs(mov) <= d[nome][0]:
                   sol[nome][0] += (abs(mov)*prezzo) 
                   d[nome][0] += mov
                else:
                    diff = abs(d[nome][0]+mov)
                    sol[nome][0] += (abs(mov+diff)*prezzo) 
                    d[nome][0] += mov+diff
                    sol[nome][1] += abs(diff*prezzo)
        day += abs(giorno-day)        
    return sol            
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv',10],{'Ipad': [4200, 1400], 'Iphone': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv',11],{'Ipad': [4200, 1400], 'Iphone': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti2.csv',9],{'Ipad': [5600, 0], 'Iphone': [5000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti1.csv',7],{'Ipad': [1200, 2000], 'Iphone': [4000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti2.csv',17],{'Ipad': [2000, 1200], 'Iphone': [7000, 5000], 'Ps5': [2500, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti3.csv',10],{'Galaxy': [4200, 1400], 'Xbox': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti3.csv',11],{'Galaxy': [4200, 1400], 'Xbox': [5000, 1000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti4.csv',9],{'Galaxy': [5600, 0], 'Xbox': [5000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti3.csv',7],{'Galaxy': [1200, 2000], 'Xbox': [4000, 2000]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti4.csv',17],{'Galaxy': [2000, 1200], 'Xbox': [7000, 5000], 'PC': [2500, 1000]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
