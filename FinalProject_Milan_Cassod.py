#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:18:19 2024

@author: devin
"""

import random
import time

# this class contains methods including both heroes (player) and villains (computer)
class Character:
    # Every character has a name and a health amount
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    #checks if the character's health > 0
    def stillAlive(self):
        if self.health > 0:
            # If it is, the character is still alive
            return True
        
    #prints a status update on character's health
    def printHealth(self):
        # Display health
        print(f"{self.name}'s Health: {self.health}")
        
    # subtracts health
    def takeDamage(self, damage):
        # Sets health to 0 if damage would give negative health to the player
        if damage >= self.health:
            self.health = 0
        else: self.health -= damage

        
    #returns name
    def getName(self):
        return self.name

# if the player chooses the knight character, the methods in 
# this class will be used        
# Similarly, the computer can use these methods as well
class Knight(Character):
    def __init__(self,name):
        # Defines the name and health of 100 at the character level
        super().__init__(name,100)
        
    # First move -- hits every time
    def swordHit(self):
        print()
        print(f"{self.name}'s sword hit successful!")
        # The return true references returning that a move was in fact successful
        # Line 93 demonstrates its use
        return True
                
    def spearHit(self):
        print()
        # spear has a 1/2 chance of hitting
        hit = random.randint(1, 2)
            
        # if the spear hits, remove health from the opponent
        # This is done below in lines 90-109
        if hit == 1:
            print(f"{self.name}'s spear hit successful!")
            return True
        else:
            print(f"{self.name}'s spear missed!")
            return False
            
    def battleaxeHit(self):
        print()
        # battleaxe has a 1/4 chance of hitting
        hit = random.randint(1, 4)
            
        if hit == 1:
            print(f"{self.name}'s battleaxe hit successful!")
            return True
        else:
            print(f"{self.name}'s battleaxe missed!")
            return False
    
    # print the move options 
    def chooseMove(self,move):
        
        damage = 0
        
        hit = False            

        
        # This actually executes the move/function
        # damage depends on the move and whether it hits
        # if the move doesn't hit, damage = 0
        if move.upper() == "S" or move.upper() == "SWORD":
            hit = self.swordHit()
            if hit:
                damage = 5
            else:
                damage = 0
        elif move.upper() == "P" or move.upper() == "SPEAR":
            hit = self.spearHit()
            if hit:
                damage = 10
            else:
                damage = 0
        elif move.upper() == "B" or move.upper() == "BATTLEAXE":
            hit = self.battleaxeHit()
            if hit:
                damage = 20
            else:
                damage = 0
                
        return damage
            
    # When it's a players turn, its available moves are displayed
    def printMoves(self):
        print("\nChoose a move!")
        print("\n(S)word - Your trusty sword is no great weapon, but it never fails! (5 damage)")
        print("S(p)ear - Your spear is powerful, but you're still learning to use it! (10 damage)")
        print("(B)attleaxe - Your battleaxe is your most fearsome weapon, if a little unpredictable! (20 damage)")
        
    # Checks if the move requested is valid
    # If not, the program will re-run the input and no hit will be performed
    # Until a valid move is selected
    def isValidMove(self,move):
        if move.upper() in ["S", "SWORD", "P", "SPEAR", "B", "BATTLEAXE"]:
            return(True)
        else: return(False)
        
    # Chooses the computer's move
    def computerChoice (self):
        # Random.choice will choose one of the list items
        # Some are more frequent because they do less damage and are more likely to hit
        # This makes the enemy more balanced 
        move = random.choice(['S','S','S','S','P','P','B'])
        # When move is returned, it'll be used to call the choose move function
        return(move)     

    # Heal takes self and the amount to heal
    # Amount healed is defined in the nature class
    def heal(self,amtheal):
        # If the amount healed is going to exceed the players total health
        # Cap it at full health
        if self.health + amtheal > 100:
            print(f"{self.name} healed {100-(self.health)} health to 100 health")
            self.health = 100
            print()
        else: 
            # Otherwise, add amount to heal to total health
            self.health += amtheal
            print(f"{self.name} healed {amtheal} health to {self.health} health")
            print()
        
# if the player chooses the dragon character, the methods in 
# this class will be used        
# Similarly, the computer can use these methods as well
class Dragon(Character):
    def __init__(self,name):
        super().__init__(name,100)
           
    def fireball(self):
        print()
        print(f"{self.name} hits with a small fireball! (5 damage)")
        return True
            
    def wingFlap(self):
        print()
        # Wing flap has 1 in 3 chance of hitting
        hit = random.randint(1, 3)
        
        print(f"{self.name} tries to unbalance their opponent by flapping their wings.")
        time.sleep(1)
        
        # if wing flap hits, remove health from the opponent
        if hit == 1:
            print(f"{self.name} knocked their enemy down! (15 damage)")
            return True
        else:
            print(f"{self.name}'s enemy held their ground! (No damage)")
            return False
        
    def flameColumn(self):
        print()
        # flamecolumn has a 1/7 chance of hitting
        hit = random.randint(1, 7)
        
        print(f"{self.name} tries to hit with a column of flame.")
        time.sleep(1)
        
        # if it hits, remove health from the opponent
        if hit == 1:
            print(f"{self.name} hit their enemy! (30 damage)")
            return True
        else:
            print(f"{self.name} missed! (0 damage)")
            return False
    
    # Same functionality as chooseMove in Knight class
    # Demonstration of polymorphism
    def chooseMove(self,move):
        
        damage = 0
        
        hit = False            
        
        # damage depends on the move and whether it hits
        # if the move doesn't hit, damage = 0
        if move.upper() == "F" or move.upper() == "FIREBALL":
            hit = self.fireball()
            if hit:
                damage = 5
            else:
                damage = 0
        elif move.upper() == "W" or move.upper() == "WINGFLAP":
            hit = self.wingFlap()
            if hit:
                damage = 15
            else:
                damage = 0
        elif move.upper() == "C" or move.upper() == "COLUMN":
            hit = self.flameColumn()
            if hit:
                damage = 30
            else:
                damage = 0
                
        return damage
            
    # Prints available dragon moves to player -- only runs if player is dragon
    # If computer is dragon, this skips
    def printMoves(self):
        print("\nChoose a move!")
        print("\n(F)ireball - Your fireball is shortlived, but it always burns! (5 damage)")
        print("(W)ingflap - Your wings hold great power! But be careful: they're hard to aim (15 damage)")
        print("(C)olumn - Your column of fire is big and wondrous...but sometimes the cold doesn't let it ignite (30 damage)")
        
    # Checks if move input is one of the accepted dragon moves
    def isValidMove(self,move):
        if move.upper() in ["F", "FIREBALL", "W", "WINGFLAP", "C", "COLUMN OF FLAME"]:
            return(True)
        else: return(False)
        
    # Specialized choices for dragon
    # Dragon takes more chance than knight--makes for a different experience
    def computerChoice (self):
        move = random.choice(['F','F','W','W','W','W','C'])
        return(move)
    
    # Same functionality as knight class heal method - see above for comments
    def heal(self,amtheal):
        if self.health + amtheal > 100:
            print(f"{self.name} healed {100-(self.health)} health to 100 health")
            print()
            self.health = 100
        else: 
            self.health += amtheal
            print(f"{self.name} healed {amtheal} health to {self.health} health")
            print()

# if the player chooses the dragon character, the methods in 
# this class will be used    
# Similarly, the computer can use these methods as well
class Wizard(Character):
    # Wizards has 125 health
    # As a consequence, its moves do less damage on average
    def __init__(self,name):
        super().__init__(name,125)
           
    # Similar to the other two, this is the "always hitting" method
    def poisonPotion (self):
        print()
        print(f"{self.name} poisoned their enemy! (6 damage)")
        return True
            
    def summonArrows(self):
        print()
        # arrows have a 1/3 chance of hitting
        hit = random.randint(1, 3)
        
        print("Arrows are raining from the sky!")
        time.sleep(1)
        
        # if the arrows hit, remove health from the opponent
        if hit == 1:
            print(f"{self.name} successfully weakened their enemy with the arrows! (9 damage)")
            return True
        else:
            print(f"{self.name} missed...this time! (No damage)")
            return False
        
    def earthquake(self):
        print()
        # earthquake has a 1/5 chance of hitting
        hit = random.randint(1, 5)
        
        print(f"{self.name} casts an earth shattering spell.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print(f"{self.name} knocked down the enemy due to the averse shaking! (13 damage)")
            return True
        else:
            print(f"{self.name} missed! (0 damage)")
            return False
        
    # Special ability -- healing potion
    def healPotion(self):
        print()
        print(f"{self.name} attempts to heal themself!")
        time.sleep(1)

        # Picks a random integer from 1 to 3
        hit = random.randint(1,3)
        
        # If health is full, automatically fail
        if self.health == 125:
            print("Healing potion failed!")
            # This is needed to make sure the program knows no attack is done
            return False
        # 2 in 3 chance of a successful heal 
        if hit == 1 or hit == 2:
            print(f"{self.name} successfully healed themself")
            # Amount healed can be 2, 5, or 8 health
            # The lower health increments are more frequent in the list
            # This makes it more simpler than just simply picking between a value
            # Kind of like a lottery scratch off, you're more likely
            # To get a lesser value when you win
            amtheal = random.choice([2,2,2,2,2,2,5,5,5,5,8,8])
            # Runs the heal function in the class
            self.heal(amtheal)
            # This is needed to make sure the program knows no attack is done
            return False
           
    # Same functionality as knight and dragon heal methods
    def heal(self,amtheal):
        if self.health + amtheal > 125:
            print(f"{self.name} healed {125-(self.health)} health to 125 health")
            print()
            self.health = 125
        else: 
            self.health += amtheal
            print(f"{self.name} healed {amtheal} health to {self.health} health")
            print()
        
    # Same functionality as Dragon and Knight classes
    def chooseMove(self,move):
        
        damage = 0
        
        hit = False            
        
        # damage depends on the move and whether it hits
        # if the move doesn't hit, damage = 0
        if move.upper() == "P" or move.upper() == "POISON":
            hit = self.poisonPotion()
            if hit:
                damage = 6
            else:
                damage = 0
        elif move.upper() == "A" or move.upper() == "ARROWS":
            hit = self.summonArrows()
            if hit:
                damage = 9
            else:
                damage = 0
        elif move.upper() == "E" or move.upper() == "EARTHQUAKE":
            hit = self.earthquake()
            if hit:
                damage = 13
            else:
                damage = 0
        elif move.upper() == "H" or move.upper() == "HEAL":
            hit = self.healPotion()

                
        return damage
    
    # Prints available moves to the console 
    # ONLY runs when the player is a wizard
    # If the computer is a wizard, it will choose a move and bypass this
    def printMoves(self):
        print("\nChoose a move!")
        print("\n(P)oison - Your poison potion is handy, but a bit cliche (6 damage)")
        print("(A)rrows - Your arrow storm might not always hit, but when it does, it hurts! (9 damage)")
        print("(E)arthquake - Your earthquake shakes the world around it...including your opponent (13 damage)")
        print("(H)eal - Heal yourself at the expense of no damage to the opponent. Be careful..your spell doesn't always work (+3 health)")
        
    # Checks if a requested move is in the moves for the character
    def isValidMove(self,move):
        if move.upper() in ["P", "POISON", "A", "ARROWS", "E", "EARTHQUAKE","H","HEAL"]:
            return(True)
        else: return(False)
        
    # Availability of computer to choose moves
    def computerChoice (self):
        # Pretty even split for wizard
        move = random.choice(['P','P','P','A','A','A','E','E','H','H'])
        return(move)
    
class Nature:
    # This variable is accessible to the entire class
    # This allows us to make a multi-turn debuff -- see line 440
    started = 0
    
    # This function runs after both characters make their move
    def natureSelect(charObj1,charObj2):
        # python chooses a number between 1 and 3 for the player and villain
        choiceP = random.randint(1,3)
        choiceV = random.randint(1,3)
        
        # Lightning method ran on player if its "dice roll" is 1
        if choiceP == 1:
            Nature.lightning(charObj1)
        # Golden apple method ran on player if its  "dice roll" is 3
        elif choiceP == 3:
            Nature.goldenApple(charObj1)
        # Runs acid rain method on BOTH player and villain if "dice roll" is 2
        elif (choiceP == 2 or choiceV == 2) and Nature.started == 0:
            Nature.acidRain()
            Nature.rainAttack(charObj1,charObj2)
        # Reruns the acid rain attack method until the storm is over
        # The storm ends 2 turns after the first attack
        elif Nature.started > 0:
            Nature.rainAttack(charObj1,charObj2)
        # Runs lightning method on villain if its "dice roll" is 1
        if choiceV == 1:
            Nature.lightning(charObj2)
        # Runs golden apple method on villain if its "dice roll" is 3
        elif choiceV == 3:
            Nature.goldenApple(charObj2)
            
    
    def lightning(charObj):
        # Lightning has 1 in 7 chance of striking
        # Combined with 1 in 3 chance of being picked, it's a 1 in 21 chance
        # Of a lightning attack at random
        light = random.randint(1,7)
        if light == 1:
            print("Oh no!")
            time.sleep(1)
            print(f"{charObj.name} has been struck by lightning! -20 health")
            print()
            time.sleep(1)
            # Deducts 20 health from the struck character
            charObj.health -= 20
            
    def acidRain():
        # 1 in 5 * 1 in 3 makes a 1 in 15 chance for acid rain
        rain = random.randint(1,5)
        if rain == 1:
            print("Oh no!")
            time.sleep(1)
            print("An acid rain storm has appeared!")
            # Modifies the class variable "started"
            # See below function for this variable's functionality
            Nature.started = 3
           
    def rainAttack(charObj1,charObj2):
        # if acid rain strikes, this condition is true
        if Nature.started > 0:
            time.sleep(1)
            print()
            print(f"{charObj1.name} has been burned by the acid! -4 health")
            print()
            print(f"{charObj2.name} has been burned by the acid! -4 health")
            print()
            time.sleep(1)
            charObj1.health -= 4
            charObj2.health -= 4
            # This signifies the end of the acid rain
            # This works because once the decrement occurs, started = 0
            # This means next turn there will be no acid rain hit
            if Nature.started == 1:
                print("The acid rainstorm is now over")
            # Decrement "started by 1"
            # AKA, acid rain lasts 3 turns
            Nature.started -= 1
                
    def goldenApple(charObj):
        # 1 in 15 chance (1 in 5 * 1 in 3) 
        apple = random.randint(1,5)
        # If "dice roll" returns 1
        if apple == 1:
            # The character can heal either 4,9,11,18,or 50 health
            # The frequency of the numbers helps balance how often they're
            # Picked
            amtheal = random.choice([4,4,4,4,4,9,9,9,9,11,11,11,18,18,50])
            time.sleep(1)
            print(f"{charObj.name} found a healing golden apple!")
            time.sleep(1)
            # Calls heal method of the character object passed in
            charObj.heal(amtheal)
            
def main():
    #Game intro
    # Character selection - will add more choices as more characters are developed
    print("Welcome to the Arena!")
    print("To choose an action, type its name or the highlighted character.")
    
    # the hero is the character the player will play as
    # while loop makes sure the user inputs a valid choice for the hero
    name = input("What is your name? ")
    playerChosen = False
    while playerChosen == False:
        print("\nType the name or first letter to choose your character:")
        print("Your character options are: Knight, Dragon, Wizard")
        heroChoice = input("")
        print()
        if heroChoice.upper() in ["K", "KNIGHT"]:
            playerChosen = True
            print("You are a noble knight!")
            player = Knight(name)
        elif heroChoice.upper() in ["D", "DRAGON"]:
            print("You are a powerful dragon!")
            playerChosen = True
            player = Dragon(name)
        elif heroChoice.upper() in ["W", "WIZARD"]:
            print("You are a magical wizard!")
            playerChosen = True
            player = Wizard(name)
            
    # Computer chooses its character (3 options)
    options = random.randint(1,3)
    # time.sleep sets a 1 minute delay before showing the next line
    # It is a purely visual element to make the game more game like
    time.sleep(1)
    # 1 = dragon
    if options == 1:
        print("Your opponent is a blood-hungry dragon!")
        villain = Dragon("Dragon")
    # 2 = knight
    if options == 2:
        print("Your opponent is a traitorous knight!")
        villain = Knight("Knight")
    # 3 = wizard
    if options == 3:
        print("Your opponent is a magical wizard!")
        villain = Wizard("Wizard")
    
    # Purely visual -- "loading"
    time.sleep(1)
    print("\nPreparing the arena for " + player.getName() + " vs. " + villain.getName() + "...")
    time.sleep(2)
    print("\nThe arena is ready!")
    time.sleep(1)
    print("\n.")
    time.sleep(1)
    print("\n.")
    time.sleep(1)
    print("\n.")
    time.sleep(1)
    print("\nFIGHT!")
    
    # game continues while neither of the characters have died (while gameOn == true)
    gameOn = True
    
    while gameOn:
        # If villain is dead
        if not villain.stillAlive():
            time.sleep(1)
            print("\n" + player.getName().upper() + " DEFEATS " + villain.getName().upper())
            print("Congratulations on your victory!")
            gameOn = False
        # If player is dead
        elif not player.stillAlive():
            time.sleep(1)
            print("\n" + villain.getName().upper() + " DEFEATS " + player.getName().upper())
            print("Better luck next time!")
            gameOn = False
        else:
            time.sleep(1)
            print("\n" + player.getName() + "'s" + " turn!")
            # Prints player's possible moves
            # Works for any character (inheritance)
            player.printMoves()
            move = input("\nWhat move would you like to make? ")
            # If the player's move is invalid, it prompts them again until it isn't 
            while not player.isValidMove(move):
                move = input("\nWhat move would you like to make? ")
            # the chooseMove function returns damage, as we saw above
            damage = player.chooseMove(move)
            # villain takes damage depending on damage amounts defined in chooseMove
            # This method will then subtract that from the villain's health
            villain.takeDamage(damage)
            print()
            # Print the health of both characters
            time.sleep(1)
            player.printHealth()
            villain.printHealth()
            time.sleep(2)
            print()
            print("\n" + villain.getName() + "'s" + " turn!")
            time.sleep(1)
            # Villain chooses its move, inputting the result from the 
            # Computer choice method as the move variable
            # Reference the method for more info
            damage = villain.chooseMove(villain.computerChoice())
            # Player takes damage the same way
            player.takeDamage(damage)
            print()
            time.sleep(1)
            # Runs the nature select function, which will choose
            # 1 of 3 nature events (golden apple, acid rain, lightning)
            # Then, it runs the corresponding method, which has its 
            # Own hit probability 
            Nature.natureSelect(player,villain)
            time.sleep(1)
            # Finally, print health after villain's hit AND possible
            # Random event
            player.printHealth()
            villain.printHealth()
            time.sleep(2)
        
        
main()
