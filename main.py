import pygame
import sys

from utilities.generic_scene import GenericScene
from start.start_scene import StartScene
from planning.planning_scene import PlanningScene
from combat.combat_scene import CombatScene
from do_it_irl.do_it_irl_scene import DoItIRLScene
from utilities.game_state_object import GameStateObject

# final vars
WIDTH, HEIGHT = 1280, 620
FPS = 60


def start_game():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    clock = pygame.time.Clock()
    game_state = GameStateObject(None)

    scenes: dict[str, GenericScene] = {
        "start": StartScene(screen, game_state),
        "planning": PlanningScene(screen, game_state),
        "combat": CombatScene(screen, game_state),
        "do_it_irl": DoItIRLScene(screen, game_state),
    }
    game_state.current_state = "start"
    

    # this is the main game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # this allows to switch between states
        scenes[game_state.current_state].game_body_loop()

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    start_game()
