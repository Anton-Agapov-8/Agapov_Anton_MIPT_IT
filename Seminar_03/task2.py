def razlozhenie(n, mnozhiteli=None):
    if mnozhiteli is None:
        mnozhiteli = []
    for d in range(2, n):
        if n % d == 0:
            mnozhiteli.append(d)
            return razlozhenie(n // d, mnozhiteli)
    mnozhiteli.append(n)
    return mnozhiteli


n = int(input())
print(razlozhenie(n))
