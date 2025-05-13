from tester import tester_fun

def Ex3(p,a,file):        
    part = {}
    arr = {}
    minTime = 1000
    f = open(file, "r", encoding = "UTF-8")
    for ln in f:
        dati = ln.strip().split(",")
        partenza = dati[0]
        arrivo = dati[1]
        tempo = int(dati[2])
        part[partenza] = part.get(partenza,{arrivo:tempo}) 
        arr[arrivo] = arr.get(arrivo,{partenza:tempo})
        part[partenza][arrivo] = part[partenza].get(arrivo, tempo)
        arr[arrivo][partenza] = arr[arrivo].get(partenza, tempo)
        part[partenza][arrivo] = min(tempo, part[partenza][arrivo])
        arr[arrivo][partenza] = min(tempo, arr[arrivo][partenza])
    if p not in part or a not in arr:
        return "Impossibile"    
    elif a in part[p]:
        return part[p][a]
    else:
        for volo in part[p]:
            durataVolo = part[p][volo]
            if  volo in arr[a]:
                print(p, volo, a)
                durataVolo += arr[a][volo]
                minTime = min(durataVolo, minTime)
            else:
                pass
    if minTime >= 1000:
        return "Impossibile"
    return minTime            

###############################################################################

"""NON MODIFICARE IL SEGUENTE CODICE (codice di test della funzione)"""

"""SE NON VOLETE ESEGUIRE UN TEST COMMENTATE LA RIGA RELATIVA"""

counter_test_positivi = 0
total_tests = 5

counter_test_positivi += tester_fun(Ex3, ['Roma','Parigi','voli1.csv'] ,180)
counter_test_positivi += tester_fun(Ex3, ['Roma','Parigi','voli2.csv'] ,170)
counter_test_positivi += tester_fun(Ex3, ['Londra','Madrid','voli2.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Londra','Roma','voli2.csv'] ,80)
counter_test_positivi += tester_fun(Ex3, ['Roma','Madrid','voli2.csv'] ,90)
counter_test_positivi += tester_fun(Ex3, ['Mosca','Roma','voli1.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Milano','Parigi','voli3.csv'] ,170)
counter_test_positivi += tester_fun(Ex3, ['Mosca','Amsterdam','voli3.csv'] ,'Impossibile')
counter_test_positivi += tester_fun(Ex3, ['Amsterdam','Milano','voli3.csv'] ,80)
counter_test_positivi += tester_fun(Ex3, ['Milano','Madrid','voli3.csv'] ,90)
            
    


print('La funzione',Ex3.__name__,'ha superato',counter_test_positivi,'test su',total_tests)
            
    

