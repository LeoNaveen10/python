from argparse import RawDescriptionHelpFormatter
from pprint import pprint
import random


for i in range(3):
    print(random.random())
    
names = ['ronaldo','messi','neymar','pele','maradona']
print(random.choices(names))


#dice game

class Dice:
    def roll(self):
        first = random.randint(1,6);
        second = random.randint(1,6);
        return first,second
dice = Dice();
print(dice.roll());