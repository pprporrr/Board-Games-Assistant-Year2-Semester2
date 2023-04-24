import os, time, pygame
from states.state import State, Button, Dectect
from states.quest_think import Quest_think

class Approved(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Approved = Button("APPROVED!", "FugazOne-Regular.ttf", 80, (33, 223, 40), (255, 255, 255), (437, 117), (584, 342))
        self.Approve_img = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (171, 142.78), (715, 496))
        self.start_count = True
        
    def update(self, delta_time, action):
            
        if self.start_count == True:
            self.game.vote_track = 0
            time.sleep(5)
            new_state = Quest_think(self.game)
            new_state.enter_state()
            
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Approved.draw_text(display)
        self.Approve_img.draw_image(display, "Approved.png")
        
        