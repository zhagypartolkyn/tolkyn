def exercise_13(l: list) -> str:
    some_dict_to_check = dict()
    print(some_dict_to_check)
    for i in l:
        if i in some_dict_to_check:
            some_dict_to_check[i] += 1
        else:
            some_dict_to_check[i] = 1
    odds = 0
    for i in some_dict_to_check.values():
        if i % 2 == 1: 
            odds += 1
        if odds > 1: 
            return "No"
    return "Yes"

print(exercise_13([3,4,8,5,3]))
print(exercise_13([1,2,3,1,2]))