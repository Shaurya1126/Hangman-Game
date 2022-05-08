"create a hangman game using the custom module words.py "
from Hangman_69 import * 


print(" _ "*len(word))
word=list(word)
answer="_"*len(word)
answer=list(answer)
while True:
	if answer==word:
		print("Congrats, you guessed the correct word")
		break
	guess= input("Guess the word")
	if guess in word:
		for i in range(len(word)):
			if word[i]==guess:
				answer[i]=guess
				print("Good guess")
				print(" ".join(answer))
	else:
		print("Incorrect guess, please retry")
		



