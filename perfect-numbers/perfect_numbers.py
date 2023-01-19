def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number<1:
        raise ValueError("Classification is only possible for positive integers.")
    sum=0
    for i in factors(number):
        sum+=i
    if sum==number:
        return 'perfect'
    if sum>number:
        return 'abundant'
    return 'deficient'


def factors(num):
    factor_list=[]
    for i in range(1, num):
       if num % i == 0:
           factor_list.append(i)
    return factor_list

print(classify(6))