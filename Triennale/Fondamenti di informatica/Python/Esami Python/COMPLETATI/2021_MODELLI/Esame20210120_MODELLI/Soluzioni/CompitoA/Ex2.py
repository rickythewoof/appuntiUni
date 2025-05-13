def Ex2(file):
    import re
    diz = {}
    testo = open(file,'r',encoding='UTF-8').read()
    pattern = r'\d\d\d-?(\d\d)-?\d\d\d-?\d\d\d\d-?\d'
    r = re.finditer(pattern,testo)
    for m in r:
        codice = m.group().replace('-','')
        lingua = m.group(1)
        somma = 0
        for i in range(len(codice)):
            if i % 2 == 0:
                somma += int(codice[i])
            else:
                somma += 3*int(codice[i])
        if somma % 10 == 0:
            diz[lingua] = diz.get(lingua,0) + 1
    return diz
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{'88': 1, '78': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{'88': 2, '78': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{'88': 2, '78': 2, '15': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{'88': 2, '78': 2, '15': 1, '05': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{'88': 1, '78': 1, '15': 1, '05': 1})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testo6.txt'],{'88': 2, '20': 1, '07': 1, '18': 1}) # tutti i codici sono validi
    counter_test_positivi += tester_fun(Ex2, ['testo7.txt'],{}) # nessun codice è valido
    counter_test_positivi += tester_fun(Ex2, ['testo8.txt'],{'88': 2, '14': 1}) # mix codici validi e non
    counter_test_positivi += tester_fun(Ex2, ['testo9.txt'],{}) # testo vuoto
    counter_test_positivi += tester_fun(Ex2, ['testo10.txt'],{'88': 2, '20': 1, '07': 1}) # validi tutti con i trattini

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
