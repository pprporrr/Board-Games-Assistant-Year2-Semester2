import os, time, pygame
from states.state import State, Button
# from states.game_rule_1 import Game_rule

class Game_rule_3(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Home_button = Button("HOME", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (85, 33), (829, 79))
        self.Categgory_button = Button("CATEGORY", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (154, 33), (933, 79))
        self.Mylist_button = Button("MY LIST", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (123, 33), (1097, 79))
        self.Back = Button("BACK", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (85, 33), (153, 79))
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (986, 670), (307, 180))
        
        self.Play = Button("", "Lexend-VariableFont_wght.ttf", 28, (255, 255, 255), (219, 160, 90, 76.5), (197, 55), (1039, 769))
        self.Play_icon = Button("", "Lexend-VariableFont_wght.ttf", 1, (0, 0, 0, 0), (0, 0, 0, 0), (46, 37), (1075, 778))
        self.Previous_page = Button("<< Previous page", "Lexend-VariableFont_wght.ttf", 28, (255, 255, 255), (219, 160, 90, 0), (231, 25), (329, 785))

    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Home_button.check_click()
        self.Categgory_button.check_click()
        self.Mylist_button.check_click()
        self.Back.check_click()
        self.Previous_page.check_click()
        
        if self.Home_button.pressed == True:
            print('Home_button click')
            self.exit_state()
            self.Home_button.pressed = False
            
        elif self.Categgory_button.pressed == True:
            print('Categgory_button click')
            
        elif self.Mylist_button.pressed == True:
            print('Mylist_button click')
            
        elif self.Previous_page.pressed == True:
            print('Previous_page click')
            self.exit_state()
            self.Previous_page.pressed = False
            
        elif self.Back.pressed == True:
            self.exit_state()
            self.Back.pressed = False
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        
        self.Home_button.draw(display)
        self.Categgory_button.draw(display)
        self.Mylist_button.draw(display)
        self.Back.draw(display)
        self.Bg.draw_image(display, 'BG.png')
        
        
        self.game.draw_text(display, 'Avalon Rule', 64, (255, 255, 255), (631, 212))        
        
        self.game.draw_text(display, "Complete the quest", 28, (255, 255, 255), (445, 300))
        self.game.draw_text(display, "1. Randomly choose who is the leader this round.", 16, (255, 255, 255), (475, 350))
        self.game.draw_text(display, "2. Leader chooses people to go on a quest with him.", 16, (255, 255, 255), (475, 380))
        self.game.draw_text(display, "3. Every players have approving card for selected players to vote, if votes are more than half ", 16, (255, 255, 255), (475, 410))
        self.game.draw_text(display, "they will go on to the quest, if not the leader passed to the next person. If the team is not ", 16, (255, 255, 255), (490, 440))
        self.game.draw_text(display, "approved within 5 rounds, the Evil team wins.", 16, (255, 255, 255), (490, 470))
        self.game.draw_text(display, "4. Players who go to do quests will get 1 success and 1 fail card. Evil teams can use both while", 16, (255, 255, 255), (475, 500))
        self.game.draw_text(display, "Good teams can only use success cards.", 16, (255, 255, 255), (490, 530))
        self.game.draw_text(display, "5. Each player secretly select a card faced down then they will be shuffled.", 16, (255, 255, 255), (475, 560))
        self.game.draw_text(display, "6. If all the selected cards are success, Good team gets a score, else the Evil team gets a score", 16, (255, 255, 255), (475, 590))

        self.Play.draw_with_border(display, 2, (255, 255, 255))
        self.Play_icon.draw_image(display, 'Play arrow.png')
        self.game.draw_text(display, 'PLAY', 28, (255, 255, 255), (1115, 780))
        
        self.Previous_page.draw_with_border(display, 1, (255, 255, 255))