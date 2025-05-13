def Ex1(s):
    s1 = ""
    massimo = 0
    for char in s:
        if char.isalpha():
            s1 += char
    s = s1
    count = 1
    for i in range(len(s1)-1):
        print(s[i], i, count)
        if s[i] <= s[i+1]:
            count += 1
        else:
            if count > massimo:
                massimo = count
            count = 1
    massimo = max(count, massimo)
    return massimo
            
    
    
        

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, ['cavallo'],4)
    counter_test_positivi += tester_fun(Ex1, ['arciere ponte'],2)
    counter_test_positivi += tester_fun(Ex1, ['casa vacanze arco'],3)
    counter_test_positivi += tester_fun(Ex1, ['parte di una casa'],3)
    counter_test_positivi += tester_fun(Ex1, ['ponte bassuz, tunnel lungo'],5)
    
    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
