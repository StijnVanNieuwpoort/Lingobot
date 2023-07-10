import sys
from evaluation import *
import pygame
import os
import datetime

pygame.init()
clock = pygame.time.Clock()
pygame.font.init()

# Screen
WIDTH, HEIGHT = 650, 900
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
LINGO_TILES_IMAGE = pygame.image.load(os.path.join('Assets', 'LingoTiles.png'))
BACKGROUND = LINGO_TILES_IMAGE.get_rect(center=(325, 300))

pygame.display.set_caption("Lingobot")

WHITE = (255, 255, 255)
RED = '#c95858'
YELLOW = "#c9b458"
GRAY = "#787c7e"
OUTLINE = "#d3d6da"
FILLED_OUTLINE = "#878a8c"

TEXT_FONT = pygame.font.Font(None, 16)
TEXT_COLOR = (233, 248, 215)

SECRET_WORD = random_word("English", "5")

ALPHABET = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]

CHAR_FONT = pygame.font.Font(None, 50)
AVAILABLE_CHAR_FONT = pygame.font.Font(None, 25)

FPS = 60

WINDOW.fill(WHITE)
WINDOW.blit(LINGO_TILES_IMAGE, BACKGROUND)

pygame.display.update()

CHAR_X_SPACING = 85
CHAR_Y_SPACING = 12
CHAR_SIZE = 75

guesses_count = 0
guesses = [[]] * 6

current_guess = []
current_guess_string = ""
current_letter_bg_x = 110


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = TEXT_COLOR
        self.text = text
        self.txt_surface = TEXT_FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                    # Limit characters           -20 for border width
                    if self.txt_surface.get_width() > self.rect.w - 20:
                        self.text = self.text[:-1]

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 10))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def update(self):
        # Re-render the text.
        self.txt_surface = TEXT_FONT.render(self.text, True, self.color)


indicators = []

game_result = ""


class Character:
    def __init__(self, text, bg_position):
        self.bg_color = "white"
        self.text_color = "black"
        self.bg_position = bg_position
        self.bg_x = bg_position[0]
        self.bg_y = bg_position[1]
        self.bg_rect = (bg_position[0], self.bg_y, CHAR_SIZE, CHAR_SIZE)
        self.text = text
        self.text_position = (self.bg_x + 36, self.bg_position[1] + 34)
        self.text_surface = CHAR_FONT.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.text_position)

    def draw(self):
        pygame.draw.rect(WINDOW, self.bg_color, self.bg_rect)
        if self.bg_color == "white":
            pygame.draw.rect(WINDOW, FILLED_OUTLINE, self.bg_rect, 3)
        self.text_surface = CHAR_FONT.render(self.text, True, self.text_color)
        WINDOW.blit(self.text_surface, self.text_rect)
        pygame.display.update()

    def delete(self):
        # Fills the letter's spot with the default square, emptying it.
        pygame.draw.rect(WINDOW, "white", self.bg_rect)
        pygame.draw.rect(WINDOW, OUTLINE, self.bg_rect, 3)
        pygame.display.update()


class Keyboard:
    def __init__(self, x, y, letter):
        self.x = x
        self.y = y
        self.text = letter
        self.rect = (self.x, self.y, 57, 75)
        self.bg_color = OUTLINE

    def draw(self):
        # Puts the indicator and its text on the screen at the desired position.
        pygame.draw.rect(WINDOW, self.bg_color, self.rect)
        self.text_surface = AVAILABLE_CHAR_FONT.render(self.text, True, "white")
        self.text_rect = self.text_surface.get_rect(center=(self.x + 27, self.y + 30))
        WINDOW.blit(self.text_surface, self.text_rect)
        pygame.display.update()


indicator_x, indicator_y = 20, 600

for i in range(3):
    for letter in ALPHABET[i]:
        new_indicator = Keyboard(indicator_x, indicator_y, letter)
        indicators.append(new_indicator)
        new_indicator.draw()
        indicator_x += 60
    indicator_y += 100
    if i == 0:
        indicator_x = 50
    elif i == 1:
        indicator_x = 105

