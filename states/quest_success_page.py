import os, time, pygame
from states.state import State, Button, Dectect

class Success_page(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Succeed = Button("SUCCEED!", "FugazOne-Regular.ttf", 80, (33, 223, 40), (255, 255, 255), (367, 117), (609, 342))
        self.Approve_img = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (171, 142.78), (715, 496))
        self.start_count = True
        
    def update(self, delta_time, action):
            
        if self.start_count == True:
            self.game.good_team_win += 1
            self.game.dic_result[self.game.quest_track] = "success"
            time.sleep(5)
            
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Succeed.draw_text(display)
        self.Approve_img.draw_image(display, "Approved.png")
        
        