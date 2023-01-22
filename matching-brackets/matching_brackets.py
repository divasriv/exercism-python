def is_paired(input_string):
    arr=[]
    OPEN_BRACKETS=['[','{','(']
    CLOSE_BRACKETS=[']','}',')']
    for char in input_string:
        if char in OPEN_BRACKETS:
            arr.append(char)
        elif char in CLOSE_BRACKETS:
            if len(arr)==0:
                return False
            popped=arr.pop()
            if (popped==OPEN_BRACKETS[0] and char != CLOSE_BRACKETS[0]) or (popped==OPEN_BRACKETS[1] and char != CLOSE_BRACKETS[1]) or (popped==OPEN_BRACKETS[2] and char != CLOSE_BRACKETS[2]):
                return False
    return len(arr)== 0


