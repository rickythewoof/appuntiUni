from tester import tester_fun
import re
def B_Ex3(file,diz):
    sol = set()
    pattern = r"\b([0-9]{5,9}) \(([\w]+)\)"
    f = open(file, "r", encoding = "UTF-8").read().strip()
    find = re.finditer(pattern, f, flags = re.MULTILINE)
    for match in find:
        tel = match.group(1)
        luogo = match.group(2)
        print(tel, luogo)
        if luogo in diz:
            sol.add(diz[luogo]+tel)
    return sol
    

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt',{'Francia':'0033','Italia':'0039'}] ,{'0033056784435'})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt',{'Spagna':'0034','Italia':'0039','UK':'0044'}],{'004411234', '003933445567'})
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt',{'Spagna':'0034','Italia':'0039'}] ,{'003933445567', '0034772749270'})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt',{'Germania':'0049','Italia':'0039'}] ,{'003933445566', '0049223345'})
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt',{'Germania':'0049','UK':'0044'}] ,set())

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

