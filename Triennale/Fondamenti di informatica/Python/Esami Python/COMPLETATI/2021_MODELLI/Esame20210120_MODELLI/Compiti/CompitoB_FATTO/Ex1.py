def Ex1(l):
    d = {}
    sol = ""
    for i in range(len(l)):
        d[i] = {}
        maxCount = 0
        maxChar = ""
        for string in l[i]:
            for char in string:
                d[i][char] = d[i].get(char, 0)
                d[i][char] += 1
        for char in d[i]:
            if d[i][char] > maxCount:
                maxCount = d[i][char]
                maxChar = char
        print(d[i], maxCount, maxChar)
        sol += maxChar
        print(sol)
    return sol
         
            

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex1, [[['amare','mare','fermata'], ['accordare','fare','dire']]],"ar")
    counter_test_positivi += tester_fun(Ex1, [[["arciere","pippo","pluto"],["minnie","paperi"],["io","valle"]]],"pil")
    counter_test_positivi += tester_fun(Ex1, [[["arciere","pompiere","bere"]]],"e")
    counter_test_positivi += tester_fun(Ex1, [[["a"],["b"],["c"],["d"]]],"abcd")
    counter_test_positivi += tester_fun(Ex1, [[["mentolo","mentore","o"],["accidentaccio"],["assassino"]]],"ocs")

    counter_test_positivi += tester_fun(Ex1, [[['o']]],"o") # un solo carattere ed una sola lista
    counter_test_positivi += tester_fun(Ex1, [[['ora','orco','otranto']]],"o") # una sola lista
    counter_test_positivi += tester_fun(Ex1, [[['anna','anita','alessandra'],['abcd','eeee']]],"ae") # più liste
    counter_test_positivi += tester_fun(Ex1, [[['a','bcd','bef'],['a','ab','abc','aeee']]],"ba") # più liste, un carattere appare in più stringhe ma ha più occorrenze in una sola stringa
    counter_test_positivi += tester_fun(Ex1, [[['a','bcd','bef'],['a','ab','abc','eeee']]],"be") # più liste, un carattere appare in più stringhe ma ha più occorrenze in una sola stringa

    print('La funzione',Ex1.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
