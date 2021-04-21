import random

print("Rock...")
print("Paper...")
print("Scissors...")

player1 = input("Player 1, make your move: ").lower()

rand_num = random.randint(0, 2)
if rand_num == 0:
    player2 = "rock"
elif rand_num == 1:
    player2 = "paper"
else:
    player2 = "scissors"
print(f"Player 2 (computer) played {player2}")

def error():
    print("something went wrong")

if player1 == player2:
    print("it's a tie")
elif player1 == "rock":
    if player2 == "scissors":
        print("player 1 wins")
    elif player2 == "paper":
         print("player 2 wins")
    else:
        error()
elif player1 == "paper":
    if player2 == "rock":
        print("player 1 wins")
    elif player2 == "scissors":
        print("player 2 wins")
    else:
        error()
elif player1 == "scissors":
    if player2 == "rock":
        print("player 2 wins")
    elif player2 == "paper":
        print("player 1 wins")
    else:
        error()
else: 
    error()