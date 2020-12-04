from random import choice

class Team:
    
    def __init__(self, name):
        """Initialize your team with its team name and empy list of heroes."""

        self.name = name
        self.heroes = list()

    def add_hero(self, hero):
        """"Add hero object to self.heroes"""

        self.heroes.append(hero)

    def remove_hero(self, name):
        """Remove hero from heroes list. If hero isn't found return 0."""

        found_hero= False

        # loop through each hero in our list
        for hero in self.heroes:
            # if we find them, remove them from the list
            if hero.name == name:
                self.heroes.remove(hero)
                # set our indicator to True
                found_hero = True
        
        # if we looped through our list and did not find our hero, the indicator would never get change, so return 0
        if not found_hero:
            return 0

    def view_all_heroes(self):
        """Prints out all heroes to the console"""
        
        for hero in self.heroes:
            print(hero.name)

    def stats(self):
        """Print team statistics"""

        for hero in self.heroes:
            kd = hero.kills / hero.deaths
            print(f'{hero.name} Kill/Deaths:{kd}')

    def revive_heroes(self, health=100):
        """Reset all heroes health to starting_health"""

        for hero in self.heroes:
            hero.current_health = hero.starting_health

    def attack(self, other_team):
        """Battle each team against each other"""

        # this lists will hold hero in a list because what is pass to this method is the actual team object not each individual hero alone
        living_heroes = list()
        living_opponents = list()

        for hero in self.heroes:
            living_heroes.append(hero)

        for hero in other_team.heroes:
            living_opponents.append(hero)

        while len(living_heroes) > 0 and len(living_opponents) > 0: 
            # randomly selecting a hero and a opponent
            fighting_hero = choice(living_heroes)
            fighting_opponent = choice(living_opponents)

            fighting_hero.fight(fighting_opponent)

            # this if statement will run only if the fighting hero is death. The method will return false if is death but with the not opperator that boolean value will change to true.
            if not fighting_hero.is_alive():
                living_heroes.remove(fighting_hero)

            # this if statement will run only if the fighting opponent is death. The method will return false if is death but with the not opperator that boolean value will change to true.
            if not fighting_opponent.is_alive():
                living_opponents.remove(fighting_opponent)