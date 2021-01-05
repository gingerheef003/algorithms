n = int(input("Enter n: "))
m = int(input("Enter m: "))

def mul(x, y):
    l = len(str(x))
    k = len(str(y))
    if l==1 or k==1:
        return x*y
    else:
        ac = mul(int(str(x)[0:l//2]), int(str(y)[0:k//2]))
        bd = mul(int(str(x)[l//2:l]), int(str(y)[k//2:l]))
        adbc = mul(int(str(x)[0:l//2])+int(str(x)[l//2:l]), int(str(y)[0:k//2])+int(str(y)[k//2:l])) - (ac + bd)

        if l%2==0:
            return ac*10**l + adbc*10**(l//2) + bd
        else:
            return ac*10**(l+1) + adbc*10**(l//2+1) + bd

print("n * m =", mul(n,m))