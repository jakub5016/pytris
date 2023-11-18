from pygame import Rect, draw
from ..main import Board, Block

BLOCK_SIZE = 30
BORDER_WIDHT = 10

class drawingBlock(Block):
    def __init__(self, type="I"):
        super().__init__(type)
        self.create_representation()

    def draw(self, surface, color):
        table_index = 0

        for index, i in enumerate(self.representation):
            for j in range(len(i)):
                if self.drawing_elements[table_index] != None:
                    self.drawing_elements[table_index].x = self.y + j
                    self.drawing_elements[table_index].y = self.x + index

                table_index += 1

        for i in self.drawing_elements:
            if i != None:
                i.ref_pos() # Refresh position
                i.draw(surface, color)

    def create_representation(self):
        self.drawing_elements = []

        for i in range(len(self.representation)):
            for j in range(len(self.representation[0])):
                if self.representation[i][j] :
                    self.drawing_elements.append(drawingElement(i,j,self))

                else:
                    self.drawing_elements.append(None)

    def rotate(self):
        """
        After rotating a bock you change a representation.
        So you MUST create representation once again
        """
        super().rotate()
        self.create_representation()

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

