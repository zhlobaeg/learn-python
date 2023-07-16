class Skin():
    def __init__(self):
        self.player_color = (0, 255, 0)
        self.bomb_color = (127, 127, 127)
        self.bomb_blast_color = (255, 102, 102)
        self.brick_color = (200, 200, 200)
        self.background_color = (0, 0, 0)
        self.name = '1'
        

skin_1 = Skin()

skin_2 = Skin()

skin_2.background_color = (0, 51, 51)
skin_2.bomb_color = (0, 180, 185)
skin_2.brick_color = (218, 149, 81)
skin_2.player_color = (115, 255, 190)
skin_2.name = '2'

skin_3 = Skin()

skin_3.background_color = (50, 45, 45)
skin_3.bomb_color = (55, 200, 135)
skin_3.brick_color = (115, 160, 30)
skin_3.player_color = (230, 230, 55)
skin_3.name = '3'