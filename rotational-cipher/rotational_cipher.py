def rotate_word(text,key):  #rotating each word, join the sentence in rotate function
    result = "" 
    for i in range(len(text)):  
        char = text[i]   
        if(str(char).isalpha()): #only alphabets are rotated
            if (char.isupper()):  
                #ascii value of A is 65, convert char to unicode (ord), rotate, then convert back to ascii char (chr)
                result += chr((ord(char) + key - 65) % 26 + 65)     
            else:  
                result += chr((ord(char) + key - 97) % 26 + 97)  #ascii value of a is 97
        else:
            result+=char #retaining numbers and symbols as it is
    return result 

def rotate(text, key):
    return ' '.join([rotate_word(word,key) for word in text.split()]) 


