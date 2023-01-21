secret={1: "wink",2: "double blink",4: "close your eyes",8: "jump"}

def commands(binary_str):
    num = int(binary_str, 2)
    secret_handshake = [val for key,val in secret.items() if num & key]
    if num & 16:
        secret_handshake.reverse()
    return secret_handshake
