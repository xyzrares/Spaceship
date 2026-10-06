import pygame
from constants import WINDOW_HEIGHT, WINDOW_WIDTH

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
if __name__ == "__main__":
    main()
