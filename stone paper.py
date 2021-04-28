#stone paper scissor game
import random
#random location
options=["stone","paper","scissors"]
matches = 5
sys_score = 0
user_score = 0
while(matches>0):
    sys_choose = random.choice(options)
    user_choice = input("enter your choice : ")
    if(user_choice.lower()==sys_choose):
        print(" no one get points")
    elif(user_choice.lower()=="stone" and sys_choose=="scissors"):
        user_score+=1
        print("user won . now user score is ",user_score)
    elif(user_choice.lower()=="stone" and sys_choose=="paper"):
        sys_score+=1
        print("system won . now system score is ",sys_score)
    elif(user_choice.lower()=="paper" and sys_choose=="scissors"):
        sys_score+=1
        print("system won . now system score is ",sys_score)
    elif(user_choice.lower()=="paper" and sys_choose=="stone"):
        user_score+=1
        print("user won . now user score is ",user_score)
    elif(user_choice.lower()=="scissors" and sys_choose=="paper"):
        user_score+=1
        print("user won . now user score is ",user_score)
    elif(user_choice.lower()=="scissors" and sys_choose=="stone"):
        sys_score+=1
        print("system won . now system score is ",sys_score)
    matches-=1
else:
    if(sys_score==user_score):
        print("NO one is winner")
    elif(sys_score>user_score):
        print("System won the game")
    else:
        print("User won the game")