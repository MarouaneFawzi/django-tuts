from models import Question, Choice
from random import *


class Seeder:

    def __init__(self):
        self.polls = ["Orange Ball", "Chew Toy 1",
                      "Cat Bowl", "Dog Bed", "Cat Food", "Dog Food"]

    def seed(self):
        for x in range(20):
            title = choice(self.polls) + " {0}".format(randint(1, 10000))
            question = Question(question_text=title)
            poll.save()
            for y in range(3):
                choice = Choice(question=question,
                                choice_text='choice' + y, votes=y)
                choice.save()
