#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 13:18:19 2024

@author: devin
"""

# Eventually we plan to have child classes based on the character selected
# As certain moves/methods will only be for certain characters


class Player():
    def __init__(self, name, characterChosen):
        self.health = 100
        self.name = name
        self.characterChosen = characterChosen
           
    # Our first move, very basic
    # We are currently brainstorming cool twists to add to make the code interesting
    def swordHit(self, opponent):
        print("Sword hit successful!")
        opponent.health -= 10
        
def main():
    #characterChosen = input("Enter the name of your character: ")
    # Just setting simple players
    player1 = Player('Devin','X')
    otherPlayer = Player('Computer', 'X')
    
    # Soon, we will have the moves switch between players
    moveChoose = eval(input("Choose a move: "))
    if moveChoose == 1:
        # Having player 1 go first, player 1 evokes sword hit on the opponent's
        # object
        # Eventually, we want the second object to be computerized/non playable
        player1.swordHit(otherPlayer)
        print(f"Currently, {player1.name} has a health of {player1.health}")
        print(f"{otherPlayer.name} has a health of {otherPlayer.health}")
        
        
main()

# So far, we have a basic setup just to get the idea down for one move
# and for coding with OOP for a game
# We plan to get started very soon on getting the player 1 functionality solid
# Then, we will deal with the opposing computer moves
# Finally, we'll tackle what a GUI will look like--for now, we just want
# The game to work