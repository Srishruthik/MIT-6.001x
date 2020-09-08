def dict_interdiff(d1, d2):
    intersect = {}
    difference = {}
    for i in d1.keys():
        if i in d2.keys():
            intersect[i] = f(d1[i], d2[i])
        else:
            difference[i] = d1[i]
    for i in d2.keys():
        if i not in d1.keys():
            difference[i] = d2[i]
    return (intersect, difference)
    



