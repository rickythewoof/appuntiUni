def Ex3(file1,file2):
    menu = {}
    diz = {}
    f1 = open(file1,'r',encoding='UTF-8')
    for riga in f1:
        riga = riga.strip().split(',')
        piatto = riga[0]
        costo = int(riga[1])
        disp = int(riga[2])
        menu[piatto] = [costo,disp]
    f1.close()
    f2 = open(file2,'r',encoding='UTF-8')
    for riga in f2:
        riga = riga.strip().split(',')
        cliente = riga[0]
        ordini = riga[1:]
        ok = True
        costo = 0
        for ordine in ordini:
            ordine = ordine.split(':')
            piatto = ordine[0]
            quan = int(ordine[1])
            if quan > menu[piatto][1]:
                ok = False
        if not ok:
            diz[cliente] = 'respinto'
        else:
            for ordine in ordini:
                ordine = ordine.split(':')
                piatto = ordine[0]
                quan = int(ordine[1])
                costo += menu[piatto][0]*quan
                menu[piatto][1] -= quan
                diz[cliente] = costo
    return diz

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini1.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66})
    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini2.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini3.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini4.csv'],{'Giorgio': 68, 'Paola': 55, 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini5.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto', 'Carlo': 30})

    # test aggiuntivi
    
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini6.csv'],{'Giorgio': 68, 'Paola': 24, 'Francesca': 54, 'Filippo': 70}) # tutti gli ordini accettati
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini7.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Francesca': 'respinto', 'Filippo': 'respinto'}) # tutti respinti
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini8.csv'],{'Giorgio': 124, 'Paola': 32, 'Francesca': 'respinto', 'Filippo': 40, 'Ernesto': 12, 'Luca': 'respinto'}) # misto
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini9.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Luca': 'respinto', 'Gino': 30}) # misto
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini10.csv'],{'Giorgio': 34, 'Paola': 28, 'Luca': 22, 'Gino': 30, 'Ernesto': 'respinto', 'Giovanni': 12, 'Kiara': 8}) # misto

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
