def steps(n):
    count=0
    if n<=0:
        raise ValueError("Only positive integers are allowed")
    while n!=1:
        if(n%2):
            n=3*n+1
            count+=1
        else:
            n=n//2
            count+=1
    return count