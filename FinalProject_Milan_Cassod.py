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
        self.health -= damage
        
    #returns name
    def getName(self):
        return self.name

# if the player chooses the knight character, the methods in 
# this class will be used        
class Knight(Character):
    def __init__(self):
        self.name = "Knight"
        self.health = 100
        
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
    def chooseMove(self):
        
        move = ""
        damage = 0
        
        hit = False
      
        while move.upper() not in ["S", "SWORD", "P", "SPEAR", "B", "BATTLEAXE"]:
            print("\nChoose a move!")
            print("\n(S)word - Your trusty sword is no great weapon, but it never fails! (5 damage)")
            print("S(p)ear - Your spear is powerful, but you're still learning to use it! (10 damage)")
            print("(B)attleaxe - Your battleaxe is your most fearsome weapon, if a little unpredictable! (20 damage)")
            
            move = input()
            
        
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
            
        
# if the player chooses the dragon opponent, the methods in 
# this class will be used        
class Dragon(Character):
    def __init__(self):
        self.name = "Dragon"
        self.health = 100
           
    def fireball(self):
        print()
        print("The dragon hit you with a small fireball! (5 damage)")
        return True
            
    def wingFlap(self):
        print()
        # spear has a 1/3 chance of hitting
        hit = random.randint(1, 3)
        
        print("The dragon tries to unbalance you by flapping its wings.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("You were knocked down! (10 damage)")
            return True
        else:
            print("You held your ground! (No damage)")
            return False
        
    def flameColumn(self):
        print()
        # battleaxe has a 1/10 chance of hitting
        hit = random.randint(1, 10)
        
        print("The dragon tries to hit you with a column of flame.")
        time.sleep(1)
        
        # if the spear hits, remove health from the opponent
        if hit == 1:
            print("You were hit! (20 damage)")
            return True
        else:
            print("The dragon missed! (0 damage)")
            return False
        
    def chooseMove(self):
        
        move = random.choice([1,1,1,2,2,3])
        
        damage = 0
        
        hit = False
     
        # damage depends on the move and whether it hits
        # if the move doesn't hit, damage = 0
        if move == 1:
            hit = self.fireball()
            if hit:
                damage = 5
            else:
                damage = 0
        elif move == 2:
            hit = self.wingFlap()
            if hit:
                damage = 10
            else:
                damage = 0
        elif move == 3:
            hit = self.flameColumn()
            if hit:
                damage = 20
            else:
                damage = 0
                
        return damage
        
def main():
    
    #Game intro
    # Character selection - will add more choices as more characters are developed
    print("Welcome to the Arena!")
    print("To choose an action, type its name or the highlighted character.")
    
    # the hero is the character the player will play as
    # while loop makes sure the user inputs a valid choice for the hero
    heroChosen = False
    while heroChosen == False:
        print("\nType the name or first letter to choose your character:")
        heroChoice = input("(K)night\n")
        if heroChoice.upper() in ["K", "KNIGHT"]:
            heroChosen = True
            hero = Knight()
    
    # player chooses opponent
    villainChosen = False
    while villainChosen == False:
        print("\nType the name or first letter to choose your character:")
        villainChoice = input("(D)ragon\n")
        if villainChoice.upper() in ["D", "DRAGON"]:
            villainChosen = True
            villain = Dragon()
    
    print("\nPreparing the arena for " + hero.getName() + " vs. " + villain.getName() + "...")
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
            sleep(1)
            print(hero.getName().upper() + " DEFEATS " + villain.getName().upper())
            print("Congratulations on your victory!")
            gameOn = False
        elif not hero.stillAlive():
            sleep(1)
            print(villain.getName().upper() + " DEFEATS " + hero.getName().upper())
            print("Better luck next time!")
            gameOn = False
        else:
            time.sleep(1)
            print("\n" + hero.getName() + "'s" + " turn!")
            damage = hero.chooseMove()
            # villain takes damage depending on damage amounts defined in chooseMove
            villain.takeDamage(damage)
            print()
            time.sleep(1)
            hero.printHealth()
            villain.printHealth()
            time.sleep(1)
            print()
            print("\n" + villain.getName() + "'s" + " turn!")
            time.sleep(1)
            damage = villain.chooseMove()
            hero.takeDamage(damage)
            print()
            time.sleep(1)
            hero.printHealth()
            villain.printHealth()
            time.sleep(1)
        
        
        
        
        
    
        
main()

# So far, we have a basic setup just to get the idea down for one move
# and for coding with OOP for a game
# We plan to get started very soon on getting the player 1 functionality solid
# Then, we will deal with the opposing computer moves
# Finally, we'll tackle what a GUI will look like--for now, we just want
# The game to work