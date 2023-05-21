import os, time, pygame
from states.state import State, Button, Dectect
from states.role import Role_state


class Confirm_people_state(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.num_player_pic = 'Table.png'
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1, 1), (386, 105))
        self.Num_people = Button(f"{self.game.num_player} players", "Amita-Regular.ttf", 88, (255, 255, 255), (255, 255, 255), (615, 200), (615, 336))
        self.Try_again = Button("try again", "Amita-Regular.ttf", 32, (255, 255, 255), (143, 22, 22, 76.5), (179, 54), (602, 494))
        self.Confirm = Button("confirm", "Amita-Regular.ttf", 32, (255, 255, 255), (63, 142, 22, 76.5), (179, 54), (819, 494))
        self.start = False
        
        
    def update(self, delta_time, action):
        
        if self.game.num_player == 5:
            self.num_player_pic = 'Table5people.png'
            self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (815, 627), (386, 105))
            
        elif self.game.num_player == 6:
            self.num_player_pic = 'Table6people.png'
            self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 659), (426, 105))
                
        self.game.reset_keys()
        self.Try_again.check_click()
        self.Confirm.check_click()
        
        
        if self.Try_again.pressed == True:
            self.Try_again.pressed = False
            self.exit_state()
            
        elif self.Confirm.pressed == True:
            self.Confirm.pressed = False
            new_state = Role_state(self.game)
            new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, self.num_player_pic)
        
        self.Num_people.draw_text(display)
        self.Try_again.draw_with_border(display, 5, (143, 22, 22))
        self.Confirm.draw_with_border(display, 5, (63, 142, 35))
        
        
        