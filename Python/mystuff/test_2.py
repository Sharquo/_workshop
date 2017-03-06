def digit_sum(x):
    x = str(x)
    l = []
    for c in x:
        l.append(int(c))
    s = sum(l)
    return s
