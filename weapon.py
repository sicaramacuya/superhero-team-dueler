from ability import Ability
from random import randint

class Weapon(Ability):

    def attack(self):
        """This method returns a random value between one half to the full attack power of the weapon"""
        
        half_max_damage = int(self.max_damage) // 2
        random_value = randint(half_max_damage, int(self.max_damage))

        return random_value

if __name__ == '__main__':
    # If you run this file from the terminal this block is executed.
    
    dimond_sword = Weapon('Dimond Sword', 300)
    print(f'{dimond_sword.name}\'s attack damage: {dimond_sword.attack()}')