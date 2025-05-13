from tester import tester_fun

def C_Ex1(s1, s2):
    sol = ""
    s2 = s2[::-1]
    minLen = min (len(s1), len(s2))
    for i in range(minLen):
        sol += s1[i]
        sol += s2[i]
    if len(s1) > len(s2):
        sol+= s1[minLen:]
    if len(s1) < len(s2):
        s2 = s2[::-1]
        diff = len(s2)- len(s1)
        sol += s2[0:diff]
    return (sol) 

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5 

counter_test_positivi += tester_fun(C_Ex1, ["abcd","xyefgh"] , "ahbgcfdexy")
counter_test_positivi += tester_fun(C_Ex1, ["abcd","ef"] , "afbecd")
counter_test_positivi += tester_fun(C_Ex1, ["abc","abc"] , "acbbca")
counter_test_positivi += tester_fun(C_Ex1, ["xyz","a"] , "xayz")
counter_test_positivi += tester_fun(C_Ex1, ["a","b"] , "ab")


print('La funzione',C_Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
