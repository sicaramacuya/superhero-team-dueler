from random import choice
from ability import Ability
from armor import Armor
from weapon import Weapon

class Hero:    
    # We want our hero to have a default "starting_health", so we can set that in the function header.
    def __init__(self, name, starting_health=100):
        '''Instance properties:
          name: String
          starting_health: Integer
          current_health: Integer
        '''

        # abilities and armor don't have starting values, and are set to empy lists on initialization
        self.abilities = list()
        self.armors = list()
        # we know the name of our hero, so we assign it here
        self.name = name
        # similarly, our starting health is passed in, just like name
        self.starting_health = starting_health
        # when a hero is created, their current health is always the same as their starting health (no damage taken yet!)
        self.current_health = starting_health

    def fight(self, opponent):
        '''Current Hero will take turns fighting the opponent hero passed in.'''

        # while both of the heroes are alive this loop will keep running.
        while self.is_alive() == True and opponent.is_alive() == True:

            # if both heroes have no abilities it will be a draw.
            if  len(self.abilities) == 0 and len(opponent.abilities) == 0:
                print("Draw")
                break

            # if there is at least one heroe with an ability this else statement will run.
            else:
                self.take_damage(opponent.attack())
                opponent.take_damage(self.attack())


            # if self is dead it will enter this if
            if self.is_alive() == False:
                print(f'{opponent.name} won the fight!')

            # if opponent is dead it enter this elif
            elif opponent.is_alive() == False:
                print(f'{self.name} won the fight!')

    def add_ability(self, ability):
        """Add ability to abilitites list."""

        self.abilities.append(ability)

    def attack(self):
        """Calculate the total damage from all ability attacks. return: total_damage: Int"""

        # start out total out at 0
        total_damage = 0
        # add the damage of each attack to our running total
        for ability in self.abilities:
            # add the damage of each attack to our running total
            total_damage += ability.attack()

        return total_damage
    
    def add_armor(self, armor):
        """Add armor to armor list."""

        self.armors.append(armor)

    def defend(self):
        """Calculate the total block amount from all armor blocks. return: total_block: Int"""

        # start out total out at 0
        total_block = 0
        # add the damage of each attack to our running total
        for armor in self.armors:
            # add the damage of each attack to our running total
            total_block += armor.block()
        
        return total_block

    def take_damage(self, damage):
        """Updates self.current_health to reflect the damage minus the defense."""

        # storing the total value of all defenses for the object
        defense = self.defend()

        # the only time the health is going to take damage is when the defense can't block the hole damage.
        if defense < damage:
            damage_taken = damage - defense
            self.current_health -= damage_taken

    def is_alive(self):
        """Return True of False depending on whether the hero is alive or not."""

        if self.current_health <= 0:
            return False
        else:
            return True
    
    def add_weapon(self, weapon):
        """Add weapon to self.abilities"""

        self.abilities.append(weapon)


if __name__ == "__main__":
    # If you run this file from the terminal this block is executed.
    # wonder_women = Hero("Wonder Women", 100)
    # super_man = Hero("Super Man", 100)

    # wonder_women.take_damage(150)
    # print(wonder_women.is_alive())
    # wonder_women.take_damage(15000)
    # print(wonder_women.is_alive())


    # attack_1 = Ability("Right Punch", 50)
    # attack_2 = Ability("Righ Kick", 90)
    # defense_1 = Armor("Punch Block", 50)
    # defense_2 = Armor("Kick Block", 90)

    # wonder_women.add_ability(attack_1)
    # wonder_women.add_ability(attack_2)
    # super_man.add_ability(attack_1)
    # super_man.add_ability(attack_2)

    # wonder_women.add_armor(defense_1)
    # wonder_women.add_armor(defense_2)
    # super_man.add_armor(defense_1)
    # super_man.add_armor(defense_2)

    # wonder_women.fight(super_man)

    # print(f'{wonder_women.name}\'s current attack is: {wonder_women.attack()}')
    # print(f'{super_man.name}\'s defense was: {super_man.defend()}')

    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 80)
    # ability2 = Ability("Super Eyes", 20)
    # ability3 = Ability("Wizard Wand", 300)
    # ability4 = Ability("Wizard Beard", 130)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    hero = Hero("Wonder Woman")
    weapon = Weapon("Lasso of Truth", 90)
    hero.add_weapon(weapon)
    print(hero.attack())