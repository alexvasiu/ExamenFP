a = int(input("a = "))
b = int(input("b = "))
if a <= 0 or b <= 0:
    print("Error")
else:
    while b:
        r = a % b
        a = b
        b = r
    print("cmmdc =", a)
