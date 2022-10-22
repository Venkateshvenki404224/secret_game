import random
from mail import sendmail


names = ['Your friends name each seperated with a collon']
n = True
i = 0
user_names = [] #To Keep track of already used names
#while loop 
while n:
    choice = random.choice(names) 
    if choice in user_names:
        n = True
    else:
        choice1 = choice
        user_names.append(choice)
        email = input("Enter the mail: ")
        name = input("Enter the name ")
        sendmail(email, choice1,name)
        if len(user_names) == len(names):
            n = False
