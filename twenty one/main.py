#
#
#
import random
# Trump cards:
# one up, two up, perfect draw, num-card, destroy, bloodshed, reincarnation, hush, refresh, shield +1, shield +2, disservice, friendship, return, exchange, bless, 
# reincarnation: one up, two up, shield +1,shield +2,bloodshed, go-for-17, go-for-24, go-for-27, bless, 



print("hallo spieler 1! du wirst nun gegen einen anderen spieler in einem epischen kartenspiel antreten!")
print("aber keine sorge, der einsatz ist nur dein leben. siehst du die kreissäge da oben? sie steht auf 7.")
print("wenn sie auf 13 fällt, stirbst du. wenn sie auf 1 fällt, stirbt dein gegner.")
print(" ")
print("die spielregeln sind einfach: du und dein gegner kriegen beide anfangs 2 karten zwischen 1-11.")
print("das ziel ist es, eine hand in höhe von 21 zu kriegen. wenn du über 21 kriegst, verlierst du direkt!")
print(" ")
print(" ")
print(" ")
nummertrummp = random.randint(1,7)
sägeblatt = 7
Trumpcards = ["one up","two up","perfect-draw","destroy","bloodshed","hush","refresh","shield +1","shield +2","disservice","friendship","return","exchange","bless", "reincarnation","num-card, go-for-17", "go-for-24", "go-for-27"]
change = 0
nummcard = ["2-card","3-card","4-card","5-card","6-card","7-card"]
Trump1 = []
Trump2 = []
choice = 0

