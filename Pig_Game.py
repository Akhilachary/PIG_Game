import random
print("**************************************************")
print("Welcome to PIG Game!!")
print("Let's Play the Game.")
names=['virat kohli','PV Sindhu','Mary Kom']
players=[]
li=['yes','no']
name =''
def count_members():
    members=int(input("Enter the numbers of players (2-4): "))
    if members >= 5 and members <=1:
        print("Please enter valid number of players!.")
        count_members()
    else:
        name = input("Enter your good name: ")
        players.append({
            'name':name,
            'score':0
        })
    for _ in range(1,members):
        namee=random.choice(names)
        players.append({'name': namee,
                       'score':0})
        names.remove(namee)
    return name
def Game():
    print("**************************************************")
    print('The Game Begins Now.')
    name_return=count_members()
    roll_again=True
    newlist = players.copy()
    Game=True
    while(Game):
        for i in newlist:
            print(f"hey Hie {i['name']} It's your turn! and your score is {i['score']}")
            while(roll_again):
                dice=random.randint(1,6)
                print(f"on rolling dice you have got {dice}")
                if dice==1:
                    print("You have got 1 so you loose your turn and score!")
                    i['score']=0
                    roll_again=False
                else:
                    i['score']=i['score']+dice
                    print(f"Your total score is {i['score']} ")
                    if i['name']==name_return:
                        opinion=input("Do you want to continue game?['yes'/''no'] ").lower()
                    else:
                        opinion=random.choice(li)
                    if opinion=='yes':
                        continue
                    else:
                        roll_again=False
            roll_again=True
            print("**************************************************")
            if i['score'] >= 20:
                print(f"Congrats {i['name']}!!! You have won the Game!..")
                Game=False
                break
Game()
print("**************************************************")
chc=input("Would you like to continue the game? ['yes'/'no'] ").lower()
if chc=='yes':
    Game()
else:
    print("Thank you for participating")




