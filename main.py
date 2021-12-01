# Python OOP practice for the Per Scholas Cloud DevOps program and uploaded from Git
# Written by Maximilian Conroy
# 12/1/2021


# Create MyDog class
class MyDog():
    def __init__(self, breed, name, age, color):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.isAsleep = False

    def walk(self):
        print("{} is walking!".format(self.name))

    def eat_food(self):
        print("{} is eating food!".format(self.name))

    def sleep(self):
        self.isAsleep = True
        print("{} is sleeping!".format(self.isAsleep))


# Main function to instantiate MyDog class
def main():
    pass


# Call main function
if __name__ == '__main__':
    main()
