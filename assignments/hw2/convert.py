from graphics import *

def main():
    print("Press enter to close")
    win = GraphWin("Celsius Converter", 500, 500)
    win.setCoords(0, 0, 10, 10)

    # input
    celsius_temp_text = Text(Point(3,9), "Celsius Temperature:")
    celsius_temp_text.draw(win)

    # input
    convert_text = Text(Point(5,5), "Convert It!")
    button_outline = Rectangle(Point(3,6), Point(7,4))
    convert_text.draw(win)
    button_outline.draw(win)

    fahrenheit_temp_text = Text(Point(3,1), "Fahrenheit Temperature")
    fahrenheit_temp_text.draw(win)

    output_text = Text(Point(7,1), "")
    output_text.draw(win)

    win.getMouse()

    celsius_temp = eval(user_input.getText())

    fahrenheit_temp = (9/5) * celsius_temp + 32

    output_text.setText(fahrenheit_temp)