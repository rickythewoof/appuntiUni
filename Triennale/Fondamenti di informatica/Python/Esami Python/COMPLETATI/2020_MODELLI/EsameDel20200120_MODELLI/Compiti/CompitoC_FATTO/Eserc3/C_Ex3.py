from tester import tester_fun
import re

def C_Ex3(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8").read()
    regex = r"(\w+\.?\w*)@(\w+\.)*(\w+)\.\w+"
    find = re.finditer(regex, f, flags=re.MULTILINE)
    for match in find:
        print(match.group())
        nome = match.group(1)
        dominio = match.group(3)
        d[dominio] = d.get(dominio, set())
        d[dominio].add(nome)
    return d
    
    
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex3, ['file1.txt'] ,{'gmail':{'marco.marco'},'uniroma1':{'anna'}})
counter_test_positivi += tester_fun(C_Ex3, ['file2.txt'] ,{'gmail':{'alberto','marco.marco'},'tiscali':{'anna'},'uniroma1':{'alberto'}})
counter_test_positivi += tester_fun(C_Ex3, ['file3.txt'] ,{'gmail':{'marco.rossi'},'yahoo':{'rossi'},'apple':{'giorgio.bianchi','marco.rossi','rossi'},'microsoft':{'bianchi'},'ping':{'ferro','paolo.ferro'}})
counter_test_positivi += tester_fun(C_Ex3, ['file4.txt'] ,{'uniroma1':{'marco.rossi','giorgio.bianchi'},'yahoo':{'rossi'},'tuwien':{'bianchi'}})
counter_test_positivi += tester_fun(C_Ex3, ['file5.txt'] ,{'uniroma1':{'marco.rossi','neri','verdi'}})

print('La funzione',C_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

