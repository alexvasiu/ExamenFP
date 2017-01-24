def isPrime(nr):
    if nr < 2:
       return False
    i = 2
    while i * i <= nr:
        if nr % i == 0:
            return False
        i += 1
    return True

n = int(input("n = "))

if n < 1: print("Error")
elif n == 1: print("1")
else:
    n -= 1
    i = 2
    while n:
        if isPrime(i):
            n -= 1
            if n == 0:
                print(i)
        else:
            d = 2
            j = i
            while j != 1 and n:
                ok = 0
                while j % d == 0:
                    j //= d
                    ok = 1
                if ok:
                    z = d
                    while z > 0 and n > 0:
                       z -= 1
                       n -= 1
                    if n == 0:
                        print(d)
                d += 1
        i += 1