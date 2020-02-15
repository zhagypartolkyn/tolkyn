def exercise_14(l,a):
    s=set()
    for i in range (len(l)):
        if l[i]>a:
            s.add(l[i])
    return s
print (exercise_14([11,2,44,23], 10))
print (exercise_14([1,200,45,-67], 45))