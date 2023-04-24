import os, time, pygame
from states.state import State
from states.vote_count_test import vote_count

class vote(State):
    def __init__(self, game):
        State.__init__(self, game)
        self.vote_button = Button("Click to start detect", "Lexend-VariableFont_wght.ttf", 20, (0, 0, 0), (255, 255, 255), (300, 33), (800, 450))
        
    def update(self, delta_time, action):
        
        self.vote_button.check_click()
        if self.vote_button.pressed == True:
            print('vote_button click')
            self.vote_button.pressed = False
            new_state = vote_count(self.game)
            new_state.enter_state()
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        # self.vote_button.draw(display)
        self.vote_button.draw_with_border(display, 2, (255, 255, 255))
        
        # self.game.draw_text(display, 'Detecting players ...', 64, (255, 255, 255), (512, 381))
        # self.Text_1.draw_text(display)
        
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
        text_rect = self.text_surf.get_rect(topleft = self.pos)
        surface.blit(self.text_surf, text_rect)
        