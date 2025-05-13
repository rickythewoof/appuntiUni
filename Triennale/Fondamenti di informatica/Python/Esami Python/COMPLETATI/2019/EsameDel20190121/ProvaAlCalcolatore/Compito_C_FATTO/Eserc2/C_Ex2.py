from tester import tester_fun

def C_Ex2(m):
   sum = 0
   for i in range(len(m)):
      for j in range(len(m)):
         print (i, j, "matrice con elemento:", m[i][j])
         if i != j and m[i][j] != 0:
            return -1
         
      sum += m[i][i]
   return sum
 
###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""
"""(shortcut da Spyder: evidenziare col mouse le righe interessate
   e premere CTRL + 1 per commentare/decommentare)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0],[0,5,0],[0,0,1]]],6)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0],[1,5,0],[0,0,1]]],-1)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0,0],[0,5,0,0],[0,0,1,0],[0,0,0,2]]],8)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0,0],[0,5,0,0],[0,0,1,0],[0,0,1,2]]],-1)
counter_test_positivi += tester_fun(C_Ex2, [[[0,0,0,0],[0,2,0,0],[0,0,-2,0],[0,0,0,-1]]],-1)

print('La funzione',C_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)

