import random
while True:
    rpc = ["Rock","Papper","Scissors"]
    npc = random.choice(rpc)
    player =  str(input("Choose Rock, Papper or Scissors: "))
    player = player.capitalize()


    if player == npc:
       print(f"Both choose {player}. it is a tie")

    elif player == "Rock":
        if npc == "Scissors":
            print(f"You won. player choose {player} and computer choose {npc}")
        else :
           print(f"You lost. player choose {player} and computer choose {npc}")

    elif player == "Papper":
        if npc == "Rock":
            print(f"You won. player choose {player} and computer choose {npc}")
        else :
            print(f"You lost. player choose {player} and computer choose {npc}")

    elif player == "Scissors":
        if npc == "Papper":
            print(f"You won. player choose {player} and computer choose {npc}")
        else :
            print(f"You lost. player choose {player} and computer choose {npc}")

    play_again = input('Play again.Y/N: ')
    if play_again.upper() != "Y":
        break 