# todo create a framework of what emotions will look like
import combat.moves
"""
stats:
    motivation (hp)
    effectiveness? (attack)
    resilience (defense)
    typing
"""
import pygame
from combat.emotions import Emotion
from start.button import Button


class PlayerEmotion(Emotion):
    def __init__(self, name, image_path):
        super().__init__(name, image_path)
        self.learnable_moves = []
        self.target = None
        self.attack = None
        self.enemy = False

        self.image = pygame.image.load(self.image_path)
        self.button = Button(None, 400, 500, self.image, 1, positioning="bottomleft")


    def teach_move(self, move: object):
        self.learned_moves.append(move)


    def forget_move(self, move: object):
        if move not in self.learned_moves:
            raise "Move not in learned moves!"
        self.learned_moves.remove(move)


    def draw(self, display):
        # this method either draws normal sprite or button
        self.button.draw(display)


# anger
# example of what an initialized emotion will look like
anger = PlayerEmotion("Anger", "Assets/SmallGoldSquare.png")
anger.initialize_emotion("Anger", 30, 50, 10, 7, "anger", 1,
                        [combat.moves.punch], [])

# # # happiness
happiness = PlayerEmotion("Happiness", "Assets/SmallGoldSquare.png")
happiness.initialize_emotion("Happiness", 30, 50, 10, 3, "joy", 1,
                              [combat.moves.punch], [])
# embarrassment


# calmness


# stress


# optimism



