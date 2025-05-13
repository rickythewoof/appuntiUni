def distanza(s1,s2):
    dist = abs(len(s1)-len(s2))
    for i in range(min(len(s1),len(s2))):
        if s1[i] != s2[i]:
            dist += 1
    return dist

def Ex2(i,file):
    diz = {}
    parole = open(file).read().split()
    for elem in i:
        diz[elem]=set()
        if len(parole) != 0:
            mindist = distanza(elem,parole[0])
            for parola in parole:
                dist = distanza(elem,parola)
                if dist < mindist:
                    diz[elem] = {parola}
                    mindist = dist
                elif dist == mindist:
                    diz[elem].add(parola)
    return diz
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex2, [{'casa','palla','mela'},'testo1.txt'],{'mela': {'nel'}, 'casa': {'la', 'casina'}, 'palla': {'molla', 'bella'}})
    counter_test_positivi += tester_fun(Ex2, [{'cassa','palline','malta'},'testo1.txt'],{'palline': {'pallone'}, 'malta': {'molla'}, 'cassa': {'casina'}})
    counter_test_positivi += tester_fun(Ex2, [{'casale','pelle'},'testo1.txt'],{'pelle': {'bella'}, 'casale': {'casina'}})
    counter_test_positivi += tester_fun(Ex2, [{'casale','pelle'},'testo2.txt'],{'pelle': {'bella'}, 'casale': {'casina', 'carine', 'case'}})
    counter_test_positivi += tester_fun(Ex2, [{'cena'},'testo2.txt'],{'cena': {'le', 'sono', 'case', 'nel', 'non'}})

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex2, [{'casa','mela'},'testo3.txt'],{'mela': {'bella', 'casa', 'ma', 'le', 'molto', 'mi'}, 'casa': {'casa'}})
    counter_test_positivi += tester_fun(Ex2, [{'cassa','palline','malta'},'testo3.txt'],{'malta': {'molto'}, 'palline': {'bella'}, 'cassa': {'casa', 'case'}})
    counter_test_positivi += tester_fun(Ex2, [{'casale','pelle'},'testo3.txt'],{'pelle': {'bella'}, 'casale': {'casa'}})
    counter_test_positivi += tester_fun(Ex2, [{'casa','pelle'},'testo4.txt'],{'casa': {'casa'}, 'pelle': {'delle', 'belle'}})
    counter_test_positivi += tester_fun(Ex2, [{'cena'},'testo4.txt'],{'cena': {'cena'}})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
