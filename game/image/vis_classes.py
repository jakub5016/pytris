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
        index = 0
        for i in range(len(self.representation)):
            for j in range(len(self.representation[0])):
                self.drawing_elements[index].x = self.y + j
                self.drawing_elements[index].y = self.x + i

                index += 1

        for i in self.drawing_elements:
            i.ref_pos() # Refresh position
            i.draw(surface, color)
            pass


class drawingElement():
    def __init__(self, x=0, y =0, block = Block()):
        
        self.x = block.x + x
        self.y = block.y + y
        
        self.outer_rect = Rect(self.x * BLOCK_SIZE, 
                               self.y * BLOCK_SIZE, 
                               BLOCK_SIZE, BLOCK_SIZE)
        
        self.inner_rect = Rect(self.x * BLOCK_SIZE + BORDER_WIDHT/2, 
                               self.y * BLOCK_SIZE + BORDER_WIDHT/2, 
                               BLOCK_SIZE-BORDER_WIDHT, BLOCK_SIZE-BORDER_WIDHT)

    def draw(self, surface, color):
        draw.rect(surface, (0,0,0), self.outer_rect)
        draw.rect(surface, color, self.inner_rect)

    def ref_pos(self):
        self.outer_rect = Rect(self.x * BLOCK_SIZE, 
                               self.y * BLOCK_SIZE, 
                               BLOCK_SIZE, BLOCK_SIZE)
        
        self.inner_rect = Rect(self.x * BLOCK_SIZE + BORDER_WIDHT/2, 
                               self.y * BLOCK_SIZE + BORDER_WIDHT/2, 
                               BLOCK_SIZE-BORDER_WIDHT, BLOCK_SIZE-BORDER_WIDHT)

class drawingBoard(Board):
    def __init__(self):
        super(drawingBoard, self).__init__()

