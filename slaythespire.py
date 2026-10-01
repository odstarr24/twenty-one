import random
import time
import sys

block = 0

kills = 0
hp1 = 80
autoheal1 = 6
vulnerable1 = 0
weak1 = 0
strength1 = 0
playtime = 0
dmg_user = 0

keyusage = 0

money = 100

hp2 = 0
block2 = 0
vulnerable2 = 0
weak2 = 0
strength2 = 0
dmg = 0

cardpol = ["strike", "defend", "bash", "bodyslam", "clothesline", "heavyblade", "ironwave", "twinstrike", "entrench", "hemokinesis", "inflame"]
def strike():
    global hp2
    hp2 -= 6
def bash():
    global hp2
    hp2 -= 8
    global vulnerable2
    vulnerable2 += 2
    global dmg_user
    dmg_user = 1.5
def bodyslam():
    global hp2
    global block
    hp2 -= block
def clothesline():
    global hp2 
    hp2 -= 12
    global weak2 
    weak2 += 2
    global dmg
    dmg = dmg*0.7
def heavyblade():
    global hp2
    global strength1
    hp2 -= 14*strength1
def ironwave():
    global block1
    block1 += 5
    global hp2
    hp2 -= 5
def twinstrike():
    global hp2
    hp2 -= 5*2
def entrench():
    global block
    block == block*2
def hemokinesis():
    global hp1 
    hp1 -= 2
    global hp2
    hp2 -= 15
def inflame():
    global strength1
    strength1 += 2
def strength():
    global dmg_user
    dmg_user = 1.5

hand = ["strike", "defend"]
drawpile = []
name = input("hello, dear user! may you tell me your name?\n")
print(f"good morning, {name}! have you slept well?...")
time.sleep(1)
print(f"well, that doesn't matter. you're here to kill the three enemies, {name}. you get different cards added into your hand as you progress.")
time.sleep(2)
print("...")
time.sleep(1)
print("currently, you have STRIKE, which lets you deal 6 dmg, and DEFEND, which blocks 5 dmg points received. there are a lot more, though.")
time.sleep(3)
print("as you go on, each enemy will get stronger, but so do you! keep in mind, though, you can only use 3 cards per round...")
time.sleep(4)
print(f"anyway, let's go, {name}!")
time.sleep(1)

hp2 += 50
print(f"so, {name}, you're facing your first fight! exciting, isn't it?")
time.sleep(1)
print("each round, you get to use up to three cards. afterwards, you enemy'll attack you. this goes on until one of you is dead.")
time.sleep(2)
print("alright, let's start!")

