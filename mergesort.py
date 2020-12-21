def merge(a):
    l = len(a)
    if l == 1:
        return a
    elif l == 2:
        if a[0]>a[1]:
            return a[::-1]
        else:
            return a
    else:
        b = merge(a[0:l//2])
        c = merge(a[l//2:l])
        d = []
        i = 0
        j = 0
        for k in range(l):
            if i<len(b) and j<len(c):
                if b[i]<c[j]:
                    d.append(b[i])
                    i+=1
                else:
                    d.append(c[j])
                    j+=1
        if i<len(b):
            d.extend(b[i:len(b)])
        else:
            d.extend(c[j:len(c)])
        return d
print(merge([9,5,45,16,7,82,101]))