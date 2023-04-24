import os, time, pygame
from states.state import State, Button, Dectect
from states.detect_state import Detect_state

class Start_game(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.Dectect = Dectect(Dectect)
        self.time = 0
        self.Avalon_Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255, 0), (748, 561), (426, 170))
        # self.Text_1 = Button("Detecting players ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
        self.Wecome_text = Button("welcome to...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (363, 124), (610, 198))
        self.Avalon_text1 = Button("AVALON", "Amita-Regular.ttf", 200, (219, 160, 90), (255, 255, 255), (768, 388), (407, 253))
        self.Avalon_text2 = Button("AVALON", "Amita-Regular.ttf", 200, (0, 0, 0), (255, 255, 255), (768, 388), (426, 260))
        self.Press_to_start = Button("[ PRESS ENTER TO START ]", "FugazOne-Regular.ttf", 32, (255, 255, 255), (255, 255, 255), (422, 47), (589, 696))
        self.Blank = Button("", "FugazOne-Regular.ttf", 32, (255, 255, 255), (255, 255, 255, 0), (1600, 900), (0, 901))
        self.Start= Button("", "FugazOne-Regular.ttf", 96, (255, 255, 255, 0), (255, 255, 255), (343, 141), (629, 380))


        self.start_count = True
        self.text_transition = False
        self.pic_transition = False
        self.run1 = 0
        self.run2 = 0
        
        
    def update(self, delta_time, actions):
        
        # self.game.reset_keys()
        
        if self.start_count == True and self.pic_transition == False and self.text_transition == False:
            if (self.time) % 2 == 1:
                self.Press_to_start = Button(f"", "FugazOne-Regular.ttf", 32, (255, 255, 255), (255, 255, 255), (422, 47), (589, 696))
                
            elif (self.time) % 2 == 0:
                self.Press_to_start = Button(f"[ PRESS ENTER TO START ]", "FugazOne-Regular.ttf", 32, (255, 255, 255), (255, 255, 255), (422, 47), (589, 696))
            self.time += 1
            time.sleep(0.5)
                
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:   
                if event.key == pygame.K_RETURN:
                    self.pic_transition = True
                    self.start_count = False
                    self.Blank = Button("", "FugazOne-Regular.ttf", 32, (255, 255, 255), (255, 255, 255, 255), (1600, 900), (0, 0))
                    self.Wecome_text = Button("", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (363, 124), (610, 198))
                    self.Avalon_text1 = Button("", "Amita-Regular.ttf", 200, (219, 160, 90), (255, 255, 255), (768, 388), (407, 253))
                    self.Avalon_text2 = Button("", "Amita-Regular.ttf", 200, (0, 0, 0), (255, 255, 255), (768, 388), (426, 260))
                    
        if self.pic_transition == True and self.run1 != 250:
            self.run1 += 25
            self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255, self.run1), (748, 561), (426, 170))

                
        elif self.pic_transition == True and self.run1 == 250:
            self.pic_transition = False
            self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255, 255), (748, 561), (426, 170))
            self.text_transition = True
                
        if self.text_transition == True and self.run2 != 250:
            self.run2 += 25
            self.Start = Button("START!", "FugazOne-Regular.ttf", 96, (255, 255, 255, self.run2), (255, 255, 255), (343, 141), (629, 380))
                
        elif self.text_transition == True and self.run2 == 250:
            self.text_transition = False
            self.Start = Button("START!", "FugazOne-Regular.ttf", 96, (255, 255, 255, 255), (255, 255, 255), (343, 141), (629, 380))
            
        if self.text_transition == False and self.run2 == 250:
            time.sleep(5)
            new_state = Detect_state(self.game)
            new_state.enter_state()
            
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Avalon_Bg.draw_image(display, 'Welcom_BG.png')
        self.Wecome_text.draw_text(display)
        self.Avalon_text2.draw_text(display)
        self.Avalon_text1.draw_text(display)
        self.Press_to_start.draw_text(display)
        self.Blank.draw_image(display, 'Blank.png')
        self.Table.draw_image(display, 'Table.png')
        self.Start.draw_text(display)       
        