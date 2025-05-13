def Ex3(file1,file2):
    sol = {}
    d1 = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    for ln in f1:
        ln = ln.strip().split(",")
        nome = ln[0]
        qt = int(ln[1])
        qtMin = int(ln[2])
        prezzo = int(ln[3])
        sol[nome] = [qt, 0, prezzo]
        d1[nome] = qtMin
    print(sol, d1)
    f1.close()
    f2 = open(file2, "r", encoding = "UTF-8")
    for ln in f2:
        ln = ln.strip().split(",")
        nome = ln[0]
        qt = int(ln[1])
        qtMin = d1[nome]
        print(ln, sol[nome])
        if qt > 0:
            if sol[nome][0] < qtMin and (qt + sol[nome][0]) >= qtMin:
                sol[nome][2] -= 5       #aumento il prezzo di 5
            sol[nome][0] += qt
            print(sol[nome])
        elif qt < 0:
            if sol[nome][0] > abs(qt):
                if sol[nome][0] > qtMin and (qt + sol[nome][0]) <= qtMin:
                    sol[nome][2] += 5       #aumento il prezzo di 5
                sol[nome][0] += qt          #rimuovo qt quantità   
            elif sol[nome][0] < abs(qt):
                if sol[nome][0] > qtMin and (qt + sol[nome][0]) <= qtMin:
                    sol[nome][2] += 5       #aumento il prezzo di 5
                sol[nome][1] += abs(sol[nome][0] + qt)
                sol[nome][0] = 0
            print(sol[nome])
    return(sol)
            
        
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti1.csv'],{'Iphone': [16, 0, 500], 'Ipad': [0, 2, 705], 'Ps5': [5, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti2.csv'],{'Iphone': [16, 0, 500], 'Ipad': [3, 2, 700], 'Ps5': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino1.csv','acquisti3.csv'],{'Iphone': [4, 0, 505], 'Ipad': [10, 2, 700], 'Ps5': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti1.csv'],{'Iphone': [11, 0, 500], 'Ipad': [0, 2, 705], 'Ps5': [3, 0, 400]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino2.csv','acquisti2.csv'],{'Iphone': [11, 0, 500], 'Ipad': [3, 2, 700], 'Ps5': [5, 0, 400]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti4.csv'],{'Xbox': [16, 0, 500], 'Galaxy': [0, 2, 705], 'Ps4': [5, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti5.csv'],{'Xbox': [16, 0, 500], 'Galaxy': [3, 2, 700], 'Ps4': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino3.csv','acquisti6.csv'],{'Xbox': [4, 0, 505], 'Galaxy': [10, 2, 700], 'Ps4': [7, 0, 500]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti4.csv'],{'Xbox': [11, 0, 500], 'Galaxy': [0, 2, 705], 'Ps4': [3, 0, 400]})
    counter_test_positivi += tester_fun(Ex3, ['magazzino4.csv','acquisti5.csv'],{'Xbox': [11, 0, 500], 'Galaxy': [3, 2, 700], 'Ps4': [5, 0, 400]})

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
