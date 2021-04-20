import random 

from Black_jack.OBOBlackjack.art import logo

# function for dealing random cards
def draw_card(cards):
  hand = random.sample(cards,2)
  return hand

#hit me function
def hit(hand,deck):
  hitme = random.choice(deck)
  hand.append(hitme)
  return hand

#change 11 to 1 
def iface(hand):
    if 11 in hand:
        for i in range(len(hand)):
            if hand[i] == 11:
                hand[i]= 1
                break
    return hand 
  
#score
def score(hand):
  scor = sum(hand)
  return scor

#######

#deck list
deck = [11,2,3,4,5,6,7,8,9,10,10,10,10]

#deal cards
comp_hand = draw_card(deck)
your_hand = draw_card(deck)

#### could add play again here 

# user input do you want to play 
print(logo)
start= input("do you want to play blackjack? Enter 'Y' or 'N: ").lower()

if start == 'y':
  print(f"Your hand: {your_hand[:]}")
  print(f"Computers hand: {comp_hand[0]}, X")



##### A WHILE LOmp

#flag up here?
active = True
while active:

# add current score 
  comp_score = score(comp_hand)
  your_score = score(your_hand)



# koes user or comp have bj?
  if your_score == 21:
    active = False
    compplays = False
    print(f'you win! final score: {your_score}. BlackJack Baby!!!')

  if comp_score == 21:
    compplays = False
    print(f'you lose! final score:{your_score}, comp: {comp_score}. BlackJack Baby!!!')
    active = False


#is score over 21? 
## is there an 11, if its 1 is it still over?

  
  if your_score > 21:
    if 11 in your_hand:
      new_hand = iface(your_hand)
      your_score = score(new_hand)
      continue
    active = False
    compplays = False
    
  

  if your_score < 21:
    ans = input("want another card? 'Y' or 'N': ").lower()
    if ans == 'y':
      your_hand = hit(your_hand, deck)
      your_score= score(your_hand)
      print(your_hand)
      print(f"your score :{your_score}")
    if ans == 'n':
      print(your_score)
      
      if comp_score <= 17:
          new_comphand = hit(comp_hand, deck)
          comp_score = score(new_comphand)
          active = False
      elif comp_score > 17:
        active = False


#put inside while loop as if ans == 'n'
compplays= True
while compplays:
  
  if comp_score <= 17:
    comp_hand = hit(comp_hand, deck)
    comp_score = score(comp_hand)
  

  if comp_score > 17:
    compplays = False
  

if comp_score > 21:
  print(f'you win! comp score:{comp_score},comp hand: {comp_hand}. Your score: {your_score}, your hand: {your_hand}')
elif your_score > 21:
  print(f'you Lose! comp score: {comp_score}{comp_hand}. Your score: {your_score},{your_hand}')
elif your_score > comp_score: 
  print(f'you win! comp_score:{comp_score}. Your score: {your_score}')
elif your_score < comp_score:
  print(f'you lose! comp_score:{comp_score}. Your score: {your_score}')















