# todo create a framework of what emotions will look like

"""
stats:
    motivation (hp)
    effectiveness? (attack)
    resilience (defense)
    typing
"""
import pygame


class Emotion:
    def __init__(self, name, image_path):
        self.name = name
        self.image_path = image_path
        self.motivation = 100
        self.effectiveness = 0
        self.resilience = 1
        self.typing = ""
        self.level = 1
        self.experience_factor = 0
        self.learned_moves = []


    def initialize_emotion(self, name, motivation, effectiveness, resilience, typing, experience_factor, learned_moves,
                           learnable_moves):
        """
        this will be used for each emotions basic starting stats at the start of the game launch
        :param name: the name of the character
        :param motivation: the HP stat of the character
        :param effectiveness: the ATT stat of the character
        :param resilience:  the DEF stat of the character
        :param typing: The Element of the character
        :param experience_factor: rate at which experience is needed to lvl up
        :param learned_moves: any moves you want the character to start with
        :param learnable_moves: a list of the moves that emotion will have
        :return: None
        """
        self.name = name
        self.motivation = motivation
        self.effectiveness = effectiveness
        self.resilience = resilience
        self.typing = typing
        self.experience_factor = experience_factor
        self.learned_moves = learned_moves
        self.learnable_moves = learnable_moves


    def draw(self, display):
        # draw the emotion here
        pass