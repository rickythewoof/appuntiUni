def Ex2(i,file):
    diff = {}
    sol = {}
    for word in i:
        diff[word] = 10000
        sol[word] = set()
    f = open(file, "r", encoding = "UTF-8")
    for ln in f:
        words = ln.strip().split(" ")
        for word in words:
            for key in diff:
                differenza = abs(len(word) - len(key))
                for j in range(min(len(word), len(key))):
                    if word[j] != key[j]:
                        differenza += 1
                if differenza < diff[key]:
                    diff[key] = differenza
                    sol[key] = set()
                    sol[key].add(word)
                elif differenza == diff[key]:
                    sol[key].add(word)
    return sol
    
            
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
    counter_test_positivi += tester_fun(Ex2, [{'casa','mela'},'testo3.txt'],{'mela': {'bella', 'casa', 'ma', 'le', 'molto', 'mi'}, 'casa': {'casa'}})
    counter_test_positivi += tester_fun(Ex2, [{'cassa','palline','malta'},'testo3.txt'],{'malta': {'molto'}, 'palline': {'bella'}, 'cassa': {'casa', 'case'}})
    counter_test_positivi += tester_fun(Ex2, [{'casale','pelle'},'testo3.txt'],{'pelle': {'bella'}, 'casale': {'casa'}})
    counter_test_positivi += tester_fun(Ex2, [{'casa','pelle'},'testo4.txt'],{'casa': {'casa'}, 'pelle': {'delle', 'belle'}})
    counter_test_positivi += tester_fun(Ex2, [{'cena'},'testo4.txt'],{'cena': {'cena'}})

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
