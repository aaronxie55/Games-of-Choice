import random

money = 100

#Write your game of chance functions here

#flipping function
def flipping(bet, call):
  print("---------------------------")
  print("Start playing flip coin!")
  print("---------------------------")
  #make sure bat is valid
  if bet < 0:
    print("Bet must be valid")
    return 0
  num = random.randint(1, 2)
  if num == 1:
    ans = "Heads"
  else:
    ans = "Tails"
  print("We got a "+ ans)
  if call == ans:
    print("You win "+ str(bet))
    return bet
  else:
    print("You lost -"+ str(bet))
    return -bet
  
  
#cho_han function 
def cho_han(bet, call):
  print("---------------------------")
  print("Start playing Cho-Han!")
  print("---------------------------")
  #make sure bat is valid
  if bet < 0:
    print("Bet must be valid")
    return 0
  num1 = random.randint(1, 6)
  print("The first dice is "+ str(num1))
  num2 = random.randint(1, 6)
  print("The second dice is "+str(num2))
  total = num1 + num2
  print("The total is " + str(total))
  if total%2 != 0:
    ans = "Odd"
    print("We got a odd number!")
  else:
    ans = "Even"
    print("We got a even number!")
  if call == ans:
    print("You win "+ str(bet))
    return bet
  else:
    print("You lost -"+ str(bet))
    return -bet


def picking_card(bet):
  print("---------------------------")
  print("Start playing Picking Card!")
  print("---------------------------")
  #make sure bat is valid
  if bet < 0:
    print("Bet must be valid")
    return 0
  deck = []
  for card in range(1,53):
    l = [card] * 4
    deck.extend(l)
  num1 = random.choice(deck)
  deck.remove(num1)
  print("The number you choose is " + str(num1))
  num2 = random.choice(deck)
  deck.remove(num2)
  print("The number I choose is " + str(num2))
  if num1 > num2:
    print("You win "+ str(bet))
    return bet
  elif num1 < num2:
    print("You lost -"+ str(bet))
    return -bet
  else:
    print("It is a tie.")
    return 0

def roulette(bet, call):
  print("---------------------------")
  print("Start playing Roulette!")
  print("---------------------------")
  pockets = [pocket for pocket in range(0, 38)]
  num = random.choice(pockets)
  #make sure bat is valid
  if bet < 0:
    print("Bet must be valid")
    return 0
  #make sure call is valid
  if call == 00:
    call = 37
  if num == 37:
    print("The number we got is 00")
  else:
    print("The number we got is " + str(num))
  if isinstance(call, str):
    if num == 0 or num == 37:
      print("You are not gussing specific number.")
      print("You lost -"+ str(bet))
      return -bet
    if num%2 != 0:
      ans = "Odd"
      print("We got a odd number!")
    else:
      ans = "Even"
      print("We got a even number!")
    if call == ans:
      print("You win "+ str(bet))
      return bet
    else:
      print("You lost -"+ str(bet))
      return -bet   
  if call == num:
    print("Congrate. You get the right number!")
    print("You win " + str(bet*35))
    return bet*35
  else: 
    print("You lost " + str(bet))
    return -bet






#Call your game of chance functions here
money += flipping(20, "Tails")
money += cho_han(20, "Odd")
money += picking_card(20)
money += roulette(20, 00)
print("Now you have " + str(money))