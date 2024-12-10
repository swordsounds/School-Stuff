import turtle

class Polygon:
    def __init__(self, sides, name, size=10, color="red", line=10):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line
        self.interior_angles = (self.sides - 2 ) * 180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        
        
class Square(Polygon):
    def __init__(self,size=10, color="red", line=10):
        super().__init__(4, "Square", size, color, line) 

        self.size = size
        self.color = color
        self.line = line

    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square(size=10, color="blue", line=1)
print(square.name, square.sides, square.size)


square.draw()


turtle.done()