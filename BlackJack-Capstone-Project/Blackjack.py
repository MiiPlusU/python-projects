import random
main_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Player metrics
player_deck=random.sample(main_deck,2)
player_score=0

# Player Total Score
for index in range(len(player_deck)):
    player_score+=player_deck[index]

# Dealer Deck
dealer_deck=random.sample(main_deck,2)
dealer_score=0

random_num=(random.choice(main_deck))

# Dealer Total Score
dealer_deck.append(random_num)
dealer_score=sum(dealer_deck)

# Question
decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()



if player_score>21 and 11 in player_deck:
    for i in range(len(player_deck)):
        if player_deck[i]==11:
            player_deck[i]==1
            break
if dealer_score < 17:
    dealer_deck.append(random_num)

if decision !='n' and decision !='y':
    print("invalid input")
elif decision=='n':
    print("game over")
else:
    while decision !='n':
        print(f"You cards: {player_deck}, current score: {player_score}" )
        print(f"Computer's first card: {dealer_deck[0]}")

        another_card=input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card=='n':
            print(f"Your final hand: {player_deck}, final score: {player_score}")
            print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
            if player_score > dealer_score and player_score <=21 and dealer_score<21:
                print("You were closer, you win!")
            elif dealer_score > player_score and dealer_score <=21 and player_score<21:
                print("Dealer was closer, you lose!")
            elif player_score > 21 and dealer_score > 21:
                print("Draw, you both busted")
            elif player_score <= 21 and dealer_score > 21:
                print("Dealer busted, you win")
            else:
                print("You busted, you lose")
        elif another_card !='n' and another_card !='y':
            print("invalid input")
        else:
            while another_card != 'n':
                
                # if player_score < 21:
                player_deck.append(random_num)
                    # player_score=sum(player_deck)

                player_score=0
                for card in player_deck:
                    player_score+=card
                    

                # else:
                #    continue
                    
                if player_score>21 and 11 in player_deck:
                    for i in range(len(player_deck)):
                        if player_deck[i]==11:
                            player_deck[i]==1
                            break

                if player_score > dealer_score and player_score <=21 and dealer_score<21:
                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
                    print("You were closer, you win!")
                    break
                elif dealer_score > player_score and dealer_score <=21 and player_score<21:
                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
                    print("Dealer was closer, you lose!")
                    break
                elif player_score > 21 and dealer_score > 21:
                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
                    print("Draw, you both busted")
                    break
                elif player_score <= 21 and dealer_score > 21:
                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
                    print("Dealer busted, you win")
                    break
                elif player_score == dealer_score:
                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
                    print("You both tied")
                    break
                else:
                    print(f"Your final hand: {player_deck}, final score: {player_score}")
                    print(f"Computer's final hand: {dealer_deck}, final score: {dealer_score}")
                    print("You busted, you lose")
                    break

        
        decision = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if decision !='n' and decision !='y':
            print("invalid input")
        elif decision=='n':
            print("game over")
        elif decision=='y':
            player_deck=random.sample(main_deck,2)
            dealer_deck=random.sample(main_deck,2)
            player_score=0
            dealer_score=0
            for index in range(len(player_deck)):
                player_score+=player_deck[index]
            for index in range(len(dealer_deck)):
                dealer_score+=dealer_deck[index]
            continue
        else:
            break

