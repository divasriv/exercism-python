def response(hey_bob):
    if hey_bob.isupper() and '?' in hey_bob and '.' not in hey_bob:
        return 'Calm down, I know what I\'m doing!'
    if hey_bob.endswith('?') or '?' in hey_bob and '.' not in hey_bob:
        return 'Sure.'
    elif hey_bob.isupper():
        return 'Whoa, chill out!'
    # elif hey_bob.isupper() and '?' in hey_bob:
    #     return 'Calm down, I know what I\'m doing!'
    elif hey_bob.isspace() or hey_bob=='':
        return 'Fine. Be that way!'
    return 'Whatever.'
