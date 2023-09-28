from pygame import Rect, draw
from ..main import Board, Block

BLOCK_SIZE = 35
BORDER_WIDHT = 10

class drawingBlock(Block):
    def __init__(self, type="I"):
        super().__init__(type)
        self.drawing_elements = []
        
        for i in range(len(self.representation)):
            for j in range(len(self.representation[0])):
                self.drawing_elements.append(drawingElement(i,j,self))


    def draw(self, surface, color):
        for i in self.drawing_elements:
            i.draw(surface, color)
            pass

class drawingElement():
    def __init__(self, x=0, y =0, block = Block()):
        
        self.outer_rect = Rect((block.x + x) * BLOCK_SIZE, 
                               (block.y + y) * BLOCK_SIZE, 
                               BLOCK_SIZE, BLOCK_SIZE)
        
        self.inner_rect = Rect((block.x + x) * BLOCK_SIZE + BORDER_WIDHT/2, 
                               (block.y + y) * BLOCK_SIZE + BORDER_WIDHT/2, 
                               BLOCK_SIZE-BORDER_WIDHT, BLOCK_SIZE-BORDER_WIDHT)

    def draw(self, surface, color):
        draw.rect(surface, (0,0,0), self.outer_rect)
        draw.rect(surface, color, self.inner_rect)

class drawingBoard(Board):
    def __init__(self):
        super(drawingBoard, self).__init__()