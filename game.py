import os, time, pygame
from states.home import Home

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 1600, 900
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 1600, 900
        self.game_canvas = pygame.surface.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.load_states()

    def game_loop(self):
        while self.playing:
            self.get_dt()
            self.get_events()
            self.update()
            self.render()

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.playing = False
                    self.running = False
                if event.key == pygame.K_a:
                    self.actions['left'] = True
                if event.key == pygame.K_d:
                    self.actions['right'] = True
                if event.key == pygame.K_w:
                    self.actions['up'] = True
                if event.key == pygame.K_s:
                    self.actions['down'] = True
                if event.key == pygame.K_p:
                    self.actions['action1'] = True
                if event.key == pygame.K_o:
                    self.actions['action2'] = True
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a:
                    self.actions['left'] = False
                if event.key == pygame.K_d:
                    self.actions['right'] = False
                if event.key == pygame.K_w:
                    self.actions['up'] = False
                if event.key == pygame.K_s:
                    self.actions['down'] = False
                if event.key == pygame.K_p:
                    self.actions['action1'] = False
                if event.key == pygame.K_o:
                    self.actions['action2'] = False
                if event.key == pygame.K_RETURN:
                    self.actions['start'] = False

    def update(self):
        self.state_stack[-1].update(self.dt, self.actions)

    def render(self):
        self.state_stack[-1].render(self.game_canvas)
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()


    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, Text_size, Text_color, pos):
        gui_font = pygame.font.Font(os.path.join("assets", "font", "Lexend-VariableFont_wght.ttf"), Text_size)
        text_surface = gui_font.render(text, True, Text_color)
        text_rect = text_surface.get_rect(topleft = pos)
        surface.blit(text_surface, text_rect)
        
    def create_rect_border(self, surface, rect_size, border, rect_color, border_color, pos):
        surf = pygame.Surface((rect_size[0]+border*2, rect_size[1]+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, rect_color, (border, border, rect_size[0], rect_size[1]), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, rect_size[0], rect_size[1]), 1)
        
        surface.blit(surf, pos)
        
    # def draw_button(self, surface, text, Text_size, Text_color, button_color, width_height, pos):
    #     rect_pos = (pos)
    #     top_rect = pygame.Rect(rect_pos, (width_height))
    #     pygame.draw.rect(surface, button_color, top_rect)
        
    #     gui_font = pygame.font.Font(os.path.join(self.font_dir, "Lexend-VariableFont_wght.ttf"), Text_size)
    #     text_surface = gui_font.render(text, True, Text_color)
    #     text_rect = text_surface.get_rect(center = top_rect.center)
    #     surface.blit(text_surface, text_rect)
        
    #     self.button = Button(surface, text, Text_size, Text_color, button_color, width_height, pos)
    #     self.button.draw()
    #     self.button.check_click()
        
    # def button(self, surface, text, Text_size, Text_color, button_color, width_height, pos):
    #     rect_pos = (pos)
    #     self.top_rect = pygame.Rect(rect_pos, (width_height))
    #     pygame.draw.rect(surface, button_color, self.top_rect)
        
    #     gui_font = pygame.font.Font(os.path.join(self.font_dir, "Lexend-VariableFont_wght.ttf"), Text_size)
    #     text_surface = gui_font.render(text, True, Text_color)
    #     text_rect = text_surface.get_rect(center = self.top_rect.center)
    #     surface.blit(text_surface, text_rect)
        
    # def check_click(self):
    #     mouse_pos = pygame.mouse.get_pos()
    #     if self.top_rect.collidepoint(mouse_pos):
    #         if pygame.mouse.get_pressed()[0]:
    #             self.pressed = True
                
    #         else:
    #             if self.pressed == True:
    #                 print('click')
    #                 self.pressed = False

    def load_assets(self):
        self.assets_dir = os.path.join("assets")
        self.sprite_dir = os.path.join(self.assets_dir, "sprites")
        self.font_dir = os.path.join(self.assets_dir, "font")
        self.font= pygame.font.Font(os.path.join(self.font_dir, "Lexend-VariableFont_wght.ttf"), 20)
    def load_states(self):
        self.home_screen = Home(self)
        self.state_stack.append(self.home_screen)

    def reset_keys(self):
        for action in self.actions:
            self.actions[action] = False
            
# class Button:
#     def __init__(self, surface, text, Text_size, Text_color, button_color, width_height, pos ):
#         gui_font = pygame.font.Font(os.path.join(os.path.join(os.path.join("assets"), "font"), "Lexend-VariableFont_wght.ttf"), Text_size)
#         self.surface = surface
        
#         # Core attributes
#         self.pressed = False
        
#         # Top rectangle
#         self.top_rect = pygame.Rect(pos, width_height)
#         self.top_color = button_color
        
#         # text
#         self.text_surf = gui_font.render(text, True, Text_color)
#         self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)
        
#     def draw(self):
#         pygame.draw.rect(self.surface, self.top_color, self.top_rect)
#         # text_rect.center = (pos[0] + width_height[0]/2, pos[1] + width_height[1]/2)
#         self.surface.blit(self.text_surf, self.text_rect)
#         self.check_click()
        
#     def check_click(self):
#         mouse_pos = pygame.mouse.get_pos()
#         if self.top_rect.collidepoint(mouse_pos):
#             if pygame.mouse.get_pressed()[0]:
#                 self.pressed = True
                
#             else:
#                 if self.pressed == True:
#                     print('click')
#                     self.pressed = False

if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()