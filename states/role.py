import os, time, pygame
from states.state import State, Button, Dectect
from states.team_think import Team_think

class Role_state(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.time = 180
        self.ori_time = 180
        self.num_people = int()
        self.start_count = True
        self.circle = 270
        
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Role = Button(f"know your role!", "Amita-Regular.ttf", 64, (238, 215, 10), (255, 255, 255), (493, 132), (567, 290))
        self.Phase_BG = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 131), (0, 0))
        self.Descrip = Button(f"use mobile app to scan character info", "Amita-Regular.ttf", 36, (255, 255, 255), (255, 255, 255), (618, 70), (491, 424))
        self.Set_up = Button(f"Setup Phase", "Amita-Regular.ttf", 36, (255, 255, 255), (255, 255, 255), (201, 78), (157, 25))
        self.Done = Button("", "Amita-Regular.ttf", 20, (255, 255, 255), (255, 255, 255), (159, 69), (1378, 785))
        self.arc = Button("", "Amita-Regular.ttf", 64, (255, 255, 255), (0, 0, 0), (112, 112), (744, 555))
        self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
        
        
    def update(self, delta_time, action):
        
        self.game.reset_keys() 
        
            
        if self.time > 0 and self.start_count == True:            
            self.time -= 1
            self.circle = self.circle - (360/self.ori_time)
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            time.sleep(1)
            
            
        elif self.time == 0 and self.start_count == True:
            self.start_count = False
            self.circle = 270
            self.time = self.ori_time
            self.Text_time1 = Button(f"0", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            # print(self.game.num_player)
            
        elif self.start_count == False:
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            self.start_count = True
            new_state = Team_think(self.game)
            new_state.enter_state()
            
        self.Done.check_click()
        
        if self.Done.pressed == True:
            self.Done.pressed = False
            new_state = Team_think(self.game)
            new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Phase_BG.draw_image(display, 'Phase_BG.png')
        self.Role.draw_text(display)
        self.Descrip.draw_text(display)
        self.Done.draw_image(display, 'Done_button.png')
        self.Set_up.draw_text(display)
        self.arc.draw_arc(display, -90, self.circle, 50, 4)
        self.Text_time1.draw_text_center(display)