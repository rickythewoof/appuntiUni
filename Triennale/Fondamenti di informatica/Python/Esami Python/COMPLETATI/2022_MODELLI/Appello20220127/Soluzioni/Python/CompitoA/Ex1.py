def Ex1(l):
    massimo = 0
    for i in range(len(l)):
        conta = 1
        for j in range(i+1,len(l)-1):
            print(i, j, l[i],l[j], l[j]+1)
            if l[j] < l[j+1]:
                print("aggiungo")
                conta += 1
            else: break
        if conta > massimo:
            massimo = conta
    return massimo
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [[1,2,3,3,1,4,5,1,7]],3)
    # counter_test_positivi += tester_fun(Ex1, [[1,2,1,4,3,4,3]],2)
    # counter_test_positivi += tester_fun(Ex1, [[100,70,70,30,70,70,88]],2)
    # counter_test_positivi += tester_fun(Ex1, [[4,3,3,2,1]],1)
    # counter_test_positivi += tester_fun(Ex1, [[]],0)

    # # test aggiuntivi

    # counter_test_positivi += tester_fun(Ex1, [[11,14,15,1,2,3,1,17,18,19]],4)
    # counter_test_positivi += tester_fun(Ex1, [[11,12,11,24,25,12,15]],3)
    # counter_test_positivi += tester_fun(Ex1, [[12,11,10,9,10,7,8,2]],2)
    # counter_test_positivi += tester_fun(Ex1, [[1,2,2,3,3,4,5]],3)
    # counter_test_positivi += tester_fun(Ex1, [[10]],1)

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
