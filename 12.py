def exercise_12(l):
    s=set()
    for i in  l:
        if i in s:
            s.add(i**2)
        else:
            s.add(i)
    return s
print (exercise_12([1, 2, 2]))
print (exercise_12([1, 2, 2, 3, 4]))