import os, time, pygame
from states.state import State, Button, Dectect
from states.confirm_player import Confirm_people_state

class Detect_state(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.time = 5
        self.ori_time = 5
        self.num_people = int()
        self.start_count = True
        self.circle = 270
        
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Text_time = Button(f"Detecting players !", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
        self.arc = Button("", "Amita-Regular.ttf", 64, (255, 255, 255), (0, 0, 0), (112, 112), (744, 555))
        self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
        
        
    def update(self, delta_time, action):
        
        self.game.reset_keys() 
            
        if self.time > 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button(f"Detecting players ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button(f"Detecting players ..", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button(f"Detecting players .", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
            
            self.time -= 1
            self.circle = self.circle - (360/self.ori_time)
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            time.sleep(1)
            
            
        elif self.time == 0 and self.start_count == True:
            self.start_count = False
            self.circle = 270
            self.time = self.ori_time
            self.Text_time1 = Button(f"0", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            num_people = self.Dectect.count_people()
            self.game.num_player = num_people
            # print(self.game.num_player)
            print("Done count")
            
        elif self.start_count == False:
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 611))
            self.start_count = True
            new_state = Confirm_people_state(self.game)
            new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Text_time.draw_text(display)
        self.arc.draw_arc(display, -90, self.circle, 50, 4)
        self.Text_time1.draw_text_center(display)
        