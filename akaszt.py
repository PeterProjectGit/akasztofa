import random
def randomwordgenerate()->str:
    '''Purpose: it gets back a random string'''
    wordsList = ["alma", "körte", "barack", "szilva", "narancs", "eper", "citrom", "mandula", "datolya", "eperfa"]
    return random.choice(wordsList)
wordTemplate = []


word = randomwordgenerate()
for i in range(len(word)):
    wordTemplate.append("_")
    
print('\n Please try to think about the word given, you have 10 chances.')
guess = input("Your guess: ")
if guess not in word:
    print("This is not the word")
else: 
    for i in range(len(word)):
        if word[i] == guess:
            wordTemplate[i] = guess