current_guess = []
current_guess_string = ""
current_char_bg_x = 110

word_to_guess = random_word("English", "5")
words_played = []
possible_answers = get_vocabulary()["English"]["5"]
bad_letters = []
score = []


def check_guess(guess_to_check):
    global current_guess, current_guess_string, guesses_count, current_letter_bg_x, game_result
    game_decided = False
    for i in range(5):
        uppercase_character = guess_to_check[i].text.upper()
        if uppercase_character in SECRET_WORD:
            if uppercase_character == SECRET_WORD[i]:
                guess_to_check[i].bg_color = RED
                for indicator in indicators:
                    if indicator.text == uppercase_character.upper():
                        indicator.bg_color = RED
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                if not game_decided:
                    game_result = "W"
            else:
                guess_to_check[i].bg_color = YELLOW
                for indicator in indicators:
                    if indicator.text == uppercase_character.upper():
                        indicator.bg_color = YELLOW
                        indicator.draw()
                guess_to_check[i].text_color = "white"
                game_result = ""
                game_decided = True
        else:
            guess_to_check[i].bg_color = GRAY
            for indicator in indicators:
                if indicator.text == uppercase_character.upper():
                    indicator.bg_color = GRAY
                    indicator.draw()
            guess_to_check[i].text_color = "white"
            game_result = ""
            game_decided = True
        guess_to_check[i].draw()
        pygame.display.update()

    guesses_count += 1
    current_guess = []
    current_guess_string = ""
    current_letter_bg_x = 110

    if guesses_count == 6 and game_result == "":
        game_result = "L"


def new_game():
    pygame.draw.rect(WINDOW, "white", (10, 600, 1000, 600))
    play_again_font = pygame.font.Font(None, 40)
    play_again_text = play_again_font.render("Press any key to play again", True, "black")
    play_again_rect = play_again_text.get_rect(center=(WIDTH / 2, 700))
    word_was_text = play_again_font.render(f"The word was {SECRET_WORD}!", True, "black")
    word_was_rect = word_was_text.get_rect(center=(WIDTH / 2, 650))
    WINDOW.blit(word_was_text, word_was_rect)
    WINDOW.blit(play_again_text, play_again_rect)
    pygame.display.update()


def reset():
    global guesses_count, SECRET_WORD, guesses, current_guess, current_guess_string, game_result
    WINDOW.fill("white")
    WINDOW.blit(LINGO_TILES_IMAGE, BACKGROUND)
    guesses_count = 0
    SECRET_WORD = random_word("English", "5")
    guesses = [[]] * 6
    current_guess = []
    current_guess_string = ""
    game_result = ""
    pygame.display.update()
    for indicator in indicators:
        indicator.bg_color = OUTLINE
        indicator.draw()


def create_new_letter(key_pressed):
    global current_guess_string, current_letter_bg_x
    current_guess_string += key_pressed
    new_letter = Character(key_pressed, (current_letter_bg_x, guesses_count * 100 + CHAR_Y_SPACING))
    current_letter_bg_x += CHAR_X_SPACING
    guesses[guesses_count].append(new_letter)
    current_guess.append(new_letter)
    for guess in guesses:
        for letter in guess:
            letter.draw()


def delete_letter():
    global current_guess_string, current_letter_bg_x
    guesses[guesses_count][-1].delete()
    guesses[guesses_count].pop()
    current_guess_string = current_guess_string[:-1]
    current_guess.pop()
    current_letter_bg_x -= CHAR_X_SPACING


def player_game():
    while True:
        if game_result != "":
            new_game()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if game_result != "":
                        reset()
                    else:
                        if len(current_guess_string) == 5:
                            check_guess(current_guess)
                elif event.key == pygame.K_BACKSPACE:
                    if len(current_guess_string) > 0:
                        delete_letter()
                else:
                    key_pressed = event.unicode.upper()
                    if key_pressed in "QWERTYUIOPASDFGHJKLZXCVBNM" and key_pressed != "":
                        if len(current_guess_string) < 5:
                            create_new_letter(key_pressed)

player_game()