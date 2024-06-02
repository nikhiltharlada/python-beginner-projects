import random as rs
options=['rock','paper','scissor']
user=input("Enter your' choices(rock,paper,scissor):-").lower()
computer=rs.choice(options)
print(f"your's choice is:_{user}")
print(f"computer choice is:-{computer}")
def game(user,computer):

    if(user==computer):
        print("It's tie")
    elif(user=='rock' and computer=='scissor'):
            #u=u+1
        print('you win!')
    elif(user=='scissor'and computer=='paper'):
        print('you win!')
    elif(user=='paper' and computer=='rock'):
        print('you win!')
    else:
        print("you lose")
print(game(user,computer))