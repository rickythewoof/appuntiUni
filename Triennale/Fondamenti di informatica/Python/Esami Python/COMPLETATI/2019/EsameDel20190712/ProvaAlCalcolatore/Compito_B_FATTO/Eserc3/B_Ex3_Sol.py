from tester import tester_fun

def B_Ex3(file):
      d = {}
      f = open(file,encoding = 'UTF-8')
      testo = f.read()
      l=testo.split()
      for i in range(len(l)): # converto gli elementi in interi
          l[i]=int(l[i])
      for i in range(0,len(l)-1):
           if l[i] not in d:
              d[l[i]] = [l[i+1]]
           elif l[i+1] not in d[l[i]]:
              d[l[i]].append(l[i+1])
      if len(l) > 0 and l[-1] not in d:
          d[l[-1]]=[]
      for e in d:
          d[e].sort()
      return d

                          
###############################################################################

"""NON MODIFICARE IL CODICE (codice di test della funzione)"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex3, ['file1.txt'],{1: [3], 3: [12, 24], 24: [2, 3, 5], 12: [8, 24], 8: [7, 8], 7: [3], 2: [24], 5: []})
counter_test_positivi += tester_fun(B_Ex3, ['file2.txt'],{1: [1]})
counter_test_positivi += tester_fun(B_Ex3, ['file3.txt'],{0: [1], 1: [2], 2: [3], 3: [4], 4: [5], 5: [6], 6: [7], 7: [8], 8: [9], 9: []})
counter_test_positivi += tester_fun(B_Ex3, ['file4.txt'],{-11: [3, 12], 12: [-11], 3: [4], 4: [3]} )
counter_test_positivi += tester_fun(B_Ex3, ['file5.txt'],{24: [1, 3], 3: [12, 24], 12: [8, 24], 8: [7, 8], 7: [3], 1: [1]})

print('La funzione',B_Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
