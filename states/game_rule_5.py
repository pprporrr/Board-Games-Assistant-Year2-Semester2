import os, time, pygame
from states.state import State, Button

class Game_rule_5(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Back = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (119, 35), (119, 77))
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1169, 670), (311, 180))
        self.Bg_line = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1360, 1), (120, 129))
        
        self.Tab = Button("", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (180, 670), (120, 180))
        self.General_box = Button("", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (174, 69), (123, 183))
        self.General_text = Button("General", "Alatsi-Regular.ttf", 20, (255, 255, 255, 70), (0, 0, 0), (68, 26), (176, 204))
        
        self.Components_box = Button("", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (174, 69), (123, 252))
        self.Components_text = Button("Components", "Alatsi-Regular.ttf", 20, (255, 255, 255,70), (0, 0, 0), (110, 26), (155, 275))
        
        self.Setup_box = Button("", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (174, 69), (123, 321))
        self.Setup_text = Button("Setup", "Alatsi-Regular.ttf", 20, (255, 255, 255, 70), (0, 0, 0), (51, 26), (185, 342))
        
        self.GamePlay_box = Button("", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (174, 69), (123, 390))
        self.GamePlay_text = Button("Game play", "Alatsi-Regular.ttf", 20, (255, 255, 255, 70), (0, 0, 0), (90, 26), (165, 412))
        
        self.HowToWin_box = Button("", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (174, 69), (123, 459))
        self.HowToWin_text = Button("How to win", "Alatsi-Regular.ttf", 20, (255, 255, 255), (0, 0, 0), (96, 26), (162, 480))
        
        
    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Back.check_click()
        self.General_box.check_click()
        self.General_text.check_click()
        self.Components_box.check_click()
        self.Components_text.check_click()
        self.Setup_box.check_click()
        self.Setup_text.check_click()
        self.GamePlay_box.check_click()
        self.GamePlay_text.check_click()
                    
        if self.General_box.pressed == True or self.General_text.pressed == True:
            self.General_box.pressed = False
            self.General_text.pressed = False
            new_state = self.game.state_game_info[0]
            new_state.enter_state()
            
        elif self.Components_box.pressed == True or self.Components_text.pressed == True:
            self.Components_box.pressed = False
            self.Components_text.pressed = False
            new_state = self.game.state_game_info[1]
            new_state.enter_state()
            
        elif self.Setup_box.pressed == True or self.Setup_text.pressed == True:
            self.Setup_box.pressed = False
            self.Setup_text.pressed = False
            new_state = self.game.state_game_info[2]
            new_state.enter_state()
            
        elif self.GamePlay_box.pressed == True or self.GamePlay_text.pressed == True:
            self.GamePlay_box.pressed = False
            self.GamePlay_text.pressed = False
            new_state = self.game.state_game_info[3]
            new_state.enter_state()
        
            
        elif self.Back.pressed == True:
            self.Back.pressed = False
            new_state = self.game.state_page[1]
            new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Back.draw_image(display, 'Back.png')
        self.Bg.draw_image(display, 'Game_rule5.png')
        self.Bg_line.draw_image(display, 'BG_line.png')
        self.Tab.draw_image(display, 'Tab.png')
        self.General_box.draw_image(display, 'Unselected_header.png')
        self.General_text.draw_text(display)
        self.Components_box.draw_image(display, 'Unselected_header.png')
        self.Components_text.draw_text(display)
        self.Setup_box.draw_image(display, 'Unselected_header.png')
        self.Setup_text.draw_text(display)
        self.GamePlay_box.draw_image(display, 'Unselected_header.png')
        self.GamePlay_text.draw_text(display)
        self.HowToWin_box.draw_image(display, 'Selected_header.png')
        self.HowToWin_text.draw_text(display)