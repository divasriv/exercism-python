def word_in_pig(word):
    vowels = 'aeiou'

    while not word[0] in vowels:
        
        if word[0] in 'xy':
            if not word[1] in vowels: 
                break #if word starts with xr or yt (2nd letter not vowel), we retain the word as it is
        word=word[1:]+word[0] # Keep shifting letters to end till you reach first vowel
        
        # print(word)
        if word[0]=='u' and word[-1]=='q': #after shift, word becomes u...q
            word=word[1:]+word[:1] #shifting u to end
            break
    return word+'ay' #add ay to shifted words as well as words with vowel start
    
def translate(text):
    return ' '.join([word_in_pig(word) for word in text.split()])
    