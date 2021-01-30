import pygame

pygame.init()

# 화면 크기 설정
screen_width = 640
screen_height = 860

screen = pygame.display.set_mode((screen_width, screen_height))

# game title
pygame.display.set_caption("BASIC GAME")


# 배경 이미지 조정
background = pygame.image.load(
    "/Users/jyr/Coding/4leaf-education/PYTHONN_GAME/basic_game/background.png"
)

character = pygame.image.load(
    "/Users/jyr/Coding/4leaf-education/PYTHONN_GAME/basic_game/character.png"
)

char_size = character.get_rect().size

char_width = char_size[0]
char_height = char_size[1]

char_position_x = (screen_width / 2) - (char_width / 2)
char_position_y = screen_height - char_height

# move
to_x = 0
to_y = 0

# 이벤트 루프
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                to_y -= 5
            elif event.key == pygame.K_RIGHT:
                to_x += 5
            elif event.key == pygame.K_DOWN:
                to_y += 5
            elif event.key == pygame.K_LEFT:
                to_x -= 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    char_position_x += to_x
    char_position_y += to_y

    if char_position_x <= 0:
        char_position_x = 0
    elif char_position_x >= screen_width-char_width:
        char_position_x = screen_width - char_width
    elif char_position_y <= 0:
        char_position_y = 0
    elif char_position_y >= screen_height - char_height:
        char_position_y = screen_height - char_height

    screen.blit(background, (char_position_x, char_position_y))
    screen.blit(character, (char_position_x, char_position_y))

    pygame.display.update()