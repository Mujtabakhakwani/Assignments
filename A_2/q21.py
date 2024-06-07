def ion2e():
    word = str(input("enter the word "))
    if word.endswith('ion'):
        print(word[:-3] + 'e')
    else:
        print(word)
ion2e()