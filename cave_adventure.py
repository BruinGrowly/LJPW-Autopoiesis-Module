
import random
import sys

def game_loop():
    print("Welcome to the Cave of Entropy")
    health = 100
    gold = 0
    
    while health > 0:
        cmd = input("Command (explore/rest/quit)> ")
        
        if cmd == "explore":
            chance = random.random()
            if chance > 0.7:
                print("You found gold!")
                gold = gold + 10
            else:
                print("A monster attacks!")
                health = health - 20
                
        if cmd == "rest":
            print("You rest and recover.")
            health = health + 10
            
        if cmd == "quit":
            break
            
    print("Game Over. Gold collected: " + str(gold))

class player_stats:
    def __init__(self):
        self.xp = 0
    
    def gain_xp(self, amount):
        self.xp = self.xp + amount

game_loop()
