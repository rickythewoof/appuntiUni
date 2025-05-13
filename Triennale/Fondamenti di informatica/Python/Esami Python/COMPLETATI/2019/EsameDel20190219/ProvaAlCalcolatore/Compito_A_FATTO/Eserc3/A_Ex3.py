from tester import tester_fun

def A_Ex3(file):
    d = {}
    f = open(file, "r", encoding = "UTF-8")
    counter = 1
    ln = f.readline().strip()
    while len(ln) > 0:
        maxChar = []
        maxTime = 0
        for char in ln:
            if char.lower() not in "aeiou ":
                if ln.count(char) > maxTime:
                    maxChar.clear()
                    maxTime = ln.count(char)
                    maxChar.append(char)
                elif ln.count(char) == maxTime and char not in maxChar:
                    maxChar.append(char)
        for char in maxChar:
            d[char] = d.get(char, [])
            d[char].append(counter)
        print(ln, maxChar, maxTime)
        counter += 1
        ln = f.readline().strip()
    return d
                          
###############################################################################

"""DECOMMENTARE le righe successive per eseguire il test"""

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

"""(shortcut da Spyder: evidenziare col mouse le righe seguenti e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(A_Ex3, ['file1.txt'],{'c': [1], 'z': [1], 'n': [2, 3]}  )
counter_test_positivi += tester_fun(A_Ex3, ['file2.txt'],{'c': [1, 5], 'z': [1], 'n': [2, 5], 't': [3, 6], 'l': [4], 's': [4], 'r': [5], 'v': [5], 'd': [5]} )
counter_test_positivi += tester_fun(A_Ex3, ['file3.txt'], {'n': [1], 'l': [2], 't': [3]})
counter_test_positivi += tester_fun(A_Ex3, ['file4.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6], 't': [3], 'p': [5], 'z': [6]} )
counter_test_positivi += tester_fun(A_Ex3, ['file5.txt'],{'n': [1, 4, 5], 'l': [2, 5, 6, 8, 9], 't': [3, 7], 'p': [5], 'z': [6]})

print('La funzione',A_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
