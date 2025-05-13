def Ex2(file,s):
    diz = {}
    f = open(file,encoding='UTF-8')
    num = 1
    for riga in f:
        l = []
        parole = riga.strip().split()
        for parola in parole:
            anagramma = len(parola) == len(s)
            parolamin = parola.lower()
            smin = s.lower()
            for c in parolamin:
                if parolamin.count(c) != smin.count(c):
                    anagramma = False
                    break
            if anagramma:
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

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt','lardo'],{1: [], 2: ['lardo', 'lorda'], 3: ['lardo', 'lorda'], 4: ['Darlo', 'ralod']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','lardo'],{1: [], 2: ['lardo', 'lorda'], 3: ['Darlo', 'ralod'], 4: ['LORDA']})
    counter_test_positivi += tester_fun(Ex2, ['testo1.txt','la'],{1: ['la', 'la'], 2: ['Al', 'LA'], 3: ['Al'], 4: []})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt','tanto'],{1: ['Tanto', 'tonta'], 2: [], 3: [], 4: []})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt','casa'],{1: [], 2: [], 3: ['asca', 'CAAs'], 4: ['asAc']})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testo4.txt','mado'],{1: [], 2: [], 3: [], 4: [], 5: ['moda', 'Mado'], 6: ['odMA']})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt','alpal'],{1: [], 2: [], 3: [], 4: [], 5: ['palla', 'allap'], 6: []})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt','orlac'],{1: [], 2: [], 3: [], 4: [], 5: ['carlo', 'coral'], 6: ['orcal']})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt','ollop'],{1: [], 2: [], 3: [], 4: [], 5: ['pollo'], 6: ['OLLOP', 'lolpo']})
    counter_test_positivi += tester_fun(Ex2, ['testo6.txt','casa'],{1: ['asca', 'CAAs'], 2: ['asAc'], 3: ['acsa'], 4: ['saca']})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
