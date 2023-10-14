# Topic 15
# Task 1

class Person:
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def talk(self):
        print(f"Hello, my name is {self.firstname} {self.lastname} and I’m {self.age} years old")

person = Person("Graham", "Momford", 56)
person.talk()

# Task 2

class Dog:
    # Class attribute
    age_factor = 7

    def __init__(self, dog_age):
        self.dog_age = dog_age

    def human_age(self):
        equivalent_human_age = self.dog_age * Dog.age_factor
        return equivalent_human_age

# Example usage:
dog1 = Dog(3)
print(f"The dog's age in human equivalent is: {dog1.human_age()} years")


# Task 3
CHANNELS = ["BBC", "Discovery", "TV1000"]
class TVController:
    def __init__(self, our_channel):
        self.our_channel = our_channel
        self.working_channel = 0

    def first_channel(self):
        self.working_channel = 1
        return self.our_channel[0]

    def last_channel(self):
        self.working_channel = len(self.our_channel)
        return self.our_channel[-1]

    def turn_channel(self, go_channel):
        self.some_channel = go_channel
        self.working_channel = go_channel
        return self.our_channel[go_channel - 1]

    def next_channel(self):
        if self.working_channel == len(self.our_channel) - 1:
            self.working_channel = 1
            return self.our_channel[0]
        self.working_channel = self.working_channel + 1
        return self.our_channel[self.working_channel - 1]

    def previous_channel(self):
        if self.working_channel == 1:
            return self.our_channel[-1]
        self.working_channel = self.working_channel - 1
        return self.our_channel[self.working_channel - 1]

    def current_channel(self):
        return self.our_channel[self.working_channel - 1]

    def is_exist(self, turning_on_channel):
        self.turning_on_channel = turning_on_channel

        if isinstance(turning_on_channel, int):
            return "Yes" if 1 <= turning_on_channel <= len(self.our_channel) else "No"

        if isinstance(turning_on_channel, str):
            return "Yes" if turning_on_channel in self.our_channel else "No"


controller = TVController(CHANNELS)

print(controller.first_channel()) # == "BBC"

print(controller.last_channel()) # == "TV1000"

print(controller.turn_channel(1)) # == "BBC"

print(controller.next_channel()) #  == "Discovery"

print(controller.previous_channel()) # == "BBC"

print(controller.current_channel()) # == "BBC"

print(controller.is_exist(4)) # == "No"

print(controller.is_exist("BBC")) # == "Yes"