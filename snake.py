from turtle import Turtle

START_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.shape = 'square'
        self.color = 'white'
        self.parts = []
        for pos in START_POS:
            part = Turtle(shape=self.shape)
            part.penup()
            part.color(self.color)
            part.setposition(pos)
            self.parts.append(part)
        self.head = self.parts[0]

    def move(self):
        for part_num in range(len(self.parts) - 1, 0, -1):
            coordinates = self.parts[part_num - 1].position()
            self.parts[part_num].setposition(coordinates)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
