def t(x):
    y=list(x)
    y.reverse()
    x=tuple(y)
    return x
print(t((5, 3, 2)))
print(t(('Hi', 'Ola', 'xD')))