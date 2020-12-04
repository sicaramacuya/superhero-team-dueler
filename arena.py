from ability import Ability
from weapon import Weapon
from armor import Armor
from hero import Hero
from team import Team

class Arena:

    def __init__(self):
        """ Instantiate properties: team_one to None and team_two to None"""

        self.team_one = Team('Team One')
        self.team_two = Team('Team Two')

    def create_ability(self):
        """Promp for Ability information. It will return Ability with values from user input"""

        name = input('What is the ability name? ')
        max_damage = input('What is the max damage of the ability? ')
        
        return Ability(name, max_damage)
    
    def create_weapon(self):
        """Promp user for Weapon information. It will return Weapon with values from user input."""

        name = input('What is the weapon name? ')
        max_damage = input('What is the max damage of the weapon? ')
        
        return Weapon(name, max_damage)

    def create_armor(self):
        """Prompt user for Armor information. It will return Armor with values from user input."""

        name = input('What is the armor name? ')
        max_block = input('What is the max blocking value of the ability? ')
        
        return Armor(name, max_block)

    def create_hero(self):
        """Prompt user for Hero information. It will return Hero with values from user input."""

        hero_name = input("Hero's name: ")
        hero = Hero(hero_name)
        add_item = None

        while add_item != "4":
            add_item = input("[1] Add ability\n[2] Add weapon\n[3] Add armor\n[4] Done adding items\n\nYour choice: ")
            
            if add_item == "1":
                ability = self.create_ability()
                hero.add_ability(ability)

            elif add_item == "2":
                weapon = self.create_weapon()
                hero.add_weapon(weapon)

            elif add_item == "3":
                armor = self.create_armor()
                hero.add_armor(armor)

        return hero

    def build_team_one(self):
        """Prompt the user to built team_one"""

        num_of_team_members = int(input("How many members would you like on Team One?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
    
    def build_team_two(self):
        """Prompt the user to built team_two"""

        num_of_team_members = int(input("How many members would you like on Team Two?\n"))
        for i in range(num_of_team_members):
            hero = self.create_hero()
            self.team_two.add_hero(hero)

    def team_battle(self):
        """Battle team_one and team_two together."""

        self.team_one.attack(self.team_two)

    def show_stats(self):
        """Prints team statistics to terminal"""

        # Surviving heroes ---------------------------------
        hero_team_one_alive = 0
        hero_team_two_alive = 0

        # cheking for surviving heroes on team 1
        for hero in self.team_one.heroes:
            if hero.is_alive():
                print(f'{hero.name} is alive.')
                hero_team_one_alive += 1

        # cheking for surviving heroes on team 2
        for hero in self.team_two.heroes:
            if hero.is_alive():
                print(f'{hero.name} is alive.')
                hero_team_two_alive += 1

        # Deciding which team won --------------------------
        if hero_team_one_alive > hero_team_two_alive:
            print(f'Team one won!')
        elif hero_team_one_alive < hero_team_two_alive:
            print(f'Team two won!')
        elif hero_team_one_alive == hero_team_two_alive:
            print(f'There was a draw!')

        # Calculating K/D for each team ---------------------
        team_one_kills = 0
        team_two_kills = 0
        team_one_deaths = 0
        team_two_deaths = 0 

        # calculating K/D for team one
        for hero in self.team_one.heroes: # para mi que el .heroes no va
            team_one_kills += hero.kills
            team_one_deaths += hero.deaths
        if team_one_deaths == 0:
            team_one_deaths = 1
        print(f'{self.team_one.name} average K/D was: {team_one_kills/team_one_deaths}')

        # calculating K/D for team two
        for hero in self.team_two.heroes: # para mi que el .heroes no va
            team_two_kills += hero.kills
            team_two_deaths += hero.deaths
        if team_two_deaths == 0:
            team_two_deaths = 1
        print(f'{self.team_two.name} average K/D was: {team_two_kills/team_two_deaths}')

if __name__ == "__main__":

    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    arena.build_team_one()
    arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()