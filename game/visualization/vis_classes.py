from pygame import Rect, draw
from ..main import Board, Block

BLOCK_SIZE = 35


class drawingBlock(Block):
    def __init__(self, type="I"):
        super().__init__(type)
        
        self.outer_rect = Rect(self.position[0] * BLOCK_SIZE, self.position[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
        self.inner_rect = self.outer_rect.inflate(10,10)

    def draw(self, surface, color):
        draw.rect(surface, color, self.outer_rect)
        draw.rect(surface, color, self.inner_rect)

class drawingBoard(Board):
    def __init__(self):
        super(drawingBoard, self).__init__()