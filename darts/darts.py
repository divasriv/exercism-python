def score(x, y):
    point=x**2+y**2
    if point<= 1:
        return 10
    if 25>=point>1:
        return 5
    if 100>=point>25:
        return 1
    return 0
