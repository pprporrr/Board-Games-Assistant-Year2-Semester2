import os, time, pygame
from states.state import State

class detect_state(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Home_button = Button("HOME", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (85, 33), (829, 79))
        self.Categgory_button = Button("CATEGORY", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (154, 33), (933, 79))
        self.Mylist_button = Button("MY LIST", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (123, 33), (1097, 79))
        self.Back = Button("BACK", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (0, 0, 0), (85, 33), (153, 79))
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Text_1 = Button("Detecting players ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (574, 124), (512, 381))
        
    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Home_button.check_click()
        self.Categgory_button.check_click()
        self.Mylist_button.check_click()
        self.Back.check_click()
        
        if self.Home_button.pressed == True:
            print('Home_button click')
            self.exit_state()
            self.Home_button.pressed = False
            
        elif self.Categgory_button.pressed == True:
            print('Categgory_button click')
            
        elif self.Mylist_button.pressed == True:
            print('Mylist_button click')
            
        elif self.Back.pressed == True:
            self.exit_state()
            self.Back.pressed = False
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Home_button.draw(display)
        self.Categgory_button.draw(display)
        self.Mylist_button.draw(display)
        self.Back.draw(display)
        self.Bg.draw_image(display, 'BG.png')
        self.Table.draw_image(display, 'Table.png')
        
        # self.game.draw_text(display, 'Detecting players ...', 64, (255, 255, 255), (512, 381))
        self.Text_1.draw_text(display)
        
class Button:
    def __init__(self, text, text_font, Text_size, Text_color, button_color, width_height, pos):
        gui_font = pygame.font.Font(os.path.join("assets", "font", text_font), Text_size)
        self.pos = pos
        self.pressed = False
        self.width_height = width_height
        self.top_rect = pygame.Rect(pos, width_height)
        self.top_color = button_color
        self.text_surf = gui_font.render(text, True, Text_color)
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
    def draw(self, surface):
        pygame.draw.rect(surface, self.top_color, self.top_rect)
        surface.blit(self.text_surf, self.text_rect)
        
    def draw_image(self, surface, image):
        image = pygame.image.load(os.path.join("assets", "Detect_pic", image))
        image = pygame.transform.scale(image, self.width_height)
        surface.blit(image, self.pos)
        
    def draw_with_border(self, surface, border, border_color):
        surf = pygame.Surface((self.width_height[0]+border*2, self.width_height[1]+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, self.top_color, (border, border, self.width_height[0], self.width_height[1]), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, self.width_height[0], self.width_height[1]), 1)
        surface.blit(surf, self.top_rect)
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
                    
    def draw_text(self, surface):
        # gui_font = pygame.font.Font(os.path.join("assets", "font", self.text_font), self.Text_size)
        # text_surface = gui_font.render(self.text, True, self.Text_color)
        text_rect = self.text_surf.get_rect(topleft = self.pos)
        surface.blit(self.text_surf, text_rect)