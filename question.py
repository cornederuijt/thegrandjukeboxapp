from random import random


class Question:

    def __init__(self, question, isopenquestion ,answers=[]):
        self.__question = question
        self.__answers = answers
        self.__isopenquestion = isopenquestion

    @property
    def question(self):
        return self.__question

    @property
    def answers(self):
        return self.__answers

    @property
    def isopenquestion(self):
        return self.__isopenquestion

    def drawanswers(self):
        if not self.__isopenquestion:
            return random.sample(self.__answers, 3)
        else:
            raise ValueError("The question is not an open question")
