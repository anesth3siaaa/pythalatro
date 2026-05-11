hands = [
    {"name": "High Card", "chips": 5, "mult": 1, "level": 1},
    {"name": "Pair", "chips": 10, "mult": 2, "level": 1},
    {"name": "Two Pair", "chips": 20, "mult": 2, "level": 1},
    {"name": "Three of a Kind", "chips": 30, "mult": 3, "level": 1},
    {"name": "Straight", "chips": 30, "mult": 4, "level": 1},
    {"name": "Flush", "chips": 35, "mult": 4, "level": 1},
    {"name": "Full House", "chips": 40, "mult": 4, "level": 1},
    {"name": "Four of a Kind", "chips": 60, "mult": 7, "level": 1},
    {"name": "Straight Flush", "chips": 100, "mult": 8, "level": 1},
    {"name": "Royal Flush", "chips": 100, "mult": 8, "level": 1},
    {"name": "Five of a Kind", "chips": 120, "mult": 12, "level": 1},
    {"name": "Flush House", "chips": 140, "mult": 14, "level": 1},
    {"name": "Flush Five", "chips": 160, "mult": 16, "level": 1},
]

levelAdds = [
    {"name": "High Card", "chips": 10, "mult": 1},
    {"name": "Pair", "chips": 15, "mult": 1},
    {"name": "Two Pair", "chips": 20, "mult": 1},
    {"name": "Three of a Kind", "chips": 20, "mult": 2},
    {"name": "Straight", "chips": 30, "mult": 3},
    {"name": "Flush", "chips": 15, "mult": 2},
    {"name": "Full House", "chips": 25, "mult": 2},
    {"name": "Four of a Kind", "chips": 30, "mult": 3},
    {"name": "Straight Flush", "chips": 40, "mult": 4},
    {"name": "Royal Flush", "chips": 40, "mult": 4},
    {"name": "Five of a Kind", "chips": 35, "mult": 3},
    {"name": "Flush House", "chips": 40, "mult": 4},
    {"name": "Flush Five", "chips": 50, "mult": 3},
]

cardList = [
    {"card": "Ace", "chips": 11},
    {"card": "King", "chips": 10},
    {"card": "Queen", "chips": 10},
    {"card": "Jack", "chips": 10},
    {"card": "10", "chips": 10},
    {"card": "9", "chips": 9},
    {"card": "8", "chips": 8},
    {"card": "7", "chips": 7},
    {"card": "6", "chips": 6},
    {"card": "5", "chips": 5},
    {"card": "4", "chips": 4},
    {"card": "3", "chips": 3},
    {"card": "2", "chips": 2},
]

handCardCount = {
    "High Card": 1,
    "Pair": 2,
    "Two Pair": 4,
    "Three of a Kind": 3,
    "Straight": 5,
    "Flush": 5,
    "Full House": 5,
    "Four of a Kind": 4,
    "Straight Flush": 5,
    "Royal Flush": 5,
    "Five of a Kind": 5,
    "Flush House": 5,
    "Flush Five": 5,
}

print("Balatro Calculator V1")
print("Warning: this application is in very early alpha.")


while True:
    findHand = input("Hand to play (use \"list\" for list): ").casefold()
    if findHand == "list":
        for hand in hands:
            print (hand["name"])
        continue
    handPlay = None
    for hand in hands:
        if hand["name"].casefold() == findHand:
            handPlay = hand
            break
    if handPlay is None:
        print("No such hand.")
        continue
    break

while True:
    try:
        findLevel = int(input("Hand level: "))
        break
    except ValueError:
        print("Level must be a number.")
        continue


while True:
    cardExists = True
    findCards = input("Cards to play (use \"list\" for list): ").casefold().split()
    if len(findCards) != handCardCount[handPlay["name"]]:
        print(findCards, "/", handCardCount[handPlay["name"]], " cards, type in more cards.")
        continue

    
    finalCards = 0
    for entry in findCards:
        for c in cardList:
            if c["card"].casefold() == entry:
                finalCards += c["chips"]
                break
        else:
            print("No such card.")
            cardExists = False
    if cardExists == False:
        continue

    finalLvl = findLevel - 1

    lvAdd = None
    for hand in levelAdds:
        if hand["name"].casefold() == findHand:
            lvAdd = hand
            break
    finalChips = handPlay["chips"] + finalCards + (lvAdd["chips"] * finalLvl)



    finalMult = handPlay["mult"] + (lvAdd["mult"] * finalLvl)
    finalScore = finalChips * finalMult

    print(finalScore)
    break
