from tester import tester_fun

def B_Ex1(s):
    sol = ""
    consecutive = 1
    for i in range(len(s)):
        if i != len(s)-1 and s[i+1] == s[i]:
            consecutive += 1
        elif  i == len(s)-1 or s[i+1] != s[i]:
            sol += str(consecutive)+s[i]
            consecutive = 1
    return sol
            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["WWWWEERWWRRRFF"] , "4W2E1R2W3R2F")
counter_test_positivi += tester_fun(B_Ex1, ["sTTTFFL"] , "1s3T2F1L")
counter_test_positivi += tester_fun(B_Ex1, [""] , "")
counter_test_positivi += tester_fun(B_Ex1, ["a"] , "1a")
counter_test_positivi += tester_fun(B_Ex1, ["aaaahhajjllhhhh"] , "4a2h1a2j2l4h")

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
