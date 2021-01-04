'''
Task *. Blackjack
'''

import random
card_dict_aces = {i: 11 for i in range(1, 25)}
card_dict_persons_10 = {i: 10 for i in range(25, 121)}
card_dict_9 = {i: 9 for i in range(121, 145)}
card_dict_8 = {i: 8 for i in range(145, 169)}
card_dict_7 = {i: 7 for i in range(169, 193)}
card_dict_6 = {i: 6 for i in range(193, 217)}
card_dict_5 = {i: 5 for i in range(217, 241)}
card_dict_4 = {i: 4 for i in range(241, 265)}
card_dict_3 = {i: 3 for i in range(265, 289)}
card_dict_2 = {i: 2 for i in range(289, 313)}

card_dict = {**card_dict_2, **card_dict_3, **card_dict_4, **card_dict_4, **card_dict_5, **
             card_dict_6, **card_dict_7, **card_dict_8, **card_dict_9, **card_dict_persons_10, **card_dict_aces}

card_deck = [i for i in range(1, 313)]
random.shuffle(card_deck)

player = 0
dealer = 0

while True:
    decision = input('A card? (Y/N): ').lower()
    if decision == 'y':
        player += card_dict.get(int(card_deck.pop()))
        print(player)
        if player > 21:
            print('You lose! Too much!')
            break
        else:
            continue
    elif decision == 'n':
        break
    else:
        continue

while True:
    dealer += card_dict.get(int(card_deck.pop()))
    print('Dealer:', dealer)
    if dealer > 21:
        print('Too much! You won!')
        break
    elif player == dealer >= 14:
        print('Draw! By:', player)
        break
    elif player == 21 or dealer < player or player == dealer <= 14:
        continue
    else:
        print('You lose! Player:', player, 'Dealer:', dealer)
        break

'''
---input and output---
A card? (Y/N): y
3
A card? (Y/N): y
13
A card? (Y/N): y
16
A card? (Y/N): n
Dealer: 4
Dealer: 11
Dealer: 21
You lose! Player: 16 Dealer: 21
'''
