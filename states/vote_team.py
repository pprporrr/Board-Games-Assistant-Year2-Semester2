import os, time, pygame
from states.state import State, Button, Dectect
from states.denied_page import Denied
from states.approved_page import Approved

class Vote_team(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Vote_time = Button("VOTE TIME!", "FugazOne-Regular.ttf", 50, (255, 245, 0), (255, 255, 255), (282, 73), (659, 310))
        self.Text_time = Button(f"team approval !", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (471, 124), (564, 381))
        self.Hand = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (334, 158), (652, 524))
        self.time = 10
        self.start_count = True
        
    def update(self, delta_time, action):
        
        if self.time >= 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button(f"team approval ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (471, 124), (564, 381))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button(f"team approval ..", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (471, 124), (564, 381))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button(f"team approval .", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (471, 124), (564, 381))
            # print(self.time_bar)
            self.time -= 1
            time.sleep(1)
            
        if self.time < 0 and self.start_count == True:
            self.start_count = False
            hand_count = self.Dectect.count_hand()
            print(hand_count)
            if hand_count >= self.game.num_player/2:
                print("Approved")
                new_state = Approved(self.game)
                new_state.enter_state()
                
            else:
                print("Denied")
                new_state = Denied(self.game)
                new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Vote_time.draw_text(display)
        self.Text_time.draw_text(display)
        self.Hand.draw_image(display, "Hand.png")
        
        