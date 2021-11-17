n = int(input("Enter n: "))
m = int(input("Enter m: "))

def mult(x, y):
    l = len(str(x))
    k = len(str(y))
    if l==1 or k==1:
        return x*y
    else:
        ac = mult(int(str(x)[0:l//2]), int(str(y)[0:k//2]))
        bd = mult(int(str(x)[l//2:l]), int(str(y)[k//2:k]))
        ad_bc = mult(int(str(x)[0:l//2])+int(str(x)[l//2:l]), int(str(y)[0:k//2])+int(str(y)[k//2:k])) - (ac + bd)

        return ac*10**(l+k-l//2-k//2) + bd + 

print("n * m =", mult(n,m))