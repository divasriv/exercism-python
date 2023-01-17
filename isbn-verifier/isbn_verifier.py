def is_valid(isbn):
    isbn = list(isbn.replace("-", ""))
    length=len(isbn)
    if length==10: #isbn should have exactly 10 chars
        for i in isbn[0:-1]: #checking till (len-1) as last char can be X
            if str(i).isalpha():
                return False
        if isbn[-1] not in '0123456789':
            if isbn[-1]!='X': 
                return False #if last char is not number and not X, isbn invalid
            else:
                if isbn[-1]=='X':
                    isbn[-1]=10 #if last char is X, it is considered 10
        code=0
        for i,val in enumerate(isbn): 
            j=length-i
            code+=(j*int(val)) #for 3-598-21508-8, code=(3*10+5*9+...+8*1)
        if code%11==0:
            return True
    return False