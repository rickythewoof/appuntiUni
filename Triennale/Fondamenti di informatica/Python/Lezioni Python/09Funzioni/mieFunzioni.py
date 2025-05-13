def ispari(n):
    if n % 2 == 0:
        return True
    else:
        return False

def isprimo(n):
    maxdivisore = n//2+1
    for i in range(2,maxdivisore):
        if n % i == 0:
            return False
    return True
