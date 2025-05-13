def Ex2(file,d):
    diz = {}
    f = open(file,encoding='UTF-8')
    num = 1
    for riga in f:
        l = []
        parole = riga.strip().split()
        for parola in parole:
            ok = True
            parolamin = parola.lower()
            for c in parolamin:
                if c not in d or parolamin.count(c) < d[c]:
                    ok = False
                    break
            for c in d:
                if c not in parolamin:
                    ok = False
                    break                    
            if ok:
                l.append(parola)
        diz[num] = l
        num += 1
    return diz
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt',{'l':1,'a':1,'n':1}],{1: [], 2: ['lana'], 3: ['Lanna', 'LAN']})
    counter_test_positivi += tester_fun(Ex2, ['testo1.txt',{'l':1,'a':2,'n':1}],{1: [], 2: ['lana'], 3: ['Lanna']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt',{'l':1,'a':2,'n':1}],{1: [], 2: ['lana'], 3: ['Lanna'], 4: ['annaL']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt',{'g':1,'a':2,'t':1}],{1: ['gatta'], 2: [], 3: [], 4: ['gata']})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt',{'l':2,'a':2,'n':1}],{1: [], 2: [], 3: [], 4: [], 5: ['lannal']})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testo3.txt',{'l':1,'a':2,'n':2}],{1: [], 2: [], 3: ['Lanna'], 4: ['annaL'], 5: ['lannal']})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt',{'g':1,'a':2,'t':2}],{1: ['gatta'], 2: [], 3: [], 4: [], 5: [], 6: []})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt',{'l':2,'a':2,'n':1}],{1: [], 2: [], 3: [], 4: [], 5: [], 6: []})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt',{'g':1,'a':2,'t':2,'r':1}],{1: [], 2: [], 3: ['gattara'], 4: [], 5: ['gratta', 'gattara']})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt',{'g':1,'a':3,'t':2,'r':1}],{1: [], 2: [], 3: ['gattara'], 4: [], 5: ['gattara']})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
