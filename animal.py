class Animal:
    
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f'{self.name} is eating')

    def drink(self):
        print(f'{self.name} is drinking')

class Frog(Animal):

    def jump(self):
        print(f'{self.name} is jumping')





if __name__ == '__main__':
    # If you run this file from the terminal this block is executed.

    dog = Animal('Amigo')
    frog = Frog('King Harold')

    frog.eat()
    frog.drink()
    frog.jump()

    dog.eat()
    dog.drink()