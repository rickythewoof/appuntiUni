from tester import tester_fun

def C_Ex1(s1,s2):
    sol = ""
    for char in s2:
        count = s1.count(char)
        sol += char*count
    for char in s1:
        if s2.count(char) == 0:
            sol += char
    return sol

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex1, ['allegria', 'jeah'], 'eaallgri')
counter_test_positivi += tester_fun(C_Ex1, ['allegria', ''], 'allegria')
counter_test_positivi += tester_fun(C_Ex1, ['dghhlf', 'hdgle'], 'hhdglf')
counter_test_positivi += tester_fun(C_Ex1, ['ba', 'ab'], 'ab')
counter_test_positivi += tester_fun(C_Ex1, ['entertainment', 'ae'], 'aeeentrtinmnt')

print('La funzione',C_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)