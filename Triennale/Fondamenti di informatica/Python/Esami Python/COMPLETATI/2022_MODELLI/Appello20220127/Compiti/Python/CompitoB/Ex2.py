def Ex2(file,ins):
    sol = {}
    f = open(file, "r", encoding = "UTF-8")
    lnNum = 1
    for ln in f:
        ln = ln.strip().split()
        for word in ln:
            if word in ins:
                sol[word] = sol.get(word, [])
                if lnNum not in sol[word]:
                    sol[word].append(lnNum)
                sol[word].sort(reverse = True)
        lnNum += 1
    return sol
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt',{'palloni','Marco','devono','viaggio'}],{'Marco':[3,1],'palloni':[3,2,1],'devono':[2]})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt',{'palloni','Marco','viaggio'}],{'palloni': [3,1], 'Marco': [2, 1]})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt',{'Marco','arbitro','11'}],{'arbitro': [4, 1], '11': [3]})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt',{'Mario','arbitri','122'}],{})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt',{'Marco','fermata','222'}],{'222': [5, 4, 1], 'fermata': [4]})

    counter_test_positivi += tester_fun(Ex2, ['testo6.txt',{'palloni','4','11'}],{'4': [3, 2, 1], 'palloni': [3, 2, 1]}) 
    counter_test_positivi += tester_fun(Ex2, ['testo7.txt',{'Marco','3','pallone','palloni'}],{'3': [1], 'palloni': [2], 'Marco': [3, 2], 'pallone': [3]})
    counter_test_positivi += tester_fun(Ex2, ['testo8.txt',{'giocatori','11','mille'}],{'giocatori': [3, 2]})
    counter_test_positivi += tester_fun(Ex2, ['testo9.txt',{'Marco','arbitro','12'}],{'arbitro': [1], '12': [4, 2], 'Marco': [4, 3]})
    counter_test_positivi += tester_fun(Ex2, ['testo10.txt',{'tre','mille','11'}],{'mille': [2], 'tre': [5, 4]})
    
    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
