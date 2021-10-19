"""
Name: Hannah Rahner
vigenere.py

Problem: Create a program that implements the Vigenere cipher

Certification of Authenticity
I certify that the assignment is entirely my own work.
"""

from graphics import *


def code(message, keyword):
    # format entries
    message = message.upper()
    message = message.replace(' ', '')

    keyword = keyword.replace(' ', '')
    keyword = keyword.upper()

    result = ""

    # encryption
    for i in range(0, len(message)):
        message_letters = ord(message[i]) - 65
        keyword_letters = ord(keyword[i % len(keyword)]) - 65

        encrypted_code = message_letters + keyword_letters
        encrypted_code = (encrypted_code % 26) + 65

        result = result + chr(encrypted_code)
    return (result)


def main():
    # window setup
    win = GraphWin("Vigenere", 400, 500)

    input_message = Text(Point(110, 150), "Message to code: ")
    input_message.draw(win)

    input_keyword = Text(Point(110, 200), "Enter keyword: ")
    input_keyword.draw(win)

    encode = Text(Point(200, 250), "Encode")
    encode.draw(win)

    encode_button = Rectangle(Point(170, 240), Point(230, 260))
    encode_button.draw(win)

    message_code = Entry(Point(260, 150), 25)
    message_code.setFill("gray")
    message_code.draw(win)

    keyword_code = Entry(Point(260, 200), 25)
    keyword_code.setFill("gray")
    keyword_code.draw(win)

    win.getMouse()

    # getting inputs
    entered_message = message_code.getText()
    entered_keyword = keyword_code.getText()

    # outputs
    encode.undraw()
    encode_button.undraw()

    resulting_message = Text(Point(200, 300), "Resulting Message")
    resulting_message.draw(win)

    # call code function
    coded_answer = Text(Point(200, 350), code(entered_message, entered_keyword))
    coded_answer.draw(win)

    closing = Text(Point(200, 450), "Click Anywhere to Close Window")
    closing.setSize(10)
    closing.draw(win)

    win.getMouse()

main()
