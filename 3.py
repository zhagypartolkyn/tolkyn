def square1(A,ind):
    
    for i in range (ind, len(A)):
        A[i]=A[i]**2
    return A
print(square1([10, 3, 4, 5, 9], 2))
print(square1([9, 0, 12, 3, 4, 56, 9, 16], 6))