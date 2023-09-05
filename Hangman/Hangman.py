import math
import random
import pygame


# Initializing Pygame:
pygame.init()
WIDTH, HEIGHT = 1200, 700
FPS = 60
A = 65

window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman")

# Fonts:
LETTER_FONT = pygame.font.SysFont("Arial", 40)
WORD_FONT = pygame.font.SysFont("Segoe UI", 55)
TITLE_FONT = pygame.font.SysFont("Segoe UI", 50)

# Button Variables:
RADIUS = 28
GAP = 25
letters = []
start_x = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
start_y = 400


for i in range(26):
    x = start_x + GAP * 2 + (RADIUS * 2 + GAP) * (i % 13)
    y = start_y + ((i // 13) * (GAP + RADIUS * 2)) + 100
    letters.append([x, y, chr(A + i), True])

# Game Variables:
hangman_status = 0

# Loading Up Images:
images_list = []
for i in range(7):
    images_list.append(pygame.image.load(r"assets/Hangman" + str(i) + ".png"))


# Creating the List of Words:
word_file = open(r"assets/words.txt", 'r')
word_list = []
for word in word_file:
    word_list.append(word)

word = random.choice(word_list)
word = word[0:len(word) - 1].upper()
guessed = []

clock = pygame.time.Clock()


# Drawing the Game:
def draw():
    window.fill("#AED6F1")
    text = TITLE_FONT.render("HANGMAN", 1, "#17202A")
    window.blit(text, (WIDTH/2 - text.get_width()/2, 20))
    # Word:
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + "  "
        else:
            display_word += "_  "

    text = WORD_FONT.render(display_word, 1, "#17202A")
    window.blit(text, (400, 200))

    # Buttons:
    for char in letters:
        x, y, ltr, visible = char
        if visible:
            pygame.draw.circle(window, "#17202A", (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, "#17202A")
            window.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

    window.blit(images_list[hangman_status], (80, 120))
    pygame.display.update()

def display_message(message):
    pygame.time.delay(1000)
    window.fill("#EBF5FB")
    text = WORD_FONT.render(message, 1, "#17202A")
    window.blit(text, (WIDTH / 2 - text.get_width() / 2, HEIGHT / 2 - text.get_height() / 2))
    pygame.display.update()
    pygame.time.delay(1500)


while True:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible = letter

                if visible:
                    dis = math.sqrt((x - mouse_x)**2 + (y - mouse_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)

                        if ltr not in word:
                            hangman_status += 1

    draw()

    # Win or Lose:
    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break

    if won:
        display_message("VICTORY")
        break

    if hangman_status == 6:
        display_message("SHAME")
        display_message(f"The Word was: {word.upper()}")
        break


pygame.quit()
