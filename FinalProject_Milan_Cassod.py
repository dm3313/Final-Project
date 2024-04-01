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
    def __init__(self, name, health):
        self.name = name
        self.health = health
    
    #checks if the character's health > 0
    def stillAlive(self):
        if self.health > 0:
            return True
        
    #prints a status update on character's health
    def printHealth(self):
        print(self.name + " Health: " +str(self.health))
        
    # subtracts health
    def takeDamage(self, damage):
        if damage >= self.health:
            self.health = 0
        else: self.health -= damage
        
    #returns name
    def getName(self):
        return self.name

# if the player chooses the knight character, the methods in 
# this class will be used        
class Knight(Character):
    def __init__(self,name):
        super().__init__(name,100)
        
    def swordHit(self):
        print()
        print("Sword hit successful!")
        return True
                
    def spearHit(self):
        print()
        # spear has a 1/3 chance of hitting
        hit = random.randint(1, 3)
            
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("Spear hit successful!")
            return True
        else:
            print("Spear missed!")
            return False
            
    def battleaxeHit(self):
        print()
        # battleaxe has a 1/5 chance of hitting
        hit = random.randint(1, 5)
            
        if hit == 1:
            print("Battleaxe hit successful!")
            return True
        else:
            print("Battleaxe missed!")
            return False
    
    # print the move options 
    def chooseMove(self,move):
        
        damage = 0
        
        hit = False            
        
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
            
    def printMoves(self):
        print("\nChoose a move!")
        print("\n(S)word - Your trusty sword is no great weapon, but it never fails! (5 damage)")
        print("S(p)ear - Your spear is powerful, but you're still learning to use it! (10 damage)")
        print("(B)attleaxe - Your battleaxe is your most fearsome weapon, if a little unpredictable! (20 damage)")
        
    def isValidMove(self,move):
        if move.upper() in ["S", "SWORD", "P", "SPEAR", "B", "BATTLEAXE"]:
            return(True)
        else: return(False)
        
    def computerChoice (self):
        move = random.choice(['S','S','S','S','P','P','B'])
        return(move)

        
        
        