while sägeblatt > 1 or sägeblatt < 13:
    hush1 = []
    spieler1 = []
    spieler2 = []
    ziel = 21
    damage = 1
    bless = 0

    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    for i in range(2):
        addon = random.choice(deck)
        spieler1.append(addon)
        deck.remove(addon)
        nummertrummp = random.randint(1,7)
        Trump1.append(random.choice(Trumpcards))
        if "num-card" in Trump1:
            Trump1.remove("num-card")
            Trump1.append(random.choice(nummcard))
    for i in range(2):
        addon = random.choice(deck)
        spieler2.append(addon)
        deck.remove(addon)
        Trump2.append(random.choice(Trumpcards))
        if "num-card" in Trump2:
            Trump2.remove("num-card")
            Trump2.append(random.choice(nummcard))

    erstekarte2 = spieler2[0]
    spieler2.remove(erstekarte2)
    erstekarte1 = spieler1[0]
    spieler1.remove(erstekarte1)

    print(Trump1)
    print(f"[{erstekarte1}, {spieler1[0]}]")
    print(f"[x, {spieler2[0]}]")

    wiederholung = 0

    while wiederholung < 2:
        
        trumja = input("willst du eine trumpcard verwenden?\n")
        while trumja == "ja":
            if trumja == "ja":
                re = choice
                choice = input("welche?\n")
                if choice =="one up" and "one up" in Trump1:
                    change += 1
                    Trump1.remove(choice)
                    print("die trump karte one up wurde vom spieler 1 verwendet.")
                elif choice =="two up" and "two up" in Trump1:
                    change += 2
                    Trump1.remove(choice)
                    print("die trump karte two up wurde vom spieler 1 verwendet.")
                elif choice =="shield +1" and "shield +1" in Trump1:
                    change -= 1
                    Trump1.remove(choice)
                    print("die trump karte shield +1 wurde vom spieler 1 verwendet.")
                elif choice =="shield +2" and "shield +2" in Trump1:
                    change -= 2
                    Trump1.remove(choice)
                    print("die trump karte shield +2 wurde vom spieler 1 verwendet.")
                elif choice == "2-card" and "2-card" in Trump1:
                    if 2 in deck:
                        spieler1.append(2)
                        deck.remove(2)
                        Trump1.remove(choice)
                        print("die trump karte two-card wurde vom spieler 1 verwendet.")
                    else:
                        print("die 2 ist nicht im deck")
                        Trump1.remove(choice)
                        continue
                
                elif choice == "3-card" and "3-card" in Trump1:
                    if 3 in deck:
                        spieler1.append(3)
                        deck.remove(3)
                        Trump1.remove(choice)
                        print("die trump karte three-card wurde vom spieler 1 verwendet.")
                    else:
                        print("die 3 ist nicht im deck")
                        Trump1.remove(choice)
                        continue
                elif choice == "4-card" and "4-card" in Trump1:
                    if 4 in deck:
                        spieler1.append(4)
                        deck.remove(4)
                        Trump1.remove(choice)
                        print("die trump karte four-card wurde vom spieler 1 verwendet.")
                    else:
                        print("die 4 ist nicht im deck")
                        Trump1.remove(choice)
                        continue
                elif choice == "5-card" and "5-card" in Trump1:
                    if 5 in deck:
                        spieler1.append(5)
                        deck.remove(5)
                        Trump1.remove(choice)
                        print("die trump karte five-card wurde vom spieler 1 verwendet.")
                    else:
                        print("die 5 ist nicht im deck")
                        Trump1.remove(choice)
                        continue
                elif choice == "6-card" and "6-card" in Trump1:
                    if 6 in deck:
                        spieler1.append(6)
                        deck.remove(6)
                        Trump1.remove(choice)
                        print("die trump karte six-card wurde vom spieler 1 verwendet.")
                    else:
                        print("die 6 ist nicht im deck")
                        Trump1.remove(choice)
                        continue
                elif choice == "7-card" and "7-card" in Trump1:
                    if 7 in deck:
                        spieler1.append(7)
                        deck.remove(7)
                        Trump1.remove(choice)
                        print("die trump karte seven-card wurde vom spieler 1 verwendet.")
                    else:
                        print("die 7 ist nicht im deck")
                        Trump1.remove(choice)
                        continue
                elif choice == "bloodshed" and "bloodshed" in Trump1:
                    change += 1
                    Trump1.append(random.choice(Trumpcards))
                    Trump1.remove(choice)
                    print("die trump karte bloodshed wurde vom spieler 1 verwendet.")
                    if "num-card" in Trump1:
                        Trump1.remove("num-card")
                        Trump1.append(random.choice(nummcard))
                elif choice == "destroy" and "destroy" in Trump1:
                    card = spieler2.pop()
                    deck.append(card)
                    Trump1.remove(choice)
                    print("die trump karte destroy wurde vom spieler 1 verwendet.")
                    print(f"{card} wurde zurück gelegt")
                elif choice == "hush" and "hush" in spieler1:
                    card = random.choice(deck)   
                    hush1.append(card)
                    deck.remove(card)
                    Trump1.remove(choice)
                    print("die trump karte hush wurde vom spieler 1 verwendet.")
                elif choice == "refresh" and "refresh" in Trump1:
                    deck.extend(spieler1)
                    deck.append(erstekarte1)
                    deck.extend(hush1)
                    spieler1.clear
                    erstekarte1 = ""
                    hush1.clear
                    Trump1.remove(choice)
                    print("die trump karte refresh wurde vom spieler 1 verwendet.")
                    for i in range(2):
                        addon = random.choice(deck)
                        spieler1.append(addon)
                        deck.remove(addon)
                    erstekarte1 = spieler1[0]
                    spieler1.remove(erstekarte1)
                    print(f"[{erstekarte1}],{hush1} {spieler1}")
                elif choice == "friendship" and "friendship" in Trump1:
                    Trump1.remove(choice)
                    for i in range(2):
                        Trump1.append(random.choice(Trumpcards))
                        print("die trump karte friendship wurde verwendet")
                        print(f"spieler 1 hat {Trump1[-1]} bekommen")
                        if "num-card" in Trump1:
                            Trump1.remove("num-card")
                            Trump1.append(random.choice(nummcard))
                        Trump2.append(random.choice(Trumpcards))
                        if "num-card" in Trump1:
                            Trump2.remove("num-card")
                            Trump2.append(random.choice(nummcard))
                elif choice == "return" and "return" in Trump1:
                    deck.append(spieler1[-1])
                    spieler1.remove(spieler1[-1])
                    Trump1.remove(choice)
                    print("die trump karte return wurde verwendet")
                elif choice == "exchange" and "exchange" in Trump1:
                    spieler2.append(spieler1[-1])
                    spieler1.append(spieler2[-2])
                    spieler1.remove(spieler1[-2])
                    spieler2.remove(spieler2[-2])
                elif choice == "bless" and "bless" in Trump1:
                    bless = 1
                    Trump1.remove(choice)
                    print("die trump karte bless wurde verwendet")
                elif choice == "disservice" and "disservice" in Trump1:
                    spieler2.append(random.choice(deck))
                    deck.remove(spieler2[-1])
                    Trump1.remove(choice)
                    print("die trump karte disservice wurde verwendet")
                elif choice == "perfect-draw" and "perfect-draw" in Trump1:
                    draw = []
                    draw.extend(spieler1)
                    draw.append(erstekarte1)
                    draw.extend(hush1)
                    drawsum = sum(draw)
                    for i in deck:
                        if i + drawsum == 21:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 20:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 19:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 18:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 17:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 16:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 15:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 14:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 13:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 12:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 11:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 10:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 9:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 8:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 7:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 6:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 5:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 4:
                            spieler1.append(i)
                            deck.remove(i)
                        elif i + drawsum == 3:
                            spieler1.append(i)
                            deck.remove(i)
                    Trump1.remove(choice)
                    print("die trump karte perfect draw wurde verwendet")
                elif choice == "go-for-17" and "go-for-17" in Trump1:
                    ziel = 17
                    Trump1.remove(choice)
                    print("die trump karte go-for-17 wurde verwendet")
                elif choice == "go-for-24" and "go-for-24" in Trump1:
                    ziel = 24
                    Trump1.remove(choice)
                    print("die trump karte go-for-24 wurde verwendet")
                elif choice == "go-for-27" and "go-for-27" in Trump1:
                    ziel = 27
                    Trump1.remove(choice)
                    print("die trump karte go-for-27 wurde verwendet")
                elif choice == "reincarnation" and "reincarnation" in Trump1:
                    Trump1.remove(choice)
                    if re == "one up":
                        change -=1
                        print("durch reincarnation wurde one up zerstört")
                    elif re == "two up":
                        change -=2
                        print("durch reincarnation wurde two up zerstört")
                    elif re == "shield +1":
                        change +=1
                        print("durch reincarnation wurde shield +1 zerstört")
                    elif re == "shield +2":
                        change += 2
                        print("durch reincarnation wurde shield +2 zerstört")
                    elif re == "bless":
                        bless = 0
                        print("durch reincarnation wurde bless zerstört")
                    elif re == "go-to-17":
                        ziel = 21
                    elif re == "go-to-24":
                        ziel = 21
                    elif re == "go-to-27":
                        ziel = 21
                    elif re == "bloodshed":
                        change -= 1
                        print("durch reincarnation wurde bloodshed zerstört")
                    else:
                        print("es gibt keine trumpkarte die man zurücksetzen kann")


                    
                else:
                            print("diese karte hast du nicht hahahahhahahahhaha")
            trumja = input("willst du noch eine?\n")
        
        
        
        card = input("willst du noch eine karte?\n")
        if card == "ja":
            nc = random.choice(deck)
            spieler1.append(nc)
            deck.remove(nc)
            Trump1.append(random.choice(Trumpcards))
            if "num-card" in Trump1:
                Trump1.remove("num-card")
                Trump1.append(random.choice(nummcard))
            print(Trump1)
            print(f"[{erstekarte1}],{hush1} {spieler1}")
            
            wiederholung = 0
        else:
            wiederholung += 1
            print("spieler 1 hat nicht gezogen")
            print(Trump1)
            print(f"[{erstekarte1}],{hush1} {spieler1}")


        potenziellesdeck = deck.copy()
        potenziellesdeck.append(erstekarte1)
        potenziellesdeck.extend(hush1)
        number_of_cards_below_22 = 0

        my_value = erstekarte2
        for val in spieler2:
            my_value = my_value + val

        for card in potenziellesdeck:
            if my_value + card < 22:
                number_of_cards_below_22 += 1

        verhaeltnis = number_of_cards_below_22 / len(potenziellesdeck)

        if verhaeltnis >= 0.5:
            nc = random.choice(deck)
            spieler2.append(nc)
            deck.remove(nc)
            wiederholung = 0
            Trump2.append(random.choice(Trumpcards))
            if "num-card" in Trump1:
                Trump1.remove("num-card")
                Trump1.append(random.choice(nummcard))
            print("spieler 2 hat gezogen")
            print(f"[x] {spieler2}")
        else:
            wiederholung += 1
            print("spieler 2 hat nicht gezogen")
            print(f"[x] {spieler2}")
    spieler1.append(erstekarte1)
    spieler1.extend(hush1)
    sum1 = sum(spieler1)
    spieler2.append(erstekarte2)
    sum2 = sum(spieler2)
    

    if sum1 == sum2 or sum1 > ziel and sum2 > ziel:
        print("gleichstand!")
        print(f"{spieler1}")
        print(f"{spieler2}")

    elif sum1 > ziel:
        print("spieler 1 overkillt!")
        print(f"{spieler1}")
        print(f"{spieler2}")
        if change + 1 < 0:
            sägeblatt += 0
        else:
            sägeblatt += 1 + change
    elif sum2 > ziel:
        print("spieler 2 overkillt!")
        print(f"{spieler1}")
        print(f"{spieler2}")
        if change - 1>0:
            sägeblatt -= 0
        sägeblatt -= 1 - change
    elif sum1 > sum2:
        print("spieler 1 gewinnt")
        print(f"{spieler1}")
        print(f"{spieler2}")
        sägeblatt -= 1 - change
    elif sum1 < sum2:
        print("spieler 2 gewinnt")
        print(f"{spieler1}")
        print(f"{spieler2}")
        sägeblatt += 1 + change
    

    if sägeblatt <1:
        sägeblatt = 1
    if sägeblatt > 13:
        sägeblatt = 13


    if bless == 1:
        if sägeblatt <= 1:
            sägeblatt = 2
            print("spieler2 wurde verschont durch bless")
        if sägeblatt >= 13:
            sägeblatt = 12
            print("spieler1 wurde verschont durch bless")
        


    print("Das Sägeblatt steht auf", sägeblatt , sep=" ")






