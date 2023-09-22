import random, sys,os
sys.stdout = open(os.devnull, "w")
import pygame
# sys.stdout = sys.__stdout__
# del globals()["sys"]
pygame.init()
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
BULLET_SIZE = 50
PLAYER_SIZE = 100
BULLET_FALL_SPEED = 5
SCORE_FONT = pygame.font.Font(None, 20)
GAME_OVER_FONT = pygame.font.Font(None, 30)
BULLET_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bullet Catcher")
player_image = pygame.image.load("img.png")
player_image = pygame.transform.scale(player_image, (PLAYER_SIZE, PLAYER_SIZE))
# Initialize game variables
player_x = (SCREEN_WIDTH - PLAYER_SIZE) // 2
player_y = SCREEN_HEIGHT - PLAYER_SIZE
bullets = []
score = 0
bullets_caught = 0
max_bullets = 20
game_over = False
def create_bullet():
    x = random.randint(0, SCREEN_WIDTH - BULLET_SIZE)
    color = random.choice(BULLET_COLORS)
    return {'rect': pygame.Rect(x, 0, BULLET_SIZE, BULLET_SIZE), 'color': color}
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))
def game_loop():
    global player_x, player_y, bullets, score, bullets_caught, game_over
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if not game_over:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player_x > 0:
                player_x -= 5
            if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - PLAYER_SIZE:
                player_x += 5
            for bulet in bullets:
                bulet['rect'].move_ip(0, BULLET_FALL_SPEED)
            bullets = [bulet for bulet in bullets if bulet['rect'].top <= SCREEN_HEIGHT]
            while len(bullets) < 5 and len(bullets) < max_bullets:
                bullets.append(create_bullet())
            for bullet in bullets:
                if bullet['rect'].colliderect(pygame.Rect(player_x, player_y, PLAYER_SIZE, PLAYER_SIZE)):
                    bullets.remove(bullet)
                    score += 10
                    bullets_caught += 1
            if bullets_caught >= max_bullets:
                game_over = True
            if len(bullets) > 0 and bullets[0]['rect'].top > SCREEN_HEIGHT:
                game_over = True
            screen.fill(WHITE)
            screen.blit(player_image, (player_x, player_y))
            for bullet in bullets:
                pygame.draw.ellipse(screen, bullet['color'], bullet['rect'])
            draw_text(f"Bullets Caught: {bullets_caught}/{max_bullets}", SCORE_FONT, (0, 0, 0), 5, 5)
        else:
            if bullets_caught >= max_bullets:
                draw_text("You caught enough bullets! To Kill Anaconda", GAME_OVER_FONT, (0, 255, 0), SCREEN_WIDTH // 2 - 250,
                          SCREEN_HEIGHT // 2 - 50)
            else:
                draw_text("Game Over - You didn't catch enough bullets. Try again!", GAME_OVER_FONT, (255, 0, 0),
                          SCREEN_WIDTH // 2 - 350, SCREEN_HEIGHT // 2 - 50)
        pygame.display.update()
        clock.tick(30)
if __name__ == "__main__":
    game_loop()