# if the player chooses the dragon opponent, the methods in 
# this class will be used        
class Dragon(Character):
    def __init__(self,name):
        super().__init__(name,100)
           
    def fireball(self):
        print()
        print("The dragon hits with a small fireball! (5 damage)")
        return True
            
    def wingFlap(self):
        print()
        # spear has a 1/3 chance of hitting
        hit = random.randint(1, 4)
        
        print("The dragon tries to unbalance its opponent by flapping its wings.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("Enemy knocked down! (15 damage)")
            return True
        else:
            print("Enemy held their ground! (No damage)")
            return False
        
    def flameColumn(self):
        print()
        # battleaxe has a 1/10 chance of hitting
        hit = random.randint(1, 10)
        
        print("The dragon tries to hit with a column of flame.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("The enemy was hit! (30 damage)")
            return True
        else:
            print("The dragon missed! (0 damage)")
            return False
    
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
            
    def printMoves(self):
        print("\nChoose a move!")
        print("\n(F)ireball - Your fireball is shortlived, but it always burns! (5 damage)")
        print("\n(W)ingflap - Your wings hold great power! But be careful: they're hard to aim (15 damage)")
        print("\n(C)olumn - Your column of fire is big and wondrous...but sometimes the cold doesn't let it ignite (30 damage)")
        
    def isValidMove(self,move):
        if move.upper() in ["F", "FIREBALL", "W", "WINGFLAP", "C", "COLUMN OF FLAME"]:
            return(True)
        else: return(False)
        
    def computerChoice (self):
        move = random.choice(['F','F','W','W','W','W','C'])
        return(move)

class Wizard(Character):
    def __init__(self,name):
        super().__init__(name,125)
           
    def poisonPotion (self):
        print()
        print("The Wizard poisoned its enemy! (6 damage)")
        return True
            
    def summonArrows(self):
        print()
        # spear has a 1/3 chance of hitting
        hit = random.randint(1, 4)
        
        print("Arrows are raining from the sky!.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("Enemy hit by the arrows! (9 damage)")
            return True
        else:
            print("Wizard missed the hit..this time! (No damage)")
            return False
        
    def earthquake(self):
        print()
        # battleaxe has a 1/10 chance of hitting
        hit = random.randint(1, 10)
        
        print("The wizard casts an earth shattering spell.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("The enemy fell due to the averse shaking! (13 damage)")
            return True
        else:
            print("The wizard missed! (0 damage)")
            return False
        
    def healPotion(self):
        print()
        print("The wizard attempts to heal itself!")
        time.sleep(1)

        
        hit = random.randint(1,3)
        
        if self.health == 125:
            print("Healing potion failed!")
            return False
        if hit == 1 or hit == 2:
            print("The wizard successfully healed itself")
            if self.health <= 122:
                self.health += 3
            else: self.health = 125
            return False
            
        
        
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
            
    def printMoves(self):
        print("\nChoose a move!")
        print("\n(P)oison - Your poison potion is handy, but a bit cliche (6 damage)")
        print("\n(A)rrows - Your arrow storm might not always hit, but when it does, it hurts! (9 damage)")
        print("\n(E)arthquake - Your earthquake shakes the world around it...including your opponent (13 damage)")
        print("\n(H)eal - Heal yourself at the expense of no damage to the opponent. Be careful..your spell doesn't always work (+3 health)")
        
    def isValidMove(self,move):
        if move.upper() in ["P", "POISON", "A", "ARROWS", "E", "EARTHQUAKE","H","HEAL"]:
            return(True)
        else: return(False)
        
    def computerChoice (self):
        move = random.choice(['P','P','P','A','A','A','E','E','H','H'])
        return(move)
    
    
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
        if heroChoice.upper() in ["K", "KNIGHT"]:
            playerChosen = True
            player = Knight(name)
        elif heroChoice.upper() in ["D", "DRAGON"]:
            playerChosen = True
            player = Dragon(name)
        elif heroChoice.upper() in ["W", "WIZARD"]:
            playerChosen = True
            player = Wizard(name)
            
        
    options = random.randint(1,3)
    if options == 1:
        print("Your opponent is a blood hungry dragon!")
        villain = Dragon("Dragon")
    if options == 2:
        print("Your opponent is traitorous knight!")
        villain = Knight("Knight")
    if options == 3:
        print("Your opponent is a magical wizard!")
        villain = Wizard("Wizard")
    

    print("\nPreparing the arena for " + player.getName() + " vs. " + villain.getName() + "...")
    time.sleep(1)
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
        
        
        if not villain.stillAlive():
            time.sleep(1)
            print(player.getName().upper() + " DEFEATS " + villain.getName().upper())
            print("Congratulations on your victory!")
            gameOn = False
        elif not player.stillAlive():
            time.sleep(1)
            print(villain.getName().upper() + " DEFEATS " + player.getName().upper())
            print("Better luck next time!")
            gameOn = False
        else:
            time.sleep(1)
            print("\n" + player.getName() + "'s" + " turn!")
            player.printMoves()
            move = input("What move u want? ")
            while not player.isValidMove(move):
                move = input("What move would you like to make? ")
            damage = player.chooseMove(move)
            # villain takes damage depending on damage amounts defined in chooseMove
            villain.takeDamage(damage)
            print()
            time.sleep(1)
            player.printHealth()
            villain.printHealth()
            time.sleep(1)
            print()
            print("\n" + villain.getName() + "'s" + " turn!")
            time.sleep(1)
            damage = villain.chooseMove(villain.computerChoice())
            player.takeDamage(damage)
            print()
            time.sleep(1)
            player.printHealth()
            villain.printHealth()
            time.sleep(1)
        
        
        
        
        
    
        
main()

# So far, we have a basic setup just to get the idea down for one move
# and for coding with OOP for a game
# We plan to get started very soon on getting the player 1 functionality solid
# Then, we will deal with the opposing computer moves
# Finally, we'll tackle what a GUI will look like--for now, we just want
# The game to work