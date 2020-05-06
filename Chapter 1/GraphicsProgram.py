import turtle
import tkinter
import tkinter.colorchooser
import tkinter.filedialog


class GoToCommand:

    def __init__(self, x, y, width=1, color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x, self.y)

    def __str__(self):
        return "goto\n" + str(self.x) + "\n" + str(self.y) + "\n" + str(self.width) + "\n" + self.color


class CircleCommand:
    def __init__(self, radius, width=1, color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self, turtle):
        turtle.width = self.width
        turtle.pencolor = self.color
        turtle.circle(self.radius)

    def __str__(self):
        return "circle\n" + str(self.radius) + "\n" + str(self.width) + "\n" + self.color


class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self, turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

    def __str__(self):
        return "beginfill\n" + self.color


class EndFillCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.end_fill()

    def __str__(self):
        return "endfill"


class PenUpCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.penup()

    def __str__(self):
        return "penup"


class PenDownCommand:
    def __init__(self):
        pass

    def draw(self, turtle):
        turtle.pendown()

    def __str__(self):
        return "pendown"


class PyList:
    def __init__(self):
        self.gcList = []

    def append(self, item):
        self.gcList = self.gcList + [item]

    def removeLast(self):
        self.gcList = self.gcList[:-1]

    def __iter__(self):
        for c in self.gcList:
            yield c

    def __len__(self):
        return len(self.gcList)


class DrawingApplication(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.pack()
        self.buildWindow()
        self.graphicsCommands = PyList()

    def main():
        filename = input("Please enter drawing filename: ")
        t = turtle.Turtle()
        screen = t.getscreen()
        file = open(filename, "r")
        graphicsCommands = PyList()
        command = file.readline.strip()
        while command != "":
            if command == "goto":
                x = float(file.readline())
                y = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                cmd = GoToCommand(x, y, width, color)
            elif command == "circle":
                radius = float(file.readline())
                width = float(file.readline())
                color = file.readline().strip()
                cmd = CircleCommand(radius, width, color)
            elif command == "beginfill":
                color = file.readline().strip()
                cmd = BeginFillCommand(color)
            elif command == "endfill":
                cmd = EndFillCommand()
            elif command == "penup":
                cmd = PenUpCommand()
            elif command == "pendown":
                cmd = PenDownCommand()
            else:
                raise RuntimeError("Unknown Command: " + command)
            graphicsCommands.append(cmd)
            command = file.readline().strip()

        for cmd in graphicsCommands:
            cmd.draw(t)

        file.close()
        t.ht()
        screen.exitonclick()
        print("Program Execution Completed")

    if __name__ == "__main__":
        main()