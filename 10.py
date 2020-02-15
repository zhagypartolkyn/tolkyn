def exercise_10(s):
    s1=set()
    for i in s:
        s1.add(i-1)
        s1.add(i+1)
    return s1    
print (exercise_10({1, 5, 9}))
print (exercise_10({2, 5, 7, 8, 10}))