def ChkPrime(List):
    PrimeList = []
    for no in List:
        if no <=1:
            continue
        for i in range(2,no):
            if no % i ==0:
                break
        else:
            PrimeList.append (no)
    return PrimeList