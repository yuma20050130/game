import pyxel
import random

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class App:
   
    def __init__(self):
        pyxel.init(128,128)

        pyxel.load("game_resource.pyxres")

        self.player = Player(8, 112)

        self.game_end = False

 
    def run(self):
        pyxel.run(self.update, self.draw)

    def check_hit(self,player):
        dx = player.x
        dy = player.y
        if 16 <= dx <= 32 and 0 <= dy <= 16:
            return True
        elif 32 <= dx <= 48 and 32 <= dy <= 48:
            return True
        elif 80 <= dx <= 96 and 32 <= dy <= 48:
            return True
        elif 80 <= dx <= 96 and 64 <= dy <= 80:
            return True
        elif 48 <= dx <= 64 and 0 <= dy <= 16:
            return True
        elif 96 <= dx <= 112 and 0 <= dy <= 16:
            return True
        elif 0 <= dx <= 16 and 48 <= dy <= 64:
            return True
        elif 32 <= dx <= 48 and 80 <= dy <= 96:
            return True
        elif 96 <= dx <= 112 and 96 <= dy <= 112:
            return True
        elif 48 <= dx <= 64 and 48 <= dy <= 64:
            return True
        elif 64 <= dx <= 80 and 96 <= dy <= 112:
            return True
        else:
            return False
        
    def check_goal(self,player):
        dx = player.x
        dy = player.y
        if 80 < dx < 96 and -8 < dy < 8:
            return True
        else:
            return False

    def update(self):
        if not self.game_end:
            energy=[6,12,24,30]
            move=random.choice(energy)
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.player.x -= move
            elif pyxel.btnp(pyxel.KEY_RIGHT):
                self.player.x += move
            elif pyxel.btnp(pyxel.KEY_UP):
                self.player.y -= move
            elif pyxel.btnp(pyxel.KEY_DOWN):
                self.player.y += move
       


    def draw(self):
        pyxel.cls(0)

        pyxel.bltm(0, 0, 0, 0, 0, 128, 128, 0)

        pyxel.blt(self.player.x, self.player.y, 0, 0, 0, 16, 16, 0)

        if self.check_goal(self.player):
            pyxel.rect(0, 0, 128, 16, 10)
            
            pyxel.text(40, 5, "GAME CLEAR!!", 11)
            
            self.game_end = True

        if self.check_hit(self.player):
            pyxel.rect(0, 0, 128, 16, 5)
            
            pyxel.text(40, 5, "GAME OVER...", 13)
            
            self.game_end = True
        
            

App().run()
