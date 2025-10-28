#Sofia Guzman section 02
# rock paper scissors
#player and computer score
yourScore = 0
computerScore = 0
choice_list = ["rock", "paper","scissors"]
print("Welcome to Rock, Paper, Scissors!")
yourChoice = input("pick rock, paper, or scissors: (q to quit)").lower()
import random
while yourChoice != "q":
    if yourChoice not in choice_list:
        print("invalid choice, try again")
    else:
        computerChoice = random.randint(1,3)
    if computerChoice ==1:
        computerChoice = "rock"
    elif computerChoice == 2:
        computerChoice = "paper"
    else:
        computerChoice = "scissors"
    print(f"computer choice: {computerChoice}")
    if (yourChoice == computerChoice):
        print ("Tie")
        yourScore += 0
        computerScore+= 0
    elif(yourChoice == "rock" and computerChoice == "scissors") or(yourChoice == "paper" and computerChoice == "rock")or(yourChoice == "scissors" and computerChoice == "paper"):
        print ("You win")
        yourScore += 1
        computerScore+= 0
    elif(yourChoice == "rock" and computerChoice == "paper") or (yourChoice == "paper" and computerChoice == "scissors") or(yourChoice == "scissors" and computerChoice == "rock"):
        print("you lose")
        yourScore += 0
        computerScore+= 1
    print(f"Score => You:{yourScore} | Computer:{computerScore}")
    yourChoice = input("Enter rock, paper, or scissors (press q to quit)").lower()
print("Thanks for playing!")

