import os, time, pygame
from states.state import State
from states.game_info import Game_info

class Home(State):
    def __init__(self, game):
        State.__init__(self, game)
        # self.GAME_W,self.GAME_H = 1600, 900
        # self.game_canvas = pygame.Surface((self.GAME_W,self.GAME_H))
        # self.display1 = self.game_canvas
        # # self.buttons = {}
        # self.buttons['Home_button'] = Button(self.display1, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        # self.buttons['Categgory_button'] = Button(self.display1, "CATEGORY", 20, (255, 255, 255), (0, 255, 0), (154, 33), (854, 49))
        # self.buttons['Mylist_button'] = Button(self.display1, "MY LIST", 20, (255, 255, 255), (0, 0, 255), (123, 33), (1018, 49))
        
        self.Home_button = Button("HOME", 20, (255, 255, 255), (0, 0, 0), (85, 33), (829, 79))
        self.Categgory_button = Button("CATEGORY", 20, (255, 255, 255), (0, 0, 0), (154, 33), (933, 79))
        self.Mylist_button = Button("MY LIST", 20, (255, 255, 255), (0, 0, 0), (123, 33), (1097, 79))
        self.Avalon_game = Button("", 20, (255, 255, 255), (255, 255, 255), (994, 312), (314, 195))
        self.test = Button("TEST", 20, (255, 255, 255), (219, 160, 90), (281.72, 312), (1026.28, 559))
        
    def update(self, delta_time, action):
        # self.buttons['Home_button'] = Button(self.display, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        # self.buttons['Categgory_button'] = Button(self.display, "CATEGORY", 20, (255, 255, 255), (0, 255, 0), (154, 33), (854, 49))
        # self.buttons['Mylist_button'] = Button(self.display, "MY LIST", 20, (255, 255, 255), (0, 0, 255), (123, 33), (1018, 49))
        
        self.game.reset_keys()
        self.Home_button.check_click()
        self.Categgory_button.check_click()
        self.Mylist_button.check_click()
        self.Avalon_game.check_click()
        if self.Home_button.pressed == True:
            print('Home_button click')
            
        elif self.Categgory_button.pressed == True:
            print('Categgory_button click')
            
        elif self.Mylist_button.pressed == True:
            print('Mylist_button click')
            
        elif self.Avalon_game.pressed == True:
            print('Avalon_game click')
            self.Avalon_game.pressed = False
            new_state = Game_info(self.game)
            new_state.enter_state()
        
    def render(self, display):
        display.fill((0, 0, 0))
        # draw_button(self, surface, text, Text_size, Text_color, button_color, width_height, pos)
        # Button1 = self.Button(display, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        
        # self.Home_button = self.game.draw_button(display, "HOME", 20, (255, 255, 255), (255, 0, 0), (85, 33), (749, 49))
        # self.Categgory_button = self.game.draw_button(display, "CATEGORY", 20, (255, 255, 255), (0, 255, 0), (154, 33), (854, 49))
        # self.Mylist_button = self.game.draw_button(display, "MY LIST", 20, (255, 255, 255), (0, 0, 255), (123, 33), (1018, 49))
        
        
        # self.Home_button.draw_with_border(display, 2, (0, 0, 255))
        # self.Categgory_button.draw_with_border(display, 2, (255, 255, 255))
        # self.Mylist_button.draw_with_border(display, 2, (255, 255, 255))
        self.Home_button.draw(display)
        self.Categgory_button.draw(display)
        self.Mylist_button.draw(display)
        self.Avalon_game.draw_image(display, 'Avalon_button.png')
        self.game.draw_text(display, "Available", 28, (137, 137, 137), (291, 145))
        self.game.draw_text(display, "AVALON", 96, (255, 255, 255), (343, 376))
        self.game.draw_text(display, "Comingsoon...", 28, (137, 137, 137), (291, 517))
        self.game.create_rect_border(display, (281.72, 312), 2, (0, 0, 0), (255, 255, 255), (314.48, 559))
        self.game.create_rect_border(display, (281.72, 312), 2, (0, 0, 0), (255, 255, 255), (670, 559))
        self.game.create_rect_border(display, (281.72, 312), 2, (0, 0, 0), (255, 255, 255), (1026.28, 559))
        # self.test.create_rect_border(display, 2, (255, 255, 255))

        # self.buttons['Home_button'].draw()
        # self.buttons['Categgory_button'].draw()
        # self.buttons['Mylist_button'].draw()
        
        
class Button:
    def __init__(self, text, Text_size, Text_color, button_color, width_height, pos ):
        gui_font = pygame.font.Font(os.path.join("assets", "font", "Lexend-VariableFont_wght.ttf"), Text_size)
        self.pos = pos
        # self.surface = surface
        
        # Core attributes
        self.pressed = False
        
        # Top rectangle
        self.width_height = width_height
        self.top_rect = pygame.Rect(pos, width_height)
        self.top_color = button_color
        
        # text
        self.text_surf = gui_font.render(text, True, Text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.top_color, self.top_rect)
        # text_rect.center = (pos[0] + width_height[0]/2, pos[1] + width_height[1]/2)
        surface.blit(self.text_surf, self.text_rect)
        # self.check_click()
        
    def draw_image(self, surface, image):
        image = pygame.image.load(os.path.join("assets", "Home_pic", image))
        image = pygame.transform.scale(image, self.width_height)
        pygame.draw.rect(surface, self.top_color, self.top_rect)
        # text_rect.center = (pos[0] + width_height[0]/2, pos[1] + width_height[1]/2)
        surface.blit(image, self.top_rect)
        # self.check_click()
        
    def draw_with_border(self, surface, border, border_color):
        surf = pygame.Surface((self.width_height[0]+border*2, self.width_height[1]+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.top_color, (border, border, self.width_height[0], self.width_height[1]), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, self.width_height[0], self.width_height[1]), 1)
        surface.blit(surf, self.pos)
        surface.blit(self.text_surf, self.text_rect)
        
    def check_click(self):
        mouse_pos = pygame.mouse.get_pos()        
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.pressed = True

            else:
                if self.pressed == True:
                    print('click')
                    self.pressed = False