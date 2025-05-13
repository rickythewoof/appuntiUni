from tester import tester_fun

def D_Ex1(s,c,n):
    if n == 0:
        return s
    L=len(s)
    ris=''
    for i in range(n,L,n):
        print (i)
        ris+=s[i-n:i]+c
    ris+=s[i:L]
    return ris

## versione che fa uso del while

##def D_Ex1(s,c,n):
##    ris=''
##    i = n
##    while i!=0 and i < len(s):
##        ris+=s[i-n:i]+c
##        i+=n
##    ris+=s[i-n:len(s)]
##    return ris


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(D_Ex1, ["abcdefghi","X",3],"abcXdefXghi")
# counter_test_positivi += tester_fun(D_Ex1, ["abcdefghi","X",0],"abcdefghi")
# counter_test_positivi += tester_fun(D_Ex1, ["abcdefghi","X",2],"abXcdXefXghXi")
# counter_test_positivi += tester_fun(D_Ex1, ["123","X",1],"1X2X3")
# counter_test_positivi += tester_fun(D_Ex1, ["a","a",0],"a")

print('La funzione',D_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
