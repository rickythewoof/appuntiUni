import re

def Ex2(file):
    sol =  {}
    f = open (file, "r", encoding = "utf-8").read().strip()
    pattern = r"(\d{3})-?(\d{2})-?(\d{3})-?(\d{4})-?(\d)"
    find = re.finditer(pattern, f, flags = re.MULTILINE)
    for match  in find:
        print (match.group())
        num = ""
        test = 0
        for i in range(1,6):
            num += match.group(i)
        for charIndex in range(len(num)):
            if (charIndex+1)%2 == 1:
                test += int(num[charIndex])
            else:
                test +=  3*int(num[charIndex])
        if  test % 10 == 0:
           sol[match.group(2)] = sol.get(match.group(2),0) 
           sol[match.group(2)] += 1
    return sol
    
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{'88': 1, '78': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{'88': 2, '78': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{'88': 2, '78': 2, '15': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{'88': 2, '78': 2, '15': 1, '05': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{'88': 1, '78': 1, '15': 1, '05': 1})
    counter_test_positivi += tester_fun(Ex2, ['testo6.txt'],{'88': 2, '20': 1, '07': 1, '18': 1}) # tutti i codici sono validi
    counter_test_positivi += tester_fun(Ex2, ['testo7.txt'],{}) # nessun codice è valido
    counter_test_positivi += tester_fun(Ex2, ['testo8.txt'],{'88': 2, '14': 1}) # mix codici validi e non
    counter_test_positivi += tester_fun(Ex2, ['testo9.txt'],{}) # testo vuoto
    counter_test_positivi += tester_fun(Ex2, ['testo10.txt'],{'88': 2, '20': 1, '07': 1}) # validi tutti con i trattini

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
