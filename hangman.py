import random
fail=5
word=['scissor','rock','stone','fight','tiger','cow','kite','joker']
na=random.choice(word)
guess=''
stage=0
turns = 10
while turns>0:
    failed = 0
    for char in na :
        if char in guess:
            print(char,end=" ")
        else:
            print("_",end=" ")
            failed += 1
    if failed==0:
        print('\n\nyou win')

        print('\n\nthe word is ',na)
        break
    guesses =input("\n\nguess a letter: ",)
    print(end=" ")
    guess += guesses
    
    if guess not in na:
        turns-= 1
        print("\n\nwrong ")
        stage+= 1
        if stage==1:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |")
            print("               |")
            print("               | ")
            print("               |")
            print("               |")
        if stage==2:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |")
            print("               |")
                print("           |")
            print("               |")
              
        if stage==3:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |     |")
            print("               |     |")
            print("               |")
            print("               |")
        if stage==4:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |     |")
            print("               |     |")
            print("               |")
            print("               |     ")
        if stage==5:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |    /|")
            print("               |     |")
            print("               | ")
            print("               |")
        if stage==6:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |    /|\   ")
            print("               |     |")
            print("               |")
            print("               |")
       
        if stage==7:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |    /|\ "  )
            print("               |     |")
            print("               |    /")
            print("               |")
        if stage==8:
            print("               -----------")
            print("               |     |")
            print("               |     |")
            print("               |     Q")
            print("               |    /|\ ")
            print("               |     |")
            print("               |    / \ ")
            print("               |")
        if stage==9:
            print("-----------")
            print("|     |")
            print("|     |")
            print("|     Q")
            print("|    /|\ ")
            print("|     |")
            print("|    / \ ")
            print("|")
            print("I can't breath")
        if turns==0:
            print('\n\ngame over')
