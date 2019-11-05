#!/usr/bin/env python3

import cmd
import subprocess
import turtle


class Shell(cmd.Cmd):
    prompt = '> '

    def preloop(self):
        turtle.shape('turtle')
        turtle.width(3)

    def precmd(self, line):
        return line.lower()

    @staticmethod
    def do_draw(_):
        turtle.shape('turtle')
        turtle.width(3)

    @staticmethod
    def do_pen(arg):
        if arg == 'up':
            turtle.penup()
        elif arg == 'down':
            turtle.pendown()

    @staticmethod
    def do_go(dist):
        try:
            dist = int(dist)
        except ValueError:
            dist = 0
        turtle.forward(dist)

    @staticmethod
    def do_pencolor(color):
        turtle.pencolor(color)

    @staticmethod
    def do_left(degrees):
        try:
            degrees = int(degrees)
        except ValueError:
            degrees = 0
        turtle.left(degrees)

    @staticmethod
    def do_right(degrees):
        try:
            degrees = int(degrees)
        except ValueError:
            degrees = 0
        turtle.right(degrees)

    @staticmethod
    def do_triangle(size):
        size = int(size)
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)
        turtle.forward(size)
        turtle.left(120)

    @staticmethod
    def do_circle(size):
        try:
            size = int(size)
        except ValueError:
            return False
        turtle.circle(size)

    @staticmethod
    def do_reset(_):
        turtle.reset()
        turtle.width(3)

    @staticmethod
    def do_home(_):
        turtle.home()

    @staticmethod
    def do_quit(_):
        return True

    do_exit = do_quit


def main():
    Shell().cmdloop()

if __name__ == '__main__':
    main()
