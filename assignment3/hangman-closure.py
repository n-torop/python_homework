def make_hangman(secret_word):
    word=[]
    for item in secret_word:
        word.append(item)
    print (word)
    guesses=[]
    def hangman_closure(letter):
        
        guesses.append(letter)
        for char in word:
            if char==letter:
                

        # if character in guesses
        # displayed=''.join()

    return hangman_closure
    
secret="icecream"

outer_call=make_hangman(secret)

letter="i"
inner_call=outer_call(letter)
