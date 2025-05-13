import re

def Ex2(file):
    f = open(file, "r", encoding = "UTF-8").read()
    d = {}
    pattern = r"mailto:(\w+)@\w+\.(\w{2,})"
    find = re.finditer(pattern, f, flags = re.MULTILINE)
    for match in find:
        nome = match.group(1)
        suff = match.group(2)
        if suff not in ["org","com","net"]:
            d[suff] = d.get(suff,[])
            d[suff].append(nome)
            d[suff].sort()
    return d
    
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 5

    counter_test_positivi += tester_fun(Ex2, ['testo1.txt'],{'it':['domenico','maria'],'es':['marco']})
    counter_test_positivi += tester_fun(Ex2, ['testo2.txt'],{'it': ['anna','marco']})
    counter_test_positivi += tester_fun(Ex2, ['testo3.txt'],{'usa':['dad','mom'], 'it':['giovanna','giovanna','marco']})
    counter_test_positivi += tester_fun(Ex2, ['testo4.txt'],{})
    counter_test_positivi += tester_fun(Ex2, ['testo5.txt'],{'uk':['boris','elizabeth'], 'it':['sergio']})

    counter_test_positivi += tester_fun(Ex2, ['testo6.txt'],{'it': ['persona'], 'fr': ['unnome'], 'euro': ['paolapozzopieno'], 'zzz': ['angelo']}) # tutti corretti senza com net ed org, un solo nome per nazione, spazio prima e dopo ogni indirizzo e-mail
    counter_test_positivi += tester_fun(Ex2, ['testo7.txt'],{}) # nessun indirizzo corretto
    counter_test_positivi += tester_fun(Ex2, ['testo8.txt'],{}) # indirizzi corretti ma tutti da escludere
    counter_test_positivi += tester_fun(Ex2, ['testo9.txt'],{'gk': ['aprimonome', 'primonome'], 'gkq': ['secondonome', 'zsecondonome'], 'it': ['primo1']}) # indirizzi corretti, non corretti e da escludere
    counter_test_positivi += tester_fun(Ex2, ['testo10.txt'],{'gk': ['aprimo_nome', 'primo_nome'], 'gkq': ['secondo_nome', 'zsecondo_nome'], 'it': ['primo1']}) # punteggiatura utilizzata. indirizzi corretti, non corretti e da escludere

    print('La funzione',Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
