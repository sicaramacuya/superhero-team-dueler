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

 