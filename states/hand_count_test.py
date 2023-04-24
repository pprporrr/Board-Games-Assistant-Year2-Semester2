import os, time, pygame
from states.state import State, Button, Dectect

class hand_count(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.start_count = False
        self.Dectect = Dectect(Dectect)
        
    def update(self, delta_time, action):
        
        if self.start_count == False:
            self.start_count = True
            self.Dectect.count_hand()
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        # self.Text_1.draw_text(display)
        
        