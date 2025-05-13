from tester import tester_fun

def A_Ex3(l):
    massimo=0
    lista=[]
    for e in l:
        cont=0
        for c in e:
            if c.isupper():
                cont+=1
        if cont>massimo:
            massimo=cont
            lista=[e]
        elif cont==massimo:
            lista.append(e)
    i=0
    while i<len(l):
        if l[i] in lista:
            l.remove(l[i])
        else:
            i = i+1
    return l


###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, [["piPPo", "pippo","PLuto","Pippo"]],["pippo","Pippo"])
counter_test_positivi += tester_fun(A_Ex3, [["Maria", "mamma","Monica"]] ,["mamma"])
counter_test_positivi += tester_fun(A_Ex3, [["","questa è una stringa"]] ,[])
counter_test_positivi += tester_fun(A_Ex3, [["Ciao","ciao"]] ,["ciao"])
counter_test_positivi += tester_fun(A_Ex3, [["gennaio","FEbbraio","Marzo"]] ,["gennaio","Marzo"])

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
