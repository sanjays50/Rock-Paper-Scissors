import random


while True:
    my_answer=input("Choose : Rock , Paper or scissors: ")
    my_answer=my_answer.lower()

    if my_answer=="quit":
        break

    if my_answer != "rock" and my_answer != "paper" and my_answer != "scissors" :
        print("Choose a correct answer")
        continue
    computer_ans=random.choice(["rock","paper","scissors"])
    if(computer_ans==my_answer):
        print("YOU tied !!! ")
        continue
    elif my_answer=="paper" and computer_ans=="rock":
        print("YOU Win ! ")
        continue
    elif my_answer=="rock" and computer_ans=="scissors":
        print("YOU Win ! ")
        continue
    elif my_answer=="scissors" and computer_ans=="paper":
        print("YOU Win ! ")
        continue
    else:
        print("YOU Lose. Try Again ! ")
        continue
