from tester import tester_fun

def C_Ex3(file):
    f=open(file,'r',encoding='UTF-8')
    testo=f.read()
    d={}
    lista=testo.split()
    for m in lista:
        if m.count('@')==1:
            email=m
            j=email.rfind('.') # j è la posizione dell'ultimo punto
            h=email.rfind('@') # h è la posizione della chiocciola
            k=email.rfind('.',0,j) # k è la posizione del penultimo punto
            if h > k:
                k=h # il dominio si trova fra @ ed il .
            dominio=email[k+1:j]
            d[dominio]=d.get(dominio,set())|{email[0:h]}
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

