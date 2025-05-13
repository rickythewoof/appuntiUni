from tester import tester_fun

def A_Ex1(s,n):
    sum = 0
    for i in range(len(s)):
        sum += ord(s[i])
        print(sum,s[i])
        if sum > n:
            return s[i:]
    return ""
	
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex1, ['abc',200], 'c')
counter_test_positivi += tester_fun(A_Ex1, ['abc',100], 'bc')
counter_test_positivi += tester_fun(A_Ex1, ['',0], '')
counter_test_positivi += tester_fun(A_Ex1, ['1234',10], '1234')
counter_test_positivi += tester_fun(A_Ex1, ['zorro',10000], '')

print('La funzione',A_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
