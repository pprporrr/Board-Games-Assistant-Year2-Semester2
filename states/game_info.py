import os, time, pygame
from states.state import State
from states.game_rule_1 import Game_rule_1
from states.detect_state import detect_state

class Game_info(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Home_button = Button("HOME", 20, (255, 255, 255), (0, 0, 0), (85, 33), (829, 79))
        self.Categgory_button = Button("CATEGORY", 20, (255, 255, 255), (0, 0, 0), (154, 33), (933, 79))
        self.Mylist_button = Button("MY LIST", 20, (255, 255, 255), (0, 0, 0), (123, 33), (1097, 79))
        self.Back = Button("BACK", 20, (255, 255, 255), (0, 0, 0), (85, 33), (153, 79))
        self.Bg = Button("", 20, (255, 255, 255), (255, 255, 255), (986, 670), (307, 180))
        self.Avalon_info = Button("", 20, (255, 255, 255), (255, 255, 255), (386, 382), (363, 239))
        self.Play = Button("", 28, (255, 255, 255), (219, 160, 90, 76.5), (197, 55), (552, 752))
        self.Rule = Button("", 28, (255, 255, 255), (116, 116, 116, 112.5), (197, 55), (552, 659))
        self.Play_icon = Button("", 1, (0, 0, 0, 0), (0, 0, 0, 0), (46, 37), (588, 761))
        self.Rule_icon = Button("", 1, (0, 0, 0, 0), (0, 0, 0, 0), (33, 28), (591, 671))
        
    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Home_button.check_click()
        self.Categgory_button.check_click()
        self.Mylist_button.check_click()
        self.Back.check_click()
        self.Rule.check_click()
        self.Play.check_click()
        
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
            
        elif self.Rule.pressed == True:
            print('Game_rule click')
            self.Rule.pressed = False
            new_state = Game_rule_1(self.game)
            new_state.enter_state()
            
        elif self.Play.pressed == True:
            print('Play click')
            self.Rule.pressed = False
            new_state = detect_state(self.game)
            new_state.enter_state()
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Home_button.draw(display)
        self.Categgory_button.draw(display)
        self.Mylist_button.draw(display)
        self.Back.draw(display)
        self.Bg.draw_image(display, 'BG.png')
        self.Avalon_info.draw_image(display, 'Avalon_info.png')
        self.game.draw_text(display, 'Avalon', 72, (255, 255, 255), (791, 209))
        self.game.draw_text(display, 'Overview', 28, (255, 255, 255), (791, 429))
        self.game.draw_text(display, 'Avalon is a popular social deduction game that ', 16, (255, 255, 255), (836, 306))
        self.game.draw_text(display, 'requires players to identify and eliminate members of ', 16, (255, 255, 255), (791, 331))
        self.game.draw_text(display, 'opposing teams', 16, (255, 255, 255), (791, 356))
        
        self.game.draw_text(display, ' - 5 to 10 players', 16, (255, 255, 255), (824, 479))
        self.game.draw_text(display, ' - each player assigned a role card', 16, (255, 255, 255), (824, 507))
        self.game.draw_text(display, ' - 2 teams - the Good and the Evil Team.', 16, (255, 255, 255), (824, 535))
        
        self.game.draw_text(display, 'Game play', 28, (255, 255, 255), (791, 603))
        self.game.draw_text(display, 'Players take turns being the leader and selecting a', 16, (255, 255, 255), (842, 657))
        self.game.draw_text(display, 'team for a mission. All players then vote on whether to', 16, (255, 255, 255), (806, 682))
        self.game.draw_text(display, 'approve the team or not. Approved players go on the', 16, (255, 255, 255), (806, 707))
        self.game.draw_text(display, 'mission and secretly decide whether to succeed or fail, ', 16, (255, 255, 255), (806, 732))
        self.game.draw_text(display, 'which determines the missions outcome.', 16, (255, 255, 255), (806, 757))
        self.game.draw_text(display, 'Then the mission outcomes determine whether ', 16, (255, 255, 255), (842, 782))
        self.game.draw_text(display, 'which teams won the game.', 16, (255, 255, 255), (806, 807))
        
        self.Play.draw_with_border(display, 2, (255, 255, 255))
        self.game.draw_text(display, 'PLAY', 28, (255, 255, 255), (634, 763))
        self.Rule.draw_with_border(display, 2, (255, 255, 255))
        self.game.draw_text(display, 'RULES', 28, (255, 255, 255), (632, 670))
        
        self.Play_icon.draw_image(display, 'Play arrow.png')
        self.Rule_icon.draw_image(display, 'Menu book.png')

        
class Button:
    def __init__(self, text, Text_size, Text_color, button_color, width_height, pos ):
        gui_font = pygame.font.Font(os.path.join("assets", "font", "Lexend-VariableFont_wght.ttf"), Text_size)
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
        image = pygame.image.load(os.path.join("assets", "Game_info", image))
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