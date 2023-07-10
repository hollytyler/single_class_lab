# Task_1

from students import Student

# student = Student("Holly", "E65")

# student.talk()
# print(student.talk)

# student.say_favourite_language(input("What is your favourite langauge? "))
# print(student.say_favourite_language)

# Task_2

from team import Team

players = ["Holly", "Ying", "Liam", "Brandon"]
team = Team("Coders", players, "Sky")

team.add_player("Jack")
print(players)

print(team.has_player("Liam"))


team.play_game(True)
print(team.points)