def delet(A,ind):
    for ind in range (ind,len(A)):
        del A[ind:len(A)]
    return A
print (delet([10, 3, 4, 5, 9], 1))
print (delet([9, 0, 12, 3, 4, 56, 9, 16], 7))