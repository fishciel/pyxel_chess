import pyxel

class App:
    WIDTH = 160
    HEIGHT = 120
    def __init__(self):
        #specify window size with init
        pyxel.init(App.WIDTH, App.HEIGHT, title="Verse")
        pyxel.run(self.update, self.draw)

    '''update frame process 30 fps'''
    def update(self):
        #esc = quit game
        if pyxel.btnp(pyxel.KEY_ESCAPE):
            pyxel.quit()

    def draw(self):
        '''think of as layers'''
        #fill screen(color)
        pyxel.cls(1)
        #x, y, w, h, color,  
        # pos 0 is upper left corner, rightmost is 159, bottom Y is 119
        # chess board parameters
        square_size = 15  # Size of each chess square
        board_size = 8    # 8x8 chess board
        start_x = (App.WIDTH - (square_size * board_size)) // 2  # Center the board horizontally
        start_y = (App.HEIGHT - (square_size * board_size)) // 2  # Center the board vertically
        
        for row in range(board_size):
            for col in range(board_size):
                # if (row + col) is even, draw a light square, otherwise dark
                color = 7 if (row + col) % 2 == 0 else 5  # 7 is white, 5 is dark color
                x = start_x + (col * square_size)
                y = start_y + (row * square_size)
                pyxel.rect(x, y, square_size, square_size, color)
        #x, y, text, color
        pyxel.text(70, 60, "Start", pyxel.COLOR_YELLOW)

App()