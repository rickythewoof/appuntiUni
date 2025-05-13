def Ex1(l):
    risultato=''
    for sottolista in l:
        parola_unica=''
        for parola in sottolista:
            parola_unica+=parola
        massimo=0
        for carattere in parola_unica:
            if parola_unica.count(carattere)>massimo:
                massimo=parola_unica.count(carattere)
                max_carattere=carattere
        risultato+=max_carattere
    return risultato
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex1, [[['amare','mare','fermata'], ['accordare','fare','dire']]],"ar")
    counter_test_positivi += tester_fun(Ex1, [[["arciere","pippo","pluto"],["minnie","paperi"],["io","valle"]]],"pil")
    counter_test_positivi += tester_fun(Ex1, [[["arciere","pompiere","bere"]]],"e")
    counter_test_positivi += tester_fun(Ex1, [[["a"],["b"],["c"],["d"]]],"abcd")
    counter_test_positivi += tester_fun(Ex1, [[["mentolo","mentore","o"],["accidentaccio"],["assassino"]]],"ocs")

    # test aggiuntivi

    counter_test_positivi += tester_fun(Ex1, [[['o']]],"o") # un solo carattere ed una sola lista
    counter_test_positivi += tester_fun(Ex1, [[['ora','orco','otranto']]],"o") # una sola lista
    counter_test_positivi += tester_fun(Ex1, [[['anna','anita','alessandra'],['abcd','eeee']]],"ae") # più liste
    counter_test_positivi += tester_fun(Ex1, [[['a','bcd','bef'],['a','ab','abc','aeee']]],"ba") # più liste, un carattere appare in più stringhe ma ha più occorrenze in una sola stringa
    counter_test_positivi += tester_fun(Ex1, [[['a','bcd','bef'],['a','ab','abc','eeee']]],"be") # più liste, un carattere appare in più stringhe ma ha più occorrenze in una sola stringa

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
