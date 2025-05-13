from tester import tester_fun

def A_Ex4(file1,file2):
    rank = []
    vittorie = {}
    f = open(file1, "r")
    for riga in f:
        rank.append(riga.strip())
    f.close()
    print(rank)
    f = open(file2, "r")
    for riga in f:
        game = riga.strip().split(",")
        g1 = game[0]
        g2 = game[1]
        set1 = game[2]
        set2 = game[3]
        print (game)
        if set1 > set2:
            print("vittoria di", g1, "contro", g2)
            if rank.index(g1) < rank.index(g2) and g1 not in vittorie:
                print("creo dizionario, ora puà aggiungere chiunque")
                vittorie[g1] = vittorie.get(g1, set())
            if g1 in vittorie:
                vittorie[g1].add(g2)
        elif set1 < set2:
            print("vittoria di", g2, "contro", g1)
            if rank.index(g2) < rank.index(g1) and g2 not in vittorie:
                print("creo dizionario, ora puà aggiungere chiunque")
                vittorie[g2] = vittorie.get(g2, set())
            if g2 in vittorie:
                vittorie[g2].add(g1)
        print(vittorie)            
    return vittorie
            
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri1.csv'],{'Federer':{ 'Medvedev', 'Djokovic'}, 'Nadal':{ 'Federer', 'Djokovic'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri2.csv'],{'Federer':{ 'Medvedev', 'Thiem','Djokovic'},'Nadal':{ 'Federer', 'Djokovic'},'Thiem':{'Nadal'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking1.csv','incontri3.csv'],{'Medvedev':{ 'Federer'},'Thiem':{ 'Nadal'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking2.csv','incontri4.csv'],{'Paperoga':{ 'Paperino'}})
counter_test_positivi += tester_fun(A_Ex4, ['ranking2.csv','incontri5.csv'],{'Paperoga':{ 'Pippo','Paperino'},'Pippo':{'Topolino','Paperoga'}})

print('La funzione',A_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
