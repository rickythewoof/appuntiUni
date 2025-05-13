def Ex1(l,n):
    sol = set()
    for i in range(len(l)):
        for j in range (i+1, len((l))):
            count = 0
            for charIndex in range (len(l[i])):
                print(l[i][charIndex], l[i][charIndex:].count(l[i][charIndex]))
                if l[i][charIndex:].count(l[i][charIndex]) == 1:
                    print("uno solo!", l[j])
                    for charIndexJ in range(len(l[j])):
                        if l[i][charIndex] == l[j][charIndexJ] and l[j][charIndexJ:].count(l[j][charIndexJ]) == 1:
                            print("almeno una  lettera")
                            count += 1
            if count >= n:
                sol.add(l[i])
                sol.add(l[j]) 
    return sol

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex1, [['arciere', 'pippo', 'accordare'],2],{'accordare', 'arciere'})
    counter_test_positivi += tester_fun(Ex1, [["arciere","pippo","pluto"],1],{'arciere', 'pluto', 'pippo'})
    counter_test_positivi += tester_fun(Ex1, [["arciere","pompiere","bere"],3],{'arciere', 'pompiere'})
    counter_test_positivi += tester_fun(Ex1, [["mare","amare","mammare",""],3],{'mammare', 'mare', 'amare'})
    counter_test_positivi += tester_fun(Ex1, [["mento","casa","cero"],2],{'mento', 'cero'})

    counter_test_positivi += tester_fun(Ex1, [['aquila', 'torta', 'parli','pippo'] ,1],{'aquila', 'torta', 'parli','pippo'}) # tutte le parole in output
    counter_test_positivi += tester_fun(Ex1, [[],2],set()) # input lista vuota
    counter_test_positivi += tester_fun(Ex1, [['anna','essere','uovo','può'],2],set()) # output vuoto
    counter_test_positivi += tester_fun(Ex1, [['anna','annabella','bellissima'],3],{'annabella','bellissima'}) # n caratteri in comune ma non distinti
    counter_test_positivi += tester_fun(Ex1, [['anatema','anna','mentana'],5],{'anatema', 'mentana'}) # più caratteri della lunghezza delle parole

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
