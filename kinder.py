#!/usr/bin/env python3

import cmd
import subprocess
import turtle


class Shell(cmd.Cmd):
    prompt = '> '

    def precmd(self, line):
        return line.lower()

    @staticmethod
    def do_say(arg):
        subprocess.call(['say', arg])

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
    def do_triangle(arg):
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)
        turtle.forward(100)
        turtle.left(120)

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
    def do_circle(size):
        try:
            size = int(size)
        except ValueError:
            return False
        turtle.circle(size)

    @staticmethod
    def do_reset(_):
        turtle.reset()

    @staticmethod
    def do_quit(_):
        return True

    do_exit = do_quit


def main():
    Shell().cmdloop()

if __name__ == '__main__':
    main()
