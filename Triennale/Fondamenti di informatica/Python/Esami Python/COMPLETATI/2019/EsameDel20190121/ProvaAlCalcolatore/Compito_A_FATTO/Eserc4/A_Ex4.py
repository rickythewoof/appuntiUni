from distutils.errors import DistutilsExecError
from tester import tester_fun

def A_Ex4(file):
    dict = {}
    sol = []
    f = open(file, "r", encoding = "UTF-8")
    ln = f.readline().strip().split(",")           #skip prima riga di info
    ln = f.readline().strip().split(",")
    while ln != [""]:
        print (ln)
        if ln[1] == "":
            dict[ln[0]] =  dict.get(ln[0], [])
            dict[ln[0]].append(ln[2])
            ln = f.readline().strip().split(",")
        else:
            if ln[2] in dict[ln[1]]:
                print(ln[1], "ha", ln[2], "che ha richiesto", ln[0])
                dict[ln[0]] = dict.get(ln[0], [])
                dict[ln[1]].remove(ln[2])
                dict[ln[0]].append(ln[2])
                ln = f.readline().strip().split(",")
            else:
                print(ln[1], "non ha", ln[2], "che ha richiesto", ln[0])
                ln = f.readline().strip().split(",")
        print(dict)    
    globalLen = 0
    for key in dict:
        localLen = len(dict[key])
        globalLen = max(globalLen, localLen)
    for key in dict:
        if len(dict[key]) == globalLen:
            sol.append(key)
    sol.sort()
    return sol

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['vendite1.csv'] ,['Mario'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite2.csv'] ,['Gianni', 'Mario', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite3.csv'] ,['Gianni', 'Paolo'])
counter_test_positivi += tester_fun(A_Ex4, ['vendite4.csv'] ,['Gianni', 'Maria', 'Paolo'] )
counter_test_positivi += tester_fun(A_Ex4, ['vendite5.csv'] ,['Paolo'] )

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
