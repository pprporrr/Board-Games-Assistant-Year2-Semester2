import os, time, pygame
from states.state import State, Button, Dectect

class Quest_reveal(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Reveal = Button("REVEAL!", "FugazOne-Regular.ttf", 50, (255, 245, 0), (255, 255, 255), (201, 73), (700, 310))
        self.Text_time = Button(f"quest result !", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
        self.Eye = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (164, 128.42), (718, 529))
        self.time = 5
        self.start_count = True
        
    def update(self, delta_time, action):
        
        if self.time >= 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button(f"quest result ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button(f"quest result ..", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button(f"quest result .", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (382, 124), (608, 381))
            # print(self.time_bar)
            self.time -= 1
            time.sleep(1)
            
        if self.time < 0 and self.start_count == True:
            self.start_count = False
            num_success = Dectect.count_vote()
            self.game.number_success = num_success
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.game.draw_text(display, "Fucntion: Count the raised hands", 20, (255, 255, 255), (800, 450))
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Reveal.draw_text(display)
        self.Text_time.draw_text(display)
        self.Eye.draw_image(display, "Eye.png")
        
        