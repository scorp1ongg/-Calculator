import pygame

WIDTH = 700
HEIGHT = 600
FPS = 60

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

bg = pygame.image.load("seamless-pattern-with-school-supplies-calculator_275421-137.jpg")
bg = pygame.transform.scale(bg, (700, 600))

b = 0
example = ""
example1 = ""

# symbols of numbers
text1_font = pygame.font.SysFont('Times New Roman', 50)
text1_text = text1_font.render("1", 1, BLACK)
text2_font = pygame.font.SysFont('Times New Roman', 50)
text2_text = text2_font.render("2", 1, BLACK)
text3_font = pygame.font.SysFont('Times New Roman', 50)
text3_text = text3_font.render("3", 1, BLACK)
text4_font = pygame.font.SysFont("Times New Roman", 50)
text4_text = text4_font.render("4", 1, BLACK)
text5_font = pygame.font.SysFont("Times New Roman", 50)
text5_text = text5_font.render("5", 1, BLACK)
text6_font = pygame.font.SysFont("Times New Roman", 50)
text6_text = text6_font.render("6", 1, BLACK)
text7_font = pygame.font.SysFont("Times New Roman", 50)
text7_text = text7_font.render("7", 1, BLACK)
text8_font = pygame.font.SysFont("Times New Roman", 50)
text8_text = text8_font.render("8", 1, BLACK)
text9_font = pygame.font.SysFont("Times New Roman", 50)
text9_text = text9_font.render("9", 1, BLACK)
text0_font = pygame.font.SysFont("Times New Roman", 50)
text0_text = text0_font.render("0", 1, BLACK,)



# symbols of actions
plus_font = pygame.font.SysFont("Times New Roman", 50)
plus_text = plus_font.render("+", 1, BLACK)
minus_font = pygame.font.SysFont("Times New Roman", 50)
minus_text = minus_font.render("-", 1, BLACK)
divide_font = pygame.font.SysFont("Times New Roman", 50)
divide_text = divide_font.render(":", 1, BLACK)
multiply_font = pygame.font.SysFont("Times New Roman", 50)
multiply_text = multiply_font.render("*", 1, BLACK)
is_font = pygame.font.SysFont("Time New Roman", 50)
is_text = is_font.render('=', 1, BLACK)
del_font = pygame.font.SysFont("Time New Roman", 50)
del_text = del_font.render('C', 1, BLACK)
dot_font = pygame.font.SysFont('Time New Roman', 70)
dot_text = del_font.render('.', 1, BLACK)
sqr_font = pygame.font.SysFont('Time New Roman', 50)
sqr_text = sqr_font.render('^', 1, BLACK)

open_font = pygame.font.SysFont('Time New Roman', 50)
open_text = open_font.render('(', 1, BLACK)
close_font = pygame.font.SysFont('Time New Roman', 50)
close_text = close_font.render(')', 1, BLACK)

