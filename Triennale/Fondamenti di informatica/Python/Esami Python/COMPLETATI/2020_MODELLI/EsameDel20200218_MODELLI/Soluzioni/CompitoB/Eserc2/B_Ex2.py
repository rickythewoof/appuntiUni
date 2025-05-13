from tester import tester_fun

def sommaContorno(M,i,j):
    somma=0
    for h in range(i-1,i+2):
        for k in range(j-1,j+2):
            if h != i or k != j:
                somma+=M[h][k]    
    return somma

def B_Ex2(M):
    n=len(M)
    m=len(M[0])
    minimo=sommaContorno(M,1,1) # per ipotesi l'elemento in questa posizione esiste sempre
    massimo=sommaContorno(M,1,1)
    for i in range(1,n-1):
        for j in range(1,m-1):
            if sommaContorno(M,i,j)<minimo:
                minimo=sommaContorno(M,i,j)
            if sommaContorno(M,i,j)>massimo:
                massimo=sommaContorno(M,i,j)
    return (minimo,massimo)
    

###############################################################################

"""TEST FUNZIONE, NON MODIFICARE"""
"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(B_Ex2, [[[-3,5,8,4],[0,7,6,3],[0,5,3,8],[1,2,0,1]]],(19,43))
counter_test_positivi += tester_fun(B_Ex2, [[[0,0,0,0],[0,0,0,0],[0,0,0,0]]], (0,0))
counter_test_positivi += tester_fun(B_Ex2, [[[-1,3,12],[6,8,9],[15,-10,8]]], (42,42))
counter_test_positivi += tester_fun(B_Ex2, [[[-1,3,12],[6,8,9],[15,-10,8],[8,6,7]]], (42,67))
counter_test_positivi += tester_fun(B_Ex2, [[[0,7,6],[0,6,3],[3,5,8],[0,0,0],[-3,-4,-15]]], (-6,32))

print('La funzione',B_Ex2.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
