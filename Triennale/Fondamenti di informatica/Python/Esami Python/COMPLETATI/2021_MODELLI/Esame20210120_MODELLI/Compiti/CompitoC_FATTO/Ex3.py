import re

def Ex3(file1,file2):
    piatti = {}
    f1 = open(file1, "r", encoding = "UTF-8")
    ln = f1.readline().strip().split(",")
    while ln != [""]:
        piatto = ln[0]
        costo = int(ln[1])
        disp = int(ln[2])
        piatti[piatto] = [costo, disp]        
        ln = f1.readline().strip().split(",")
    f1.close()
    ordini = {}
    f2 = open(file2, "r", encoding = "UTF-8")
    ln = f2.readline().strip().split(",")
    respinti = set()
    while ln != [""]:
        nome = ln[0]
        print(nome)
        for i in range(1, len(ln)):
            found = re.match(r"(\w+)\:(\d+)", ln[i])
            piatto = found.group(1)
            quanto = int(found.group(2))
            print(piatto, quanto, piatti[piatto][1])
            if nome not in respinti and quanto <= piatti[piatto][1]:
                piatti[piatto][1] -= quanto
                ordini[nome] = ordini.get(nome, 0) + (quanto * piatti[piatto][0])
                print("ORDINI:",ordini[nome])
            else:
                respinti.add(nome)
                ordini[nome] = "respinto"
        ln = f2.readline().strip().split(",")
    return ordini
          
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini1.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66})
    counter_test_positivi += tester_fun(Ex3, ['menu1.csv','ordini2.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini3.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini4.csv'],{'Giorgio': 68, 'Paola': 55, 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto'})
    counter_test_positivi += tester_fun(Ex3, ['menu2.csv','ordini5.csv'],{'Giorgio': 68, 'Paola': 'respinto', 'Francesca': 66, 'Daniele': 36, 'Fabio': 'respinto', 'Carlo': 30})

    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini6.csv'],{'Giorgio': 68, 'Paola': 24, 'Francesca': 54, 'Filippo': 70}) # tutti gli ordini accettati
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini7.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Francesca': 'respinto', 'Filippo': 'respinto'}) # tutti respinti
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini8.csv'],{'Giorgio': 124, 'Paola': 32, 'Francesca': 'respinto', 'Filippo': 40, 'Ernesto': 12, 'Luca': 'respinto'}) # misto
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini9.csv'],{'Giorgio': 'respinto', 'Paola': 'respinto', 'Luca': 'respinto', 'Gino': 30}) # misto
    counter_test_positivi += tester_fun(Ex3, ['menu3.csv','ordini10.csv'],{'Giorgio': 34, 'Paola': 28, 'Luca': 22, 'Gino': 30, 'Ernesto': 'respinto', 'Giovanni': 12, 'Kiara': 8}) # misto

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
