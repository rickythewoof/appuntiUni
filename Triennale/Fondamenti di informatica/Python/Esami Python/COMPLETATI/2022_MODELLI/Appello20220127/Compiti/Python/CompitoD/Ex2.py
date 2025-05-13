

def Ex2(file,d):
    sol = {}
    parola = "".join(sorted(d.keys()))
    print(parola)
    lnNum = 1
    f = open(file, "r", encoding = "UTF-8")  
    for ln in f:
        sol[lnNum] = []
        ln = ln.strip().split()
        for word in ln:
            si = True
            for char in word:
                if char not in d or word.lower().count(char) < d[char]:
                    si = False
                    break
            print ("PRIMA",word)
            for char in d:
                if char not in word.lower():
                    si = False
                    break
            print("DOPO", word)
            if si:
                sol[lnNum].append(word)
        lnNum += 1
    return sol

    
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt',{'l':1,'a':1,'n':1}],{1: [], 2: ['lana'], 3: ['Lanna', 'LAN']})
    counter_test_positivi += tester_fun(Ex2, ['testo1.txt',{'l':1,'a':2,'n':1}],{1: [], 2: ['lana'], 3: ['Lanna']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt',{'l':1,'a':2,'n':1}],{1: [], 2: ['lana'], 3: ['Lanna'], 4: ['annaL']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt',{'g':1,'a':2,'t':1}],{1: ['gatta'], 2: [], 3: [], 4: ['gata']})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt',{'l':2,'a':2,'n':1}],{1: [], 2: [], 3: [], 4: [], 5: ['lannal']})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
