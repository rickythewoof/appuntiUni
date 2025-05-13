def Ex3(file):
    d = {}
    
    f = open(file, "r",encoding =  "UTF-8")
    for ln in f:
        ln = ln.strip().split(",")
        nome =  ln[0]
        caratt = ln[1]
        val = int(ln[2])
        if nome not in d:
            d[nome] = {caratt:val}
        elif caratt not in  d[nome]:
            d[nome][caratt] = val
        else:
            d[nome][caratt] += val
    f.close()
    maxVal = val
    maxNome = nome
    maxCaratt = caratt
    for nome in d:
        for  char in d[nome]:
            if d[nome][char] > maxVal:
                maxVal = d[nome][char]
                maxNome = nome
                maxCaratt = char
    return (maxNome, maxCaratt)
                

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex3, ['file1.csv'],('Marco', 'soldi'))
    counter_test_positivi += tester_fun(Ex3, ['file2.csv'],('Paolo', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file3.csv'],('Marco', 'soldi'))
    counter_test_positivi += tester_fun(Ex3, ['file4.csv'],('Anna', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file5.csv'],('Paolo', 'punti'))
    counter_test_positivi += tester_fun(Ex3, ['file6.csv'],('Anna', 'soldi')) # vi è una sola caratteristica
    counter_test_positivi += tester_fun(Ex3, ['file7.csv'],('Anna', 'punti')) # vi sono due caratteristiche
    counter_test_positivi += tester_fun(Ex3, ['file8.csv'],('Marco', 'soldi')) # valori tutti negativi
    counter_test_positivi += tester_fun(Ex3, ['file9.csv'],('Marco', 'soldi')) # risultato finale = 0
    counter_test_positivi += tester_fun(Ex3, ['file10.csv'],('Anna', 'bonus')) # valori tutti positivi


    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
