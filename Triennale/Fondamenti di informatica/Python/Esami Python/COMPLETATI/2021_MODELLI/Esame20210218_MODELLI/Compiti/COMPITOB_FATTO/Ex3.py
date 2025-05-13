def Ex3(file,n):
    sol = {}
    attesa = []
    f = open(file, "r", encoding = "utf-8")
    for riga in f:
        dati = riga.strip().split(",")
        print(dati)
        nome = dati[0]
        tipo = dati[1]
        if tipo == "P" and int(dati[2]) <= n:
            num = int(dati[2])
            sol[nome] = sol.get(nome, 0) + num
            n -= num
            print("prenotazione confermata", num, "POSTI RIMANENTI:", n)
        elif tipo == "P" and int(dati[2]) > n:
            num = int(dati[2])
            print("metto lista d'attesa per persone n:",num)
            attesa.append((nome, num))
        elif tipo == "C" and nome in sol:
            print("rimuovo prenotazione, libero", sol[nome], "posti")
            n += sol[nome]
            sol.pop(nome)
            for i in attesa:
                print("ATTESA:",i)
                num = i[1]
                nome = i[0]
                if num <= n:
                    print("prenotazione confermata da attesa", num, "POSTI RIMANENTI:", n)
                    sol[nome] = sol.get(nome, 0) + num
                    n -= num
                    attesa.remove(i)
    return sol

###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

if __name__ == '__main__':
    from tester import tester_fun

    counter_test_positivi = 0
    total_tests = 10

    # test distribuzione

    counter_test_positivi += tester_fun(Ex3, ['prenotazioni1.csv',10],{'Marco': 4, 'Giorgio': 5})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni1.csv',8],{'Marco': 4, 'Paola': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni2.csv',12],{'Giorgio': 3, 'Andrea': 3, 'Paola': 6})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni2.csv',8],{'Giorgio': 3, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni3.csv',12],{'Paola': 6, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni3.csv',15],{'Paola': 6, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni4.csv',8],{'Andrea': 3, 'Marco': 1, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni4.csv',14],{'Paola': 6, 'Andrea': 3, 'Marco': 1, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni5.csv',12],{'Paola': 6, 'Andrea': 3, 'Michela': 2})
    counter_test_positivi += tester_fun(Ex3, ['prenotazioni5.csv',30],{'Paola': 6, 'Gianni': 7, 'Andrea': 3, 'Michela': 2})
    
    print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
