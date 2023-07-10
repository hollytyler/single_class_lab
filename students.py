class Student:
    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        self.speak = "I love"

    def talk(self):
        self.talk = "I can talk!"

    def say_favourite_language(self,language):
        self.say_favourite_language = "I Love " + language