#basic game core
secret_word = "giraffe"
guess = ""
failure_num = 0

while guess != secret_word
    guess = input("Enter guess: ")
    failure_num += 1
    
print("You win!")
print("Number of failures: " + failure_num)

#set a limit for people to guess the secret_word

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:  
    print("End of Game!")
else:
    print("You win!")
