nr = int(input("nr = "))
ok = True
if nr < 2:
    ok = False
i = 2
while i * i <= nr and ok:
    if nr % i == 0:
        ok = False
    i += 1
if ok:
    print(nr, "e prim")
else:
    print(nr, "nu e prim")