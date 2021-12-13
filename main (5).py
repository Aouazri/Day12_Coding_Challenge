import random 
logo = """    _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                        """
## ********** Function to pick which difficulty level: ********** ##
def difficulty_level() : 
  difficulty= input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()
  if difficulty== 'easy':
    return 10
  else:
    return 5
## ********** ********** ********** ********** ********** ## 
## A function that prints out which answer the user will see ## 
def check_guess(user_guess, computer_number):
  if user_guess == computer_number:
    return(f"You got it! The answer was {computer_number}")
  elif user_guess> computer_number:
    return("Too high ")
  else: 
    return("Too low ")
## ********** ********** ********** ********** ********** ##
## A function that shows how many attempts are left: ## 
def number_of_attempts(user_guess,computer_number):
  if user_guess> computer_number or user_guess< computer_number:
    return (attempts-1)
## ********** ********** ********** ********** ********** ##
#Start of the program 

print(logo)
print("Welcome to the Number Guessing Game! ")
print("I'm Thinking of a number between 1 and 100")
#Computer chooses a number between 1 and 100
computer_number = random.randint(1,100)
#print(f"The number the user has to guess is: {computer_number}")

#global variable 'attempts'

attempts= difficulty_level()
print(f"you have {attempts} attempts remaining to guess the number")

##while loop 
answer_found= False
while attempts !=0 and answer_found== False: 
  user_guess= int(input("Make a guess: "))
  guess = check_guess(user_guess, computer_number)
  attempts= number_of_attempts(user_guess,computer_number)
  if user_guess== computer_number:
    answer_found= True
    print(f"{guess}")
  elif attempts !=0:
    print(f"{guess} \nGuess Again.")
    print(f"You have {attempts} attempts remaining to guess the number.")
  else:
    print(guess)
    print("You have run out of guesses, you lose.")




