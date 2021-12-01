# Python OOP practice for the Per Scholas Cloud DevOps program and uploaded from Git
# Written by Maximilian Conroy
# 12/1/2021

# Assignment 1 details:
# ❑ Create a class named MyDog and define the following properties.
# ➢ instance attributes: breed, name, age, color, isAsleep=False
# ➢ __init__ method that takes breed, name, age, color as parameters, sets the values
# for them and also sets isAsleep to False
# ➢ instance methods:
# ▶ walk() which prints "name is walking!"
# ▶ eat(food) which prints "name is eating food!"
# ▶ sleep() which changes the value of the instance attribute, isAsleep to True and
# prints "name is sleeping!"
# ▶ wake_up() which changes the value of the instance attribute, isAsleep to False
# and prints "name is waking up!"
# ▶ info() which prints out the values for all instance attributes except isAsleep.
# ❑ Create two instances of MyDog class.
# ➢ On the first instance, invoke method walk and then sleep.
# ➢ On the second instance, invoke method eat and then sleep.
# ➢ On the first instance, invoke method wake_up and then eat.
# ➢ Print out the description of the instances using info method.
#
# Assignment 2 details (working on the same code):
# ❑ Use the MyDog class created from previous problem.
# ➢ class attribute: home_address
# ➢ class method:
# ▶ from_birthyear() which returns cls that allows accepting birthyear instead of age
# as parameter. (*hint – use datetime module)
# ▶ move(destination) which changes value of the class attribute, home_address to
# destination and prints "We moved to destination!!"
# ➢ static method:
# ▶ checkup_needed(age) which returns True if the age is x, such that
# (x - 1) % 3 = 0, False otherwise.
#
# ❑ Create two instances of MyDog class using from_birthyear method.
# ➢ Print out the description of the instances using info method to make sure the ages
# are calculated correctly.
# ➢ On the first instance, print its home_address.
# ➢ Change the value for home_address using move method.
# ➢ On the second instance, print its home_address and check if the value has been
# properly changed.
# ➢ Check if two instances need checkup using checkup_needed method.


# Create MyDog class
class MyDog:
    def __init__(self, breed, name, age, color):
        self.breed = breed
        self.name = name
        self.age = age
        self.color = color
        self.isAsleep = False

    def walk(self):
        print("{} is walking!".format(self.name))

    def eat(self, food):
        print("{} is eating {}!".format(self.name, food))

    def sleep(self):
        self.isAsleep = True
        print("{} is sleeping!".format(self.name))

    def wake_up(self):
        self.isAsleep = False
        print("{} is waking up!".format(self.name))

    def info(self):
        print("Breed: {}, Name: {}, Age: {}, Color: {}".format(self.breed, self.name, self.age, self.color))


# Main function to instantiate MyDog class and use the MyDog objects
def main():
    mila = MyDog("German Shepherd", "Mila", "8", "Black")
    freyja = MyDog("Australian Shepherd", "Freyja", "1", "Red")

    mila.walk()
    mila.sleep()

    freyja.eat("Arcana")
    freyja.sleep()

    mila.wake_up()
    mila.eat("Blue Buffalo")

    mila.info()
    freyja.info()


# Call main function
if __name__ == '__main__':
    main()
