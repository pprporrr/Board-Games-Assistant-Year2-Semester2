import os, time, pygame
# Load our scenes
from states.home import Home
from states.game_info import Game_info
from states.start_game import Start_game
from states.team_think import Team_think
from states.game_rule_1 import Game_rule_1
from states.game_rule_2 import Game_rule_2
from states.game_rule_3 import Game_rule_3
from states.game_rule_4 import Game_rule_4
from states.game_rule_5 import Game_rule_5

class Game():
    def __init__(self):
        pygame.init()
        self.GAME_W,self.GAME_H = 1600, 900
        self.SCREEN_WIDTH,self.SCREEN_HEIGHT = 1600, 900
        self.game_canvas = pygame.surface.Surface((self.GAME_W,self.GAME_H))
        self.screen = pygame.display.set_caption("Board Game Assistant")
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH,self.SCREEN_HEIGHT))
        self.running, self.playing = True, True
        self.actions = {"left": False, "right": False, "up" : False, "down" : False, "action1" : False, "action2" : False, "start" : False}
        self.dt, self.prev_time = 0, 0
        self.state_stack = []
        self.load_assets()
        self.load_states()
        self.num_player = 0
        self.dic_result = {1 : "success", 2 : "fail", 3 : None, 4 : None, 5 : None}
        self.result_position = [(93, 761), (209, 761), (325, 761), (), ()]
        self.good_team_win = 0
        self.evil_team_win = 0
        self.team_leader = 1
        self.vote_track = 1 # Track the number when vote the approval team is denie
        self.quest_track = 1 # track the round of quest
        self.num_playler_team = {(1, 0) : 2, 
                                 (1, 5) : 2, (2, 5) : 3, (3, 5) : 2, (4, 5) : 3, (5, 5) : 3,
                                 (1, 6) : 2, (2, 6) : 3, (3, 6) : 4, (4, 6) : 3, (5, 6) : 4,
                                 (1, 7) : 2, (2, 7) : 3, (3, 7) : 3, (4, 7) : 4, (5, 7) : 4,
                                 (1, 8) : 3, (2, 8) : 4, (3, 8) : 4, (4, 8) : 5, (5, 8) : 5,
                                 (1, 9) : 3, (2, 9) : 4, (3, 9) : 4, (4, 9) : 5, (5, 9) : 5,
                                 (1, 10) : 3, (2, 10) : 4, (3, 10) : 4, (4, 10) : 5, (5, 10) : 5}
        self.state_page = [Home(self), Game_info(self), Team_think(self)]
        self.state_game_info = [Game_rule_1(self), Game_rule_2(self), Game_rule_3(self), Game_rule_4(self), Game_rule_5(self)]
        

        # # Core attributes
        # self.pressed = False

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
        # Render current state to the screen
        self.screen.blit(pygame.transform.scale(self.game_canvas,(self.SCREEN_WIDTH, self.SCREEN_HEIGHT)), (0,0))
        pygame.display.flip()


    def get_dt(self):
        now = time.time()
        self.dt = now - self.prev_time
        self.prev_time = now

    def draw_text(self, surface, text, Text_size, Text_color, pos):
        # text_surface = self.font.render(text, True, color)
        gui_font = pygame.font.Font(os.path.join("assets", "font", "Lexend-VariableFont_wght.ttf"), Text_size)
        text_surface = gui_font.render(text, True, Text_color)
        #text_surface.set_colorkey((0,0,0))
        text_rect = text_surface.get_rect(topleft = pos)
        # text_rect.center = (pos)
        surface.blit(text_surface, text_rect)
        
    def create_rect_border(self, surface, rect_size, border, rect_color, border_color, pos):
        surf = pygame.Surface((rect_size[0]+border*2, rect_size[1]+border*2), pygame.SRCALPHA)
        pygame.draw.rect(surf, rect_color, (border, border, rect_size[0], rect_size[1]), 0)
        for i in range(1, border):
            pygame.draw.rect(surf, border_color, (border-i, border-i, rect_size[0], rect_size[1]), 1)
        
        surface.blit(surf, pos)

    def load_assets(self):
        # Create pointers to directories 
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
            
if __name__ == "__main__":
    g = Game()
    while g.running:
        g.game_loop()