def square(number):
    if(number<1 or number >64):
        raise ValueError("square must be between 1 and 64")
    grains=1
    for i in range(1,number):
        grains=grains*2 
    return grains


def total():
    sum=0
    for i in range(1,65):
        sum=sum+square(i)
    return sum

