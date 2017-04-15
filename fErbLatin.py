erbLatin ='erb'

original = raw_input("Enter a word:")
if len(original) > 2 and original.isalpha():
    print (original)
else:
    print ('404 Error')
word = original.lower()
first = word[0]
new_word = word[1:len(word)] + first + erbLatin
if len(new_word) > 5: 
    print (new_word)
