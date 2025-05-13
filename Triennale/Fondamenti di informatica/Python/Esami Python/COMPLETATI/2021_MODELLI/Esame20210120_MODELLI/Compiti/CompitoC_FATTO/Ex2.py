import re
def Ex2(i,file):
    d = {}
    for num in i:
        d[num] = 0
    f = open(file, "r", encoding = "UTF-8").read().strip()
    pattern = r'([+]|[0]{2})(\d{1,3})-?\d{3}-?\d{5}'
    find = re.finditer(pattern, f, flags = re.MULTILINE)
    for match in find:
        print ("match:",match.group())
        prefix = match.group(2)
        print(prefix)
        if prefix in i:
            d[prefix] += 1
    return d
                           
            
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, [{'39','351','34'},'testo1.txt'],{'39':2,'351':1,'34':0})
    counter_test_positivi += tester_fun(Ex2, [{'1','351'},'testo2.txt'],{'1':3,'351':1})
    counter_test_positivi += tester_fun(Ex2, [{'39','351','34','1'},'testo3.txt'],{'1':0,'351':0,'34':0,'39':2})
    counter_test_positivi += tester_fun(Ex2, [{'351','34'},'testo3.txt'],{'351':0,'34':0})
    counter_test_positivi += tester_fun(Ex2, [{'7','1'},'testo4.txt'],{'7':2,'1':2})

    counter_test_positivi += tester_fun(Ex2, [{'39','44','661','9'},'testo6.txt'],{'661': 1, '39': 2, '9': 1, '44': 2}) # tutti corretti e tutti esportare
    counter_test_positivi += tester_fun(Ex2, [{'44','661'},'testo6.txt'],{'661': 1, '44': 2}) # tutti corretti ma solo alcuni da esportare
    counter_test_positivi += tester_fun(Ex2, [{'39','1','22'},'testo7.txt'],{'39': 0, '1': 0,'22':0}) # tutti non corretti
    counter_test_positivi += tester_fun(Ex2, [set(),'testo6.txt'],{}) # insieme vuoto
    counter_test_positivi += tester_fun(Ex2, [{'66','492'},'testo8.txt'],{'492': 1, '66': 2}) # generico

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
