from tester import tester_fun

def C_Ex1(s1, s2):
    ris=''
    i=0
    while i <min(len(s1),len(s2)):
        ris=ris+s1[i]+s2[len(s2)-1-i]
        i+=1
    if len(s1) > len(s2):
        ris += s1[i:len(s1)]
    if len(s2) > len(s1):
        ris += s2[0:len(s2)-i]      
    return ris

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