Running = True
while Running:
    screen.blit(bg, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running = False
        # взаимодействие с кнопками
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[0] > 50 and event.pos[0] < 70 + 50 \
                    and event.pos[1] > 170 and event.pos[1] < 170 + 70:
                b = 0
                example += (str(1))
                example1 += (str(1))
            if event.pos[0] > 50 and event.pos[0] < 70 + 50 \
                    and event.pos[1] > 270 and event.pos[1] < 270 + 70:
                b = 0
                example += (str(4))
                example1 += (str(4))
            if event.pos[0] > 50 and event.pos[0] < 70 + 50 \
                    and event.pos[1] > 370 and event.pos[1] < 370 + 70:
                b = 0
                example += (str(7))
                example1 += (str(7))
            if event.pos[0] > 150 and event.pos[0] < 70 + 150 \
                    and event.pos[1] > 170 and event.pos[1] < 170 + 70:
                b = 0
                example += (str(2))
                example1 += (str(2))
            if event.pos[0] > 150 and event.pos[0] < 70 + 150 \
                    and event.pos[1] > 270 and event.pos[1] < 270 + 70:
                b = 0
                example += (str(5))
                example1 += (str(5))
            if event.pos[0] > 150 and event.pos[0] < 70 + 150 \
                    and event.pos[1] > 370 and event.pos[1] < 370 + 70:
                b = 0
                example += (str(8))
                example1 += (str(9))
            if event.pos[0] > 150 and event.pos[0] < 70 + 150 \
                    and event.pos[1] > 470 and event.pos[1] < 470 + 70:
                b = 0
                example += (str(0))
                example1 += (str(0))
            if event.pos[0] > 250 and event.pos[0] < 70 + 250 \
                    and event.pos[1] > 170 and event.pos[1] < 170 + 70:
                b = 0
                example += (str(3))
                example1 += (str(3))
            if event.pos[0] > 250 and event.pos[0] < 70 + 250 \
                    and event.pos[1] > 270 and event.pos[1] < 270 + 70:
                b = 0
                example += (str(6))
                example1 += (str(6))
            if event.pos[0] > 250 and event.pos[0] < 70 + 250 \
                    and event.pos[1] > 370 and event.pos[1] < 370 + 70:
                b = 0
                example += (str(9))
                example1 += (str(9))
            if event.pos[0] > 380 and event.pos[0] < 70 + 380 \
                    and event.pos[1] > 170 and event.pos[1] < 170 + 70:
                b = 0
                example += "+"
                example1 += "+"
            if event.pos[0] > 380 and event.pos[0] < 70 + 380 \
                    and event.pos[1] > 270 and event.pos[1] < 270 + 70:
                b = 0
                example += "-"
                example1 += "-"
            if event.pos[0] > 480 and event.pos[0] < 70 + 480 \
                    and event.pos[1] > 270 and event.pos[1] < 270 + 70:
                b = 0
                example += '.'
                example1 += '.'
            if event.pos[0] > 480 and event.pos[0] < 70 + 480 \
                    and event.pos[1] > 370 and event.pos[1] < 370 + 70:
                b = 0
                example += '^'
                example1 += '**'
            if event.pos[0] > 380 and event.pos[0] < 70 + 380 \
                    and event.pos[1] > 370 and event.pos[1] < 370 + 70:
                b = 0
                example += "*"
                example1 += "*"
            if event.pos[0] > 380 and event.pos[0] < 70 + 380 \
                    and event.pos[1] > 470 and event.pos[1] < 470 + 70:
                b = 0
                example += ":"
                example1 += "/"
            if event.pos[0] > 250 and event.pos[0] < 70 + 250 \
                    and event.pos[1] > 470 and event.pos[1] < 470 + 70:
                b = 1
                example = ''
            if event.pos[0] > 480 and event.pos[0] < 70 + 480 \
                    and event.pos[1] > 170 and event.pos[1] < 170 + 70:
                b = 0
                example = ''
                example1 = ''
            if event.pos[0] > 580 and event.pos[0] < 70 + 580 \
                    and event.pos[1] > 170 and event.pos[1] < 170 + 70:
                b = 0
                example += '('
                example1 += "("
            if event.pos[0] > 580 and event.pos[0] < 70 + 580 \
                    and event.pos[1] > 270 and event.pos[1] < 270 + 70:
                b = 0
                example += ')'
                example1 += ")"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                b = 0
                example += '0'
                example1 += '0'
            if event.key == pygame.K_1:
                b = 0
                example += '1'
                example1 += '1'
            if event.key == pygame.K_2:
                b = 0
                example += '2'
                example1 += '2'
            if event.key == pygame.K_3:
                b = 0
                example += '3'
                example1 += '3'
            if event.key == pygame.K_4:
                b = 0
                example += '4'
                example1 += '4'
            if event.key == pygame.K_5:
                b = 0
                example += '5'
                example1 += '5'
            if event.key == pygame.K_6:
                b = 0
                example += '6'
                example1 += '6'
            if event.key == pygame.K_7:
                b = 0
                example += '7'
                example1 += '7'
            if event.key == pygame.K_8:
                b = 0
                example += '8'
                example1 += '8'
            if event.key == pygame.K_9:
                b = 0
                example += '9'
                example1 += '9'
            if event.key == pygame.K_MINUS:
                b = 0
                example += '-'
                example1 += '-'
            if event.key == pygame.K_PERIOD:
                b = 0
                example += '.'
                example1 += '.'
            if event.key == pygame.K_EQUALS:
                b = 1
                example = ''


    # кнопки
    pygame.draw.rect(screen, (255, 255, 0), (50, 170, 70, 70))  # 1
    pygame.draw.rect(screen, (255, 255, 0), (50, 270, 70, 70))  # 4
    pygame.draw.rect(screen, (255, 255, 0), (50, 370, 70, 70))  # 7
    pygame.draw.rect(screen, (255, 255, 0), (150, 170, 70, 70))  # 2
    pygame.draw.rect(screen, (255, 255, 0), (150, 270, 70, 70))  # 5
    pygame.draw.rect(screen, (255, 255, 0), (150, 370, 70, 70))  # 8
    pygame.draw.rect(screen, (255, 255, 0), (150, 470, 70, 70))  # 0
    pygame.draw.rect(screen, (255, 255, 0), (250, 170, 70, 70))  # 3
    pygame.draw.rect(screen, (255, 255, 0), (250, 270, 70, 70))  # 6
    pygame.draw.rect(screen, (255, 255, 0), (250, 370, 70, 70))  # 9
    pygame.draw.rect(screen, (255, 255, 0), (250, 470, 70, 70))  # =
    pygame.draw.rect(screen, (255, 255, 0), (380, 170, 70, 70))  # +
    pygame.draw.rect(screen, (255, 255, 0), (380, 270, 70, 70))  # -
    pygame.draw.rect(screen, (255, 255, 0), (380, 370, 70, 70))  # *
    pygame.draw.rect(screen, (255, 255, 0), (380, 470, 70, 70))  # /
    pygame.draw.rect(screen, (255, 255, 0), (480, 170, 70, 70))  # del
    pygame.draw.rect(screen, (255, 255, 0), (480, 270, 70, 70))  # dot
    pygame.draw.rect(screen, (255, 255, 0), (480, 370, 70, 70))  # sqr
    pygame.draw.rect(screen, (255, 255, 0), (580, 170, 70, 70))  # (
    pygame.draw.rect(screen, (255, 255, 0), (580, 270, 70, 70))  # )
    # цифры
    screen.blit(text1_text, (70, 175))
    screen.blit(text4_text, (70, 275))
    screen.blit(text7_text, (70, 375))
    screen.blit(text2_text, (170, 175))
    screen.blit(text5_text, (170, 275))
    screen.blit(text8_text, (170, 375))
    screen.blit(text0_text, (170, 475))
    screen.blit(text3_text, (270, 175))
    screen.blit(text6_text, (270, 275))
    screen.blit(text9_text, (270, 375))
    # действия
    screen.blit(plus_text, (400, 175))
    screen.blit(minus_text, (405, 275))
    screen.blit(multiply_text, (403, 382))
    screen.blit(divide_text, (409, 473))
    screen.blit(is_text, (274, 482))
    screen.blit(del_text, (502, 190))
    screen.blit(dot_text, (510, 280))
    screen.blit(sqr_text, (503, 386))
    screen.blit(open_text, (606, 189))
    screen.blit(close_text, (606, 289))

    example_font = pygame.font.SysFont("Times New Roman", 48)
    example_text = example_font.render(example, 1, BLACK)

    screen.blit(example_text, (30, 30))

    if b == 1:
        a = str(eval(example1))
        text20_font = pygame.font.SysFont("Times New Roman", 48)
        text20_text = text20_font.render(a, 1, BLACK)
        screen.blit(text20_text, (30, 30))

    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
