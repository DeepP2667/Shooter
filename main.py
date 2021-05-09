import pygame
import random
import os
pygame.font.init()

WIDTH, HEIGHT = 1200, 650
TARGET_WIDTH, TARGET_HEIGHT = 120, 120
RESTART_WIDTH, RESTART_HEIGHT = 128, 128
QUIT_WIDTH, QUIT_HEIGHT = 141, 128

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

TARGET_IMAGE = pygame.image.load(os.path.join('Assests', 'target.png'))
TARGET = pygame.transform.scale(TARGET_IMAGE, (TARGET_WIDTH, TARGET_HEIGHT))
RESTART_IMAGE = pygame.image.load(os.path.join('Assests', 'restart.png'))

RESTART = pygame.transform.scale(RESTART_IMAGE, (RESTART_WIDTH, RESTART_HEIGHT))
QUIT_IMAGE = pygame.image.load(os.path.join('Assests', 'quit.png'))
_QUIT = pygame.transform.scale(QUIT_IMAGE, (QUIT_WIDTH, QUIT_HEIGHT))

FPS = 60

SCORE_FONT = pygame.font.SysFont('comicsans', 24)
TIME_FONT = pygame.font.SysFont('arial', 30)
FINAL_SCORE = pygame.font.SysFont('arial', 50)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Target Practice")

def check(target, SCORE, seconds):
    
    x, y = pygame.mouse.get_pos()

    if (target.x < x < (target.x + TARGET_WIDTH)) and (target.y < y < (target.y + TARGET_HEIGHT)):
        SCORE += 1 
        target = pygame.Rect(random.randint(0, WIDTH - TARGET_WIDTH), 
                         random.randint(0, HEIGHT - TARGET_HEIGHT), 
                         TARGET_WIDTH, TARGET_HEIGHT)
        pygame.display.update()
    return (target, SCORE)       


def draw_window(SCORE, seconds, target):        
    
    WIN.fill(WHITE)
    score_text = SCORE_FONT.render(f'SCORE: {SCORE}', True, BLACK)
    WIN.blit(score_text, (WIDTH // 2 - score_text.get_width(), 20))

    time_text = TIME_FONT.render(f"{60 - seconds}", True, BLACK)
    WIN.blit(time_text, (10, 10))

    WIN.blit(TARGET, (target.x, target.y))

    pygame.display.update()


def draw_final_screen(SCORE):

    option = None
    WIN.fill(WHITE)
    final_score_text = FINAL_SCORE.render(f'FINAL SCORE: {SCORE}', True, BLACK)
    WIN.blit(final_score_text, (WIDTH // 2 - final_score_text.get_width()/2, 
                                HEIGHT // 4 - final_score_text.get_height()/2))

    restart = pygame.Rect(WIDTH // 3 - RESTART_WIDTH / 2, (2 * HEIGHT) // 3 - RESTART_HEIGHT / 2,
                          RESTART_WIDTH, RESTART_HEIGHT)
    _quit = pygame.Rect((2 * WIDTH) // 3 - QUIT_WIDTH / 2, (2 * HEIGHT) // 3 - QUIT_HEIGHT / 2,
                         QUIT_WIDTH, QUIT_HEIGHT)

    WIN.blit(RESTART, (restart.x, restart.y))
    WIN.blit(_QUIT, (_quit.x, _quit.y))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            option = check_buttons(restart, _quit)
            return option

def check_buttons(restart, _quit):

    x, y = pygame.mouse.get_pos()

    if (restart.x < x < restart.x + RESTART_WIDTH) and (restart.y < y < restart.y + RESTART_HEIGHT):
        return 'restart'
    
    if (_quit.x < x < _quit.x + QUIT_WIDTH) and (_quit.y < y < _quit.y + QUIT_HEIGHT):
        return 'quit'

def main():
    
    SCORE = 0
    WIN.fill(WHITE)
    target = pygame.Rect(random.randint(0, WIDTH - TARGET_WIDTH), 
                         random.randint(0, HEIGHT - TARGET_HEIGHT), 
                         TARGET_WIDTH, TARGET_HEIGHT)

    WIN.blit(TARGET, (target.x, target.y))
    pygame.display.update()

    clock = pygame.time.Clock()
    start_ticks = pygame.time.get_ticks()

    run = True

    while run:
        clock.tick(FPS)  

        seconds = (pygame.time.get_ticks() - start_ticks) / 1000

        if (60 - seconds) < -1:
            restart_quit = draw_final_screen(SCORE)  
            if restart_quit == 'restart':
                break
            if restart_quit == 'quit':
                pygame.quit()   
        else:
            draw_window(SCORE, int(seconds), target)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()   

            if event.type == pygame.MOUSEBUTTONDOWN:
                (target, SCORE) = check(target, SCORE, int(seconds))

    main()


if __name__ == "__main__":
    print("Welcome to target practice")
    main()