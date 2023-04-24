import os, time, pygame
from states.state import State, Button, Dectect
# from states.team_think import Team_think

class Denied(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Denied = Button("DENIED!", "FugazOne-Regular.ttf", 80, (255, 0, 0), (255, 255, 255), (311, 117), (647, 342))
        self.X = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (156.29, 139.12), (720.51, 485.52))
        self.start_count = True
        
    def update(self, delta_time, action):
            
        if self.start_count == True:
            self.game.vote_track += 1
            if self.game.vote_track == 5:
                print("Evil win")
            time.sleep(5)
            new_state = self.game.state_page[2]
            new_state.enter_state()
            
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Denied.draw_text(display)
        self.X.draw_image(display, "Denied.png")
        
        