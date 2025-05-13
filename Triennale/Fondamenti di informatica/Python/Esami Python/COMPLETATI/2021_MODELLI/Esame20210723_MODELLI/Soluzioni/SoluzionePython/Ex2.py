from tester import tester_fun

def Ex2(s):
    i=0
    massimo=0
    while i < len(s):
        if s[i]!='a':
            i=i+1
        else:
            contaSequenza=0
            while i < len(s) and s[i]=='a':
                contaSequenza=contaSequenza+1
                i=i+1
            if contaSequenza>massimo:
                massimo=contaSequenza
    return massimo

## Soluzione alternativa che fa uso di espressioni regolari
##
##import re
##
##def Ex2(s):
##    pattern='a+'
##    it=re.finditer('a+',s)
##    massimo=0
##    for m in it:
##       sequenza_di_a=m.group()
##       if len(sequenza_di_a)>massimo:
##           massimo=len(sequenza_di_a)
##    return massimo

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex2, ['dfgaadfaaaffgeaf'] ,3)
counter_test_positivi += tester_fun(Ex2, ['serftghno'] ,0)
counter_test_positivi += tester_fun(Ex2, ['portaala'] ,2)
counter_test_positivi += tester_fun(Ex2, ['aaaaaaaaaa'] ,10)
counter_test_positivi += tester_fun(Ex2, ['aaaabbaaaabba'] ,4)

print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

counter_test_positivi += tester_fun(Ex2, ['gaaaadfaffaageaaf'] ,4)
counter_test_positivi += tester_fun(Ex2, ['serfaatghno'] ,2)
counter_test_positivi += tester_fun(Ex2, ['poraallaaala'] ,3)
counter_test_positivi += tester_fun(Ex2, ['aaaaabaaaaa'] ,5)
counter_test_positivi += tester_fun(Ex2, ['a'] ,1)
           
    
