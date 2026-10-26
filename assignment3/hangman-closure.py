def make_hangman(secret_word):
    # word=[]
    # for item in secret_word:
    #     word.append(item)
    # print (word)
    guesses=[]

    def hangman_closure(letter):
        
        guesses.append(letter)
        word=""
        for char in secret_word:
            if char in guesses:
                word+=char
            else:
                word+="_"

        print (word)
        return all(char in guesses for char in secret_word)





        # if character in guesses
        # displayed=''.join()

    return hangman_closure


if __name__=="__main__":
    secret=input("Enter the secret word: ").lower()
    check_guess=make_hangman(secret)

    while True:
        letter=input("Guess a letter: ").lower()

        if check_guess(letter):
            print ("You guessed the word!")
            break

