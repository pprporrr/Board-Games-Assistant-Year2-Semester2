import os, time, pygame
from states.state import State, Button
from states.game_info import Game_info

class Home(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Home_button = Button("HOME", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (85, 33), (829, 79))
        self.Categgory_button = Button("CATEGORY", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (154, 33), (933, 79))
        self.Mylist_button = Button("MY LIST", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (123, 33), (1097, 79))
        self.Avalon_game = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (994, 312), (314, 195))
        self.test = Button("TEST", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (219, 160, 90), (281.72, 312), (1026.28, 559))
        
    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Home_button.check_click()
        self.Categgory_button.check_click()
        self.Mylist_button.check_click()
        self.Avalon_game.check_click()
        if self.Home_button.pressed == True:
            pass
            
        elif self.Categgory_button.pressed == True:
            pass
            
        elif self.Mylist_button.pressed == True:
            pass
            
        elif self.Avalon_game.pressed == True:
            self.Avalon_game.pressed = False
            new_state = Game_info(self.game)
            # new_state = self.game.state_page[1]
            new_state.enter_state()
        
    def render(self, display):
        display.fill((0, 0, 0))
        self.Home_button.draw(display)
        self.Categgory_button.draw(display)
        self.Mylist_button.draw(display)
        self.Avalon_game.draw_image(display, 'Avalon_button.png')
        self.game.draw_text(display, "Available", 28, (137, 137, 137), (291, 145))
        self.game.draw_text(display, "AVALON", 96, (255, 255, 255), (343, 376))
        self.game.draw_text(display, "Comingsoon...", 28, (137, 137, 137), (291, 517))
        self.game.create_rect_border(display, (281.72, 312), 2, (0, 0, 0), (255, 255, 255), (314.48, 559))
        self.game.create_rect_border(display, (281.72, 312), 2, (0, 0, 0), (255, 255, 255), (670, 559))
        self.game.create_rect_border(display, (281.72, 312), 2, (0, 0, 0), (255, 255, 255), (1026.28, 559))
        