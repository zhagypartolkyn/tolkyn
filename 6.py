def ins(a,ind1,ind2,b):
    l=0
    for k in range (ind1,ind1+len(b)):
        a.insert(k,b[l])
        l+=1
    for c in range (ind2, len(a)):
        del a[ind2]
    return a
print (ins([10, 3, 4, 5, 9], 3, 4, [1, 2, 3]))