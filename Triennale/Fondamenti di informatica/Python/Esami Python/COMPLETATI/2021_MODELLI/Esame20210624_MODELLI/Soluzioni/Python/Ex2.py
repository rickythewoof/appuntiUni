from tester import tester_fun

import re

def Ex2(file):
    f = open(file,'r',encoding = 'UTF-8')
    ris= set()
    testo=f.read()
    for e in 'abcdefghijklmnopqrstuvwxyz':
        s=e+chr(ord(e)+1)
        pattern=r'\b([a-z])[a-z]*'+s+r'[a-z]*\1\b'
        i=re.finditer(pattern,testo)
        for m in i:
            ris.add(m.group(0))
    return ris

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ['file1.txt'] ,{'ostico', 'astuta', 'abracadabra'})
counter_test_positivi += tester_fun(Ex2, ['file2.txt'] ,{'acaba', 'arsa', 'alma'})
counter_test_positivi += tester_fun(Ex2, ['file3.txt'] ,{'inoltrati', 'aruva'})
counter_test_positivi += tester_fun(Ex2, ['file4.txt'] ,set())
counter_test_positivi += tester_fun(Ex2, ['file5.txt'] ,{'oxyzwo', 'eebcdeee', 'astratta', 'gghhgg'})


print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

counter_test_positivi += tester_fun(Ex2, ['file6.txt'] ,{'nostran', 'peruvp'})
counter_test_positivi += tester_fun(Ex2, ['file7.txt'] ,{'opquanto','rinovar'})
counter_test_positivi += tester_fun(Ex2, ['file8.txt'] ,set())
counter_test_positivi += tester_fun(Ex2, ['file9.txt'] ,{'inughuali', 'aabvoia','ffgfgfgf'})
counter_test_positivi += tester_fun(Ex2, ['file10.txt'] ,{'nellanotten','ostusto'})

          
    
