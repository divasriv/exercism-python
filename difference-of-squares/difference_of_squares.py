def square_of_sum(number):
    sum=0
    for i in range(1,number+1):
        sum+=i
    square=sum**2
    return square
        


def sum_of_squares(number):
    # pass
    square=0
    for i in range(1,number+1):
        square+=i**2
    return square
        


def difference_of_squares(number):
    return abs(square_of_sum(number) - sum_of_squares(number))
