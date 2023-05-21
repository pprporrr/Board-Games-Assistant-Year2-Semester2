import os, time, pygame
from states.state import State, Button, Dectect
from states.no_winner import No_winer
from states.good_win import Good_win

class Success_page(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.start_count = True
        self.dic_track_round = {1 : (46, 820), 2 : (135, 820), 3 : (224, 820), 4 : (313, 820), 5 : (402, 820)}
        
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (426, 170))
        self.Quest_Succeed = Button("Quest success!", "Amita-Regular.ttf", 72, (50, 192, 47), (255, 255, 255), (467, 140), (566, 358))
        self.Describe = Button("good team gets a point!", "Amita-Regular.ttf", 36, (255, 255, 255), (255, 255, 255), (379, 70), (613, 497))
        self.Phase = Button("Quest Phase", "Amita-Regular.ttf", 36, (255, 255, 255), (255, 255, 255), (200, 70), (148, 25))
        
        self.Player_leader = Button(f"Leader : player {self.game.team_leader}", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (291, 78), (673, 792))
        self.Track_round = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), self.dic_track_round[self.game.vote_track])
        
        self.Quest_result1 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1131, 819))
        self.Quest_result2 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1221, 819))
        self.Quest_result3 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1310, 819))
        self.Quest_result4 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1399, 819))
        self.Quest_result5 = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), (1487, 819))
        
    def update(self, delta_time, action):
        
        self.game.reset_keys()
        self.Track_round = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (63, 63), self.dic_track_round[self.game.vote_track])
        
        if self.start_count == True:
            self.game.good_team_win += 1
            self.game.dic_result[self.game.quest_track] = "success"
            self.game.quest_track += 1
            time.sleep(3)
            
            if self.game.good_team_win == 3:
                new_state = Good_win(self.game)
                new_state.enter_state()
            
            elif self.game.evil_team_win != 3:
                new_state = No_winer(self.game)
                new_state.enter_state()
            
            
        
    def render(self, display):
        display.fill((0, 0, 0))
        self.Bg.draw_image(display, 'Gameplay_background.png')
        self.Table.draw_image(display, 'Table.png')

        self.Player_leader.draw_text(display)
        self.Quest_Succeed.draw_text(display)
        self.Describe.draw_text(display)
        self.Phase.draw_text(display)
        
        self.Track_round.draw_image(display, "Track_round.png")
        for i in range(1, 5, 1):
            if self.game.dic_result[i] != None:
                if i == 1:
                    if self.game.dic_result[1] == "success":
                         self.Quest_result1.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[1] == "fail":
                        self.Quest_result1.draw_image(display, "Quest_failed.png")
                        
                elif i == 2:
                    if self.game.dic_result[2] == "success":
                         self.Quest_result2.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[2] == "fail":
                        self.Quest_result2.draw_image(display, "Quest_failed.png")
                        
                elif i == 3:
                    if self.game.dic_result[3] == "success":
                         self.Quest_result3.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[3] == "fail":
                        self.Quest_result3.draw_image(display, "Quest_failed.png")
                        
                elif i == 4:
                    if self.game.dic_result[4] == "success":
                         self.Quest_result4.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[4] == "fail":
                        self.Quest_result4.draw_image(display, "Quest_failed.png")
                        
                elif i == 5:
                    if self.game.dic_result[5] == "success":
                         self.Quest_result5.draw_image(display, "Quest_successed.png")
                         
                    elif self.game.dic_result[5] == "fail":
                        self.Quest_result5.draw_image(display, "Quest_failed.png")
        