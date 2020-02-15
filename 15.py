def exercise_15(l):
    k=0
    for i in range (1,len(l),2):
        if l[i]%2!=0:
            k+=1
    return k
print (exercise_15([0,3,11,2,44,23,4]))
print (exercise_15([22,23,24,33,34,35]))

