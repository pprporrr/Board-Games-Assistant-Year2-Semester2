import os, time, pygame
from states.state import State, Button, Dectect

class Fail_page (State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Failed = Button("FAILED!", "FugazOne-Regular.ttf", 80, (255, 0, 0), (255, 255, 255), (293, 117), (656, 342))
        self.X = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (156.29, 139.12), (720.51, 485.52))
        self.start_count = True
        
    def update(self, delta_time, action):
            
        if self.start_count == True:
            self.game.evil_team_win += 1
            time.sleep(5)
            
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Failed.draw_text(display)
        self.X.draw_image(display, "Denied.png")
        
        