import os, time, pygame
from states.state import State, Button, Dectect
from states.confirm_player import Confirm_people_state

class Detect_state(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.time = 10
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        # self.Text_1 = Button("Detecting players ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
        self.Text_time = Button(f"Detecting players !", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
        
        self.num_people = int()
        self.start_count = True
        
        
    def update(self, delta_time, action):
        
        self.game.reset_keys() 
            
        if self.time >= 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button(f"Detecting players ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button(f"Detecting players ..", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button(f"Detecting players .", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
            
            self.time -= 1
            time.sleep(1)
            
            
        if self.time < 0 and self.start_count == True:
            self.start_count = False
            self.time = 10
            num_people = self.Dectect.count_people()
            self.game.num_player = num_people
            # print(self.game.num_player)
            print("Done count")
            new_state = Confirm_people_state(self.game)
            new_state.enter_state()
            self.start_count = True
    
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        
        # self.Text_1.draw_text(display)
        self.Text_time.draw_text(display)
        
        
        