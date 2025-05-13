from ast import Pass
from tester import tester_fun

def B_Ex4(file):
    stazioni = {}
    f = open(file, "r", encoding= "UTF-8")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        print(ln)
        treno = ln[0]
        stazione = ln[1]
        ap = ln[2]
        stazioni[stazione] = stazioni.get(stazione,[])
        if ap == "P":
            stazioni[stazione].append(treno)
            stazioni[stazione].sort()
        elif ap == "A":
            if treno in stazioni[stazione]:
                stazioni[stazione].remove(treno)
        ln = f.readline().strip().split(",")
    return (stazioni)

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['treni1.csv'],{'Termini': ['T72', 'T81'], 'Tiburtina': ['T61'], 'Trastevere': []})
counter_test_positivi += tester_fun(B_Ex4, ['treni2.csv'],{'Termini': ['T72', 'T81'], 'Tiburtina': ['T61'], 'Trastevere': ['T53']})
counter_test_positivi += tester_fun(B_Ex4, ['treni3.csv'],{'Termini': ['T72'], 'Tiburtina': ['T61'], 'Trastevere': ['T53', 'T81']})
counter_test_positivi += tester_fun(B_Ex4, ['treni4.csv'],{'Termini': ['T72'], 'Tiburtina': ['T53', 'T61'], 'Trastevere': ['T81']})
counter_test_positivi += tester_fun(B_Ex4, ['treni5.csv'],{'Termini': ['T12', 'T72'], 'Tiburtina': ['T53', 'T61'], 'Trastevere': ['T81'], 'SanPietro': []})

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
