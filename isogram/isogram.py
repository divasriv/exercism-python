def is_isogram(string):
    string=string.lower()
    a=''
    b=''
    word=[symbol.replace('-', '') for symbol in string.split()]
    for char in word:
        a=set(char)
        b=list(char)
    return len(a) == len(b)