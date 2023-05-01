import os, time, pygame
from states.state import State, Button, Dectect
from states.vote_team import Vote_team

class Team_think(State):
    def __init__(self, game):
        State.__init__(self, game)
        
        self.Dectect = Dectect(Dectect)
        self.ori_time = 30
        self.time = 30
        self.start_count = True
        self.circle = 270
        self.dic_quest_round = {1 : "1st", 2 : "2nd", 3 : "3rd", 4 : "4th", 5 : "5th"}
        self.dic_track_round = {1 : (986, 761), 2 : (1102, 761), 3 : (1218, 761), 4 : (1334, 761), 5 : (1450, 761)}
        
        self.Bg = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (1600, 900), (0, 0))
        self.Table = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (748, 561), (445, 170))
        self.Leader_plate = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (364, 95), (445, 42))
        self.Quest_round_plate = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (364, 95), (829, 42))
        self.Player_leader = Button(f"Player {self.game.team_leader} is leader", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (312, 78), (473, 50))
        self.Quest_round = Button(f"{self.dic_quest_round[self.game.quest_track]} Quest", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (156, 78), (935, 50))
        self.Time_to_think = Button("LEADER THINK!", "FugazOne-Regular.ttf", 50, (255, 0, 184), (255, 255, 255), (367, 73), (635, 294))
        self.Text_time = Button(f"team approval ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (484, 124), (577, 367))
        self.Describe = Button("Leader choose players to be on the team.", "Amita-Regular.ttf", 20, (255, 255, 255), (255, 255, 255), (371, 39), (633, 491))
        self.think = Button("", "Lexend-VariableFont_wght.ttf", 20, (255, 255, 255), (255, 255, 255), (139.81, 112), (749, 567))
        self.arc = Button("", "Amita-Regular.ttf", 64, (255, 255, 255), (0, 0, 0), (127, 127), (736, 742))
        self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 806))
        self.Phase = Button("Team Building Phase", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (379, 78), (44, 793))
        self.Track_round_plate = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (614, 132.17), (958, 739))
        self.Track_round = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (88, 88), self.dic_track_round[self.game.vote_track])
        
        
        
    def update(self, delta_time, action):
        self.game.reset_keys()
        if self.start_count == True:
            self.Player_leader = Button(f"Player {self.game.team_leader} is leader", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (312, 78), (473, 50))
            self.Quest_round = Button(f"{self.dic_quest_round[self.game.quest_track]} Quest", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (156, 78), (935, 50))
            self.Track_round = Button("", "Amita-Regular.ttf", 40, (255, 255, 255), (255, 255, 255), (88, 88), self.dic_track_round[self.game.vote_track])
        
        if self.time > 0 and self.start_count == True:
            if (self.time) % 3 == 1:
                self.Text_time = Button(f"team approval ...", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (484, 124), (577, 367))
                
            elif (self.time) % 3 == 2:
                self.Text_time = Button(f"team approval ..", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (484, 124), (577, 367))
                
            elif (self.time) % 3 == 0:
                self.Text_time = Button(f"team approval .", "Amita-Regular.ttf", 64, (255, 255, 255), (255, 255, 255), (484, 124), (577, 367))
            
            # print(self.time_bar)
            self.time -= 1
            self.circle = self.circle - (360/self.ori_time)
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 806))
            time.sleep(1)
            
        elif self.time == 0 and self.start_count == True:
            self.start_count = False
            self.circle = 270
            self.time = self.ori_time
            self.Text_time1 = Button(f"0", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 806))
            
        elif self.start_count == False:
            self.Text_time1 = Button(f"{self.time}", "Amita-Regular.ttf", 48, (255, 255, 255), (0, 0, 0), (49, 93), (800, 806))
            self.start_count = True
            new_state = Vote_team(self.game)
            new_state.enter_state()
            
            
        # if self.time < 0 and self.start_count == True:
        #     self.start_count = False
        #     self.time = 10
        #     num_people = self.Dectect.count_people()
        #     self.game.num_player = num_people
        #     print(self.game.num_player)
        #     print("Done count")
        #     new_state = Confirm_people_state(self.game)
        #     new_state.enter_state()
        #     self.start_count = True
            
    
            
        
    def render(self, display):
        display.fill((0, 0, 0))        
        
        self.Bg.draw_image(display, 'Avalon_BG.png')
        self.Table.draw_image(display, 'Table.png')
        self.Leader_plate.draw_image(display, "PlayerQuest_plate.png")
        self.Quest_round_plate.draw_image(display, "PlayerQuest_plate.png")
        self.Player_leader.draw_text(display)
        self.Quest_round.draw_text(display)
        self.Time_to_think.draw_text(display)
        self.Describe.draw_text(display)
        self.Text_time.draw_text(display)
        self.Text_time1.draw_text_center(display)
        self.arc.draw_arc(display, -90, self.circle, 50, 4)
        self.think.draw_image(display, "Think.png")
        self.Phase.draw_text(display)
        self.Track_round_plate.draw_image(display, "Track_round_plate.png")
        self.Track_round.draw_image(display, "Track_round.png")
        