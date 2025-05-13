def Ex3(l,file):
    d = {}
    f = open(file, "r", encoding="UTF-8")
    ln = f.readline().strip().split(",")
    ln = f.readline().strip().split(",")
    while ln != [""]:
        g1 = ln[0]
        g2 = ln[1]
        punto1 = ln[2]
        punto2 = ln[3]
        score1 = l.index(punto1)
        score2 = l.index(punto2)
        if score1 > score2:
            d[g1] = d.get(g1, 0) + 1
        elif score1 < score2:
            d[g2] = d.get(g2, 0) + 1
        ln = f.readline().strip().split(",")
    max = 0
    ris = []
    for nome in d:
        if d[nome] > max:
            ris.clear()
            ris.append(nome)
            max = d[nome]
        elif d[nome] == max:
            ris.append(nome)
    ris.sort()
    return ris
    

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file1.csv'],['Aldo','Marco'])
    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file2.csv'],['Anna'])
    counter_test_positivi += tester_fun(Ex3, [['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci'],'file3.csv'],['Anna','Franco','Olga'])
    counter_test_positivi += tester_fun(Ex3, [['zero','uno','due','tre','quattro','cinque','sei','sette','otto','nove','dieci'],'file4.csv'],['Matteo'])
    counter_test_positivi += tester_fun(Ex3, [['sballato','mezzo','uno','uno e mezzo','due','due e mezzo','tre','tre e mezzo','quattro', 'quattro e mezzo','cinque','cinque e mezzo','sei','sei e mezzo','sette','sette e mezzo'],'file5.csv'],['Frank','Olga'])

    counter_test_positivi += tester_fun(Ex3, [['coppia','doppiacoppia','tris','scala','full','poker','colore','scalareale'],'file6.csv'],['Aldo','Marco']) # due giocatori che vincono entrambi il massimo numero di volte
    counter_test_positivi += tester_fun(Ex3, [['uno','due','tre'],'file7.csv'],['Massimo']) # una sola partita
    counter_test_positivi += tester_fun(Ex3, [['A','B','C','D'],'file8.csv'],['Luca']) # un solo vincitore
    counter_test_positivi += tester_fun(Ex3, [['giu','su'],'file9.csv'],['Adele', 'Ernesto', 'Franco', 'Mimmo']) # tutti vincitori con una vittoria
    counter_test_positivi += tester_fun(Ex3, [['a','b','c','d','e'],'file10.csv'],['Carlo', 'Enrico']) # due vincitori su diversi

    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
