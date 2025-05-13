from tester import tester_fun

def B_Ex4(file):
            

                
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex4, ['performance1.csv'],{'Mario': [5, 8], 'Marco': [3, 1], 'Anna': [5, 1, 8], 'Aldo': [1, 3], 'Antonio': [4, 10]} )
counter_test_positivi += tester_fun(B_Ex4, ['performance2.csv'],{'Mario': [5, 9], 'Marco': [4, 14, 17], 'Anna': [5, 1, 9, 14, 17], 'Aldo': [1, 3], 'Antonio': [4, 12, 14]})
counter_test_positivi += tester_fun(B_Ex4, ['performance3.csv'],{'Mario': [5, 9], 'Marco': [4, 14, 17], 'Anna': [6, 20], 'Aldo': [1, 3], 'Antonio': [4, 12, 14], 'Gianni': [1, 20]})
counter_test_positivi += tester_fun(B_Ex4, ['performance4.csv'],{'Mario': [5, 9], 'Marco': [5, 27, 28], 'Anna': [6, 20], 'Aldo': [1, 3], 'Antonio': [4, 12, 14], 'Gianni': [1, 20, 25]})
counter_test_positivi += tester_fun(B_Ex4, ['performance5.csv'],{'Mario': [5, 9], 'Marco': [6, 30], 'Anna': [6, 20], 'Aldo': [1, 3], 'Antonio': [4, 12, 14], 'Gianni': [1, 20, 25]})

print('La funzione',B_Ex4.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
