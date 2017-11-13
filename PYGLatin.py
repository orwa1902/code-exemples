#what we add to the original word
pygLatin ='ay'
"""a condition that say \'dont print the word if its not bigger than 2 chars and if there is a numbers in it and if it doesnt follow the if statment, it prints an error"""
original = input("Enter a word:")
if len(original) > 2 and original.isalpha():
    print (original)
else:
    print ('plese enter a valid expression')
#make the word we choose in lower case
word = original.lower()
#the first char in the word is store inside the first variable
first = word[0]
#finally, we create the new word and store it in a variable new_word
new_word = word[1:len(word)] + first + pygLatin
"""eventually, if the word is more or equals to 5 charactert long, it will be printed by the console"""
if len(new_word) >= 5: 
    print (new_word)
