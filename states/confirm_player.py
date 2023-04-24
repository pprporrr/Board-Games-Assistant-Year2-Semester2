import os, time, pygame
from states.state import State, Button, Dectect
from states.team_think import Team_think


class Confirm_people_state(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Num_people = Button(f"{self.game.num_player} players", "Amita-Regular.ttf", 88, (255, 255, 255), (255, 255, 255), (615, 200), (615, 336))
        self.Try_again = Button("try again", "Amita-Regular.ttf", 32, (255, 255, 255), (143, 22, 22, 76.5), (179, 54), (602, 494))
        self.Confirm = Button("confirm", "Amita-Regular.ttf", 32, (255, 255, 255), (63, 142, 22, 76.5), (179, 54), (819, 494))
        self.start = False
        
        
    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Try_again.check_click()
        self.Confirm.check_click()
        
        
        if self.Try_again.pressed == True:
            self.exit_state()
            self.Try_again.pressed = False
            
        elif self.Confirm.pressed == True:
            self.Confirm.pressed = False
            new_state = Team_think(self.game)
            new_state.enter_state()
            
            
    
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Num_people.draw_text(display)
        self.Try_again.draw_with_border(display, 5, (143, 22, 22))
        self.Confirm.draw_with_border(display, 5, (63, 142, 35))
        
        
        