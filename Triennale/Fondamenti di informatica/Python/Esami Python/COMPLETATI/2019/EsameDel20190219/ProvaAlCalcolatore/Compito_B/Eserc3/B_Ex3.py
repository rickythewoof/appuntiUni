from tester import tester_fun

def B_Ex3(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    counter = 1
    ln = f.readline().strip()
    while len(ln) > 0:
        minChar = []
        minTime = 100000
        for char in ln:
            if char in "aeiouAEIOU":
                if ln.count(char) < minTime:
                    minChar.clear()
                    minTime = ln.count(char)
                    minChar.append(char)
                elif ln.count(char) == minTime and char not in minChar:
                    minChar.append(char)
        for char in minChar:
            d[char] = d.get(char, [])
            d[char].append(counter)
        print(ln, minChar, minTime)
        counter += 1
        ln = f.readline().strip()
    return d
        
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt'],{'I': [1], 'A': [1], 'e': [1], 'u': [2, 3]})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt'],{'I': [1], 'A': [1], 'e': [1, 5], 'u': [2, 3, 5, 6], 'o': [4, 5]} )
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt'],{'I': [1], 'A': [1], 'u': [1, 2, 3]})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt'],{'I': [1], 'A': [1, 4], 'u': [1, 2, 3, 4, 6], 'o': [5], 'e': [6]} )
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt'],{'I': [1, 7, 8], 'A': [1, 4], 'u': [1, 2, 3, 4, 6, 8, 9], 'o': [5], 'e': [6]})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

