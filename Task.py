words=input('Enter the word: ')


vowels = 'AEIOUaeiou'
    
if words[-1] in vowels:
    inator = "-inator"
else:
    inator = "inator"

word_result = words + inator + str(len(words)) + '000'

print(word_result)