while hp1 > 0 and hp2 > 0: 
    while playtime < 3:
        print(hand)
        if keyusage == 0:
            key = input("enter key if available:\n")
            if key == "one":
                dmg = round(random.randint(6, 18))
                hp1 += autoheal1
                hp2 = 100
                if hp1 > 80:
                    hp1 = 80
                keyusage += 1
            elif key == "midboss":
                dmg = round(8)
                hp1 += autoheal1
                hp2 = 200
                if hp1 > 80:
                    hp1 = 80
                keyusage += 1
                weak1 = random.randint(0, 1)
                vulnerable = random.randint(0, 1)
            else:
                dmg = round(12)
                keyusage += 1
        print(f"enemy attack: {dmg}")
        usage = input("which card do you wanna use?\n")
        if usage == "strike":
           strike()
           
           print("strike has been used successfully!")
           playtime += 1
        elif usage == "defend":
            block += 5
            
            print(f"defend has been used successfully! current hp: {hp1}")
            playtime += 1
        elif usage == "bash":
            bash()
            
            playtime += 1
            print("bash has been used successfully!")
        elif usage == "bodyslam":
            bodyslam()
           
            playtime +=1
            print("bodyslam has been used successfully!")
        elif usage == "clothesline":
            clothesline()
            
            playtime += 1   
            print("clothesline has been used successfully!")             
        elif usage == "heavyblade":
            heavyblade()
            
            playtime += 1
            print("heavyblade has been used successfully!")    
        elif usage == "ironwave":
            ironwave()
            
            playtime += 1
            print("ironwave has been used successfully!")
        elif usage == "twinstrike":
            twinstrike()
            
            playtime += 1
            print("twinstrike has been used successfully!")
        elif usage == "entrench":
            entrench()
            
            playtime += 1
            print("entrench has been used successfully!")
        elif usage == "hemokinesis":
            hemokinesis()
            
            playtime += 1
            print("hemokinesis has been used successfully!")
        elif usage == "inflame":
            inflame()
            
            playtime += 1
            print("inflame has been used successfully!")
        if playtime >= 3:
            print("3 cards have been used!")
            block -= dmg
            hp1 += block
            block = 0
            if key == "one":
                dmg = random.randint(6, 18)
            elif key == "midboss":
                weak1 = random.randint(0, 1)
                if weak1 == 1:
                    dmg_user = dmg_user*0.7
                vulnerable1 = random.randint(0, 1)
                if vulnerable1 == 1:
                    dmg *= 1.5

            print(f"enemy attacked succesfully! current hp: {hp1}; enemy hp: {hp2}")
            playtime = 0

        if hp1 <= 0:
            print("oh no, you've died!")
            sys.exit(1)
    
        elif hp2 <= 0:
            print("enemy killed!")
            kills += 1
            keyusage = 0
            money += random.randint(40, 80)
            if kills == 1:
                print(f"good job, {name}!")
                difficulty = input("that was easy, wasn't it?\n")
                print(f"{difficulty}?...well, just brace for what's about to happen :)")

                print("before we go on, I think it would be useful for me to explain the other cards, right?")
                time.sleep(1)
                print("BASH deals 8 dmg and applies 2 VULNERABLE")
                time.sleep(1)
                print("BODYSLAM deals equal the damage to your block")
                time.sleep(1)
                print("CLOTHESLINE deals 12 dmg and applies 2 WEAK")
                time.sleep(1)
                print("HEAVYBLADE deals 14 dmg but is thrice as much affected by STRENGTH")
                time.sleep(1)
                print("IRONWAVE gives 5 block and deals 5 damage")
                time.sleep(1)
                print("TWINSTRIKE deals 5 dmg twice")
                time.sleep(1)
                print("ENTRENCH doubles your block")
                time.sleep(1)
                print("HEMOKINESIS makes you lose 2HP but deal 15 dmg")
                time.sleep(1)
                print("and lastly, INFLAME makes you gain 2 strength.")
                time.sleep(1)
                answer = input("each batlle, you'll have to think more and more strategically. got that?\n")

                if answer == "yes":
                    print("great!")
                else: 

                    print("...I don't really care, you know. that question was rethorical.")
                time.sleep(1)
                print(f"now, you might be wondering what in the world STRENGTH, WEAK and VULNERABLE are, right {name}?")
                time.sleep(1)
                print()
                print("well, VULNERABLE makes the affected person more affected by damage")
                time.sleep(1)
                print("WEAK weakens the affected person's damage dealt")
                time.sleep(1)
                print("and STRENGTH, well...increases your strength, you know... you'd have to be an idiot to not get that.")

                time.sleep(1)
                print("...")
                time.sleep(1)
                print("anyway, let's continue.")

                choice = input(f"you'll now get to choose a card to add to your deck: {random.sample(cardpol, 3)}\n")
                hand.append(choice)

                reply = input(f"good. also, {name}, do you remember? at the start, you were asked for a KEY.\n")
                print("those keys unlock the other enemies hidden away. as you progress, you'll get more and more keys from me.")
                time.sleep(1)

                ready = input("your current key is 'one'. press enter to start your second battle.\n" )

            elif kills == 2:
                difficulty = input(f"woah, that was tough, wasn't it, {name}?\n")
                print("well, you'll now have your well deserved break.")
                print(f"here, you can either heal your full hp (current hp: {hp1}) or go to the merchant.")
                print("the merchant let's you buy several cards to add to your deck, but keep in mind that they cost money!")
                time.sleep(2)
                print("...")
                time.sleep(1)
                print("well, I guess I forgot to mention. each game attempt, you start off with 100 coins and earn between 40-80 coins per kill.")
                print("during your playthrough, you'll have an opportunity to visit the merchant and spend your money wisely.")
                print("each revisit, he'll have a different offer, though, so keep that in mind!")
                print("before anything, though, you can now choose another card to add to your deck, for free!")
                choice = input(f"you'll now get to choose a card to add to your deck: {random.sample(cardpol, 3)}\n")
                hand.append(choice)
                loc = input("great! now, where do you wanna go: bedroom or merchant?\n")
                if loc == "bedroom":
                    hp1 = 80
                    print("hp restored!")
                else:
                    while True:
                        print(f"you can now choose between those cards: {random.sample(cardpol, 5)}")
                        print("keep in mind, though, each costs 80 coins!")
                        choice = input(f"current balance: {money}.\n")
                        if choice in cardpol:
                            hand.append(choice)
                            money -= 80
                            furtherlies = input("wanna buy more?\n")
                            if furtherlies == "no" or money < 80:
                                break
                            else:
                                continue
                print("alright, now, be cautious. this one will be by far more difficult...")
                ready = input("your current key is 'midboss'. press enter to start your third battle.\n" )

            else:
                print(f"good job, {name}, you've won! congrats!")
                sys.exit(1)
 

