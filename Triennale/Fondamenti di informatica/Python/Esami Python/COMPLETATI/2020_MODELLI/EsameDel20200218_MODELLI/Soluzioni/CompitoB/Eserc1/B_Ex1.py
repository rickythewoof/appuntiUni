from tester import tester_fun

def B_Ex1(s):
    r=''
    i=0
    while(i<len(s)):
        c=s[i]
        j=i
        n=0
        finito=False
        while(j<len(s) and not finito):
            if (s[i]==s[j]):
                n=n+1
                j=j+1
            else:
                finito=True
        i=j
        r=r+str(n)+c
    return r


###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex1, ["WWWWEERWWRRRFF"] , "4W2E1R2W3R2F")
counter_test_positivi += tester_fun(B_Ex1, ["sTTTFFL"] , "1s3T2F1L")
counter_test_positivi += tester_fun(B_Ex1, [""] , "")
counter_test_positivi += tester_fun(B_Ex1, ["a"] , "1a")
counter_test_positivi += tester_fun(B_Ex1, ["aaaahhajjllhhhh"] , "4a2h1a2j2l4h")

print('La funzione',B_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
