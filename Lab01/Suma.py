n = int(input("n = "))
s = 0
for i in range(n):
    s += int(input("Number_{0} = ".format(i)))
print("Sum =", s)