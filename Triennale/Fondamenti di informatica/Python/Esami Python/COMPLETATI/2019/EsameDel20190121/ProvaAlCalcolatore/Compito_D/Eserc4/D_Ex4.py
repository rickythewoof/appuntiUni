from tester import tester_fun

def D_Ex4(file,ore,minuti):
    dict = {}
    f = open(file, "r", encoding="UTF-8")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        
        if len(ln) == 3:
            ora = int(ln[1])
            minuto = int(ln[2])
            dict[ln[0]] = ora*60 + minuto
        else:
            var = int(ln[1][1:])
            if ln[1][0] == "+":
                dict[ln[0]] += var
            else:
                dict[ln[0]] -= var
        ln = f.readline().strip().split(",")
    ris = []
    orario = ore*60 + minuti
    for treno in dict:
        if dict[treno] <= orario:
            ris.append(treno)
    ris.sort()
    return ris
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',12,20] ,['54200','6310'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',12,20] ,['54200', '6310', '79001'])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi1.csv',10,20] ,[])
counter_test_positivi += tester_fun(D_Ex4, ['ritardi2.csv',11,40] ,['54200'] )
counter_test_positivi += tester_fun(D_Ex4, ['ritardi3.csv',14,20] ,['54200', '6310', '6550', '79001'])

print('La funzione',D_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
