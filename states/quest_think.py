import os, time, pygame
from states.state import State, Button, Dectect
from states.quest_vote import Quest_vote

class Quest_think(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Time_to_think = Button("TIME TO THINK!", "FugazOne-Regular.ttf", 50, (255, 0, 184), (255, 255, 255), (385, 73), (608, 310))
        self.Text_time = Button(f"quest result ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
        self.Time_bar_outer = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (1220, 60), (190, 791))
        self.Time_bar_inner = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1200, 40), (200, 801))
        self.think = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (181, 145), (709, 532))
        self.orig_size = self.Time_bar_inner.width_height[0]
        self.orig_time = 20
        self.time_bar = self.Time_bar_inner.width_height[0]
        self.time = 20
        self.start_count = True
        
        
    def update(self, delta_time, action):
        self.game.reset_keys() 
            
        if self.time >= 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button(f"quest result ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button(f"quest result ..", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button(f"quest result .", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
            
            self.Time_bar_inner = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (self.time_bar , 40), (200, 801))
            self.time_bar -= self.orig_size/self.orig_time
            # print(self.time_bar)
            self.time -= 1
            time.sleep(1)
            
        if self.time < 0:
            self.start_count = False
            new_state = Quest_vote(self.game)
            new_state.enter_state()
            
            
        # if self.time < 0 and self.start_count == True:
        #     self.start_count = False
        #     self.time = 10
        #     num_people = self.Dectect.count_people()
        #     self.game.num_player = num_people
        #     print(self.game.num_player)
        #     print("Done count")
        #     new_state = Confirm_people_state(self.game)
        #     new_state.enter_state()
        #     self.start_count = True
            
    
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Time_to_think.draw_text(display)
        self.Text_time.draw_text(display)
        self.Time_bar_outer.draw_image(display, "Outer_bar.png")
        self.Time_bar_inner.draw_image(display, "Inner_bar.png")
        self.think.draw_image(display, "Think.png")
        