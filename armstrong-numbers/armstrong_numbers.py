def is_armstrong_number(number):
    n = [int(x) for x in str(number)]
    length=len(n)
    add=0
    for i in n:
      add+=i**length
    return add==number
