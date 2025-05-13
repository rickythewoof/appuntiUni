def Ex2(file):
    f=open(file,'r',encoding='UTF-8')
    contaRighe=1
    ris={}
    for riga in f:
        riga=riga.split()
        for elem in riga:
            if elem.isdigit():
                elem=int(elem)
                if elem in ris:
                    if contaRighe not in ris[elem]:
                        ris[elem]=[contaRighe]+ris[elem]
                        #ris[elem].append(contaRighe) # alternativa
                        #ris.sort(reverse)
                if elem not in ris:
                    ris[elem]=[contaRighe]
        contaRighe+=1
    return ris   
    
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{11:[1],3:[3,2,1],1:[2],111:[3]})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{1:[2,1],2:[3]})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{1:[1],11:[3],22:[4]})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{22:[1],11:[3,2],1:[4],2:[4]})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{222:[5,4,1],1000:[4,3,2],22:[4]})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, ['testo6.txt'],{13:[3,1],4:[3,2,1],3:[2]}) 
    counter_test_positivi += tester_fun(Ex2, ['testo7.txt'],{1:[3,2],3:[1]}) 
    counter_test_positivi += tester_fun(Ex2, ['testo8.txt'],{3:[1],1:[2],22:[3]}) 
    counter_test_positivi += tester_fun(Ex2, ['testo9.txt'],{11:[4,1],12:[2],10:[3],1:[4]}) 
    counter_test_positivi += tester_fun(Ex2, ['testo10.txt'],{})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
