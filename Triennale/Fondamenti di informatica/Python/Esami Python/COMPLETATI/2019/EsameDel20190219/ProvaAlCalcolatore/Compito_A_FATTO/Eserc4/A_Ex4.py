from tester import tester_fun

def A_Ex4(file,n):
    d = {}
    sol = [] 
    f = open(file, "r", encoding = "UTF-8")
    ln = f.readline().strip().split(",")    
    ln = f.readline().strip().split(",") 
    while ln != [""]:
        partenza = ln[0]
        arrivo = ln[1]
        oraPartenza = int(ln[2])
        oraArrivo = int(ln[3])
        if partenza == "Anycity":
            d[arrivo] = d.get(arrivo, [0,0])
            d[arrivo][0] = oraArrivo
        elif arrivo == "Anycity":
            d[partenza] = d.get(partenza, [0,0])
            d[partenza][1] = oraPartenza
        ln = f.readline().strip().split(",") 
    print(d)
    for posti in d:
        diff = d[posti][1]-d[posti][0]
        print(posti, diff)
        if 0 < diff < 23 and diff >= n:
            sol.append(posti)
    return sol           

###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['voli1.csv',3],['Londra','Parigi'])
counter_test_positivi += tester_fun(A_Ex4, ['voli1.csv',5],['Parigi'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',4],['Londra', 'Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',7],['Parigi', 'Stoccolma'])
counter_test_positivi += tester_fun(A_Ex4, ['voli2.csv',11],[])

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
