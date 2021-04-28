#number guess game
import random
#decided num
sys_num = random.randint(1,101)
tries = 10
while(tries>0):
    user_guess=int(input("enter you guess : "))
    if(user_guess==sys_num):
        print("you won :-)")
        print("the number is ",sys_num)
        break
    elif(sys_num<user_guess):print("you guess is greater than system number")
    elif(sys_num>user_guess):print("you guess is lower than system number")
    tries-=1
    print("you have ",tries," no of tries left")
else:print("you dont have tries .. number is ",sys_num,"you loose the game :-(")