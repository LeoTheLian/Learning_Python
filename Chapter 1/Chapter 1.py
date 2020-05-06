import turtle


def main():
    filename = input("Please enter drawing filename: ")
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, "r")  # r for reading, w for writing, a for appending
    for line in file:
        text = line.strip()  # cleans up the newline character and any blanks in the beginning and end of the line
        commandList = text.split(",")  # split the line by the given character
        command = commandList[0]
        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width(width)
            t.pencolor(color)
            t.goto(x, y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width(width)
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print("Unknown command found in the file:", command)
    file.close()
    t.ht()  # hide the turtle
    screen.exitonclick()  # Hold the turtle graphics window open until the mouse is clicked
    print("Program Execution Completed")


if __name__ == "__main__":
    main()
