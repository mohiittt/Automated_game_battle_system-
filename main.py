import random
import os, time

def rollDice(sides):
  result = random.randint(1,sides)
  return result

def roll_1():
  health = (rollDice(6) * rollDice(12))/2 + 10
  return health

def roll_2():
  strength = (rollDice(6) * rollDice(12))/2 + 10
  return strength 


print("⚔️  BATTLE DAY ⚔️")
character_1 = input("Name your Legend : ")
Character_type = input("Character type (Human, Elf, Wizard, Orc) : ")
print()
print(character_1)
health_1 = roll_1()
print("HEALTH : ", health_1 ) 
strength_1 = roll_2()
print("STRENGTH : ", strength_1)
print()

print("Who are they battling?")
print()

character_2 = input("Name your Legend : ")
type = input("Character type (Human, Elf, Wizard, Orc) : ")
print()
print(character_2)
health_2 = roll_1()
print("HEALTH : ", health_2 ) 
strength_2 = roll_2()
print("STRENGTH : ", strength_2)
print()

round = 1
winner = None

while True:
  time.sleep(1)
  os.system("clear")

  print("⚔️  BATTLE TIME ⚔️")
  print()
  print("The battle begins!")
  print()

  c1Dice = rollDice(6)
  c2Dice = rollDice(6)
  difference = abs(strength_1 - strength_2) + 1
  if c1Dice > c2Dice:
    health_2 -= difference
    if round==1:
      print(character_1, "wins the first blow")
    else:
      print(character_1, "wins round", round)
  elif c2Dice > c1Dice:
    health_1 -= difference
    if round==1:
      print(character_2, "wins the first blow")
    else:
      print(character_2, "wins round", round)
  else:
    print("Their swords clash and they draw round", round)
  print()
  print(character_1)
  print("HEALTH:", health_1)
  print()
  print(character_2)
  print("HEALTH:", health_2)
  print()
  if health_1<=0:
    print(character_1, "has died!")
    winner = character_2
    break
  elif health_2<=0:
    print(character_2, "has died!")
    winner = character_1
    break
  else:
    print("And they're both standing for the next round")
    round += 1

  time.sleep(3)
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  print(winner, "has won in", round, "rounds")





    

  
