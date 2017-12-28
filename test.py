#!/usr/bin/env python

from __future__ import division, print_function
import turtle
import time
import scrollphathd


class LED(object):
    def __init__(self):
        self.r = 17
        self.c = 7
        scrollphathd.set_brightness(0.5)
        self.brightness = 0.5

    def __del__(self):
        pass

    def draw(self, face, row_offset=0):
        for i in range(self.r):
            for j in range(self.c):
                scrollphathd.pixel(i, j, self.brightness)

class LEDTurtle(turtle.Turtle):
    """
    Simulate a pimoroni LED hat 17x7
    """
    def __init__(self):
        self.r = 17
        self.c = 7

        turtle.Turtle.__init__(self)
        self.penup()
        self.speed(0)
        self.hideturtle()

        s = self.getscreen()
        s.tracer(self.c*self.r,0)
        # print('delay', s.delay())

    def __del__(self):
        self.bye()

    def draw(self, face, row_offset=0):
        for i in range(self.r):
            for j in range(self.c):
                space = 10
                dia = 7
                self.setpos((j+row_offset)*space, -i*space)
                if face[i][j] == 0:
                    self.dot(dia, "gray")
                else:
                    self.dot(dia, "blue")

class Eye(object):
    def __init__(self, leds, dims):
        self.led = leds
        self.dims = dims

    def look(self, loc):
        r, c = loc

        # double check bounds
        # loc[0] => row
        # loc[1] => col
        if 0 > r:
            r = 0
        elif r > 6:
            r = 6

        if 0 > c:
            c = 0
        elif c > 16:
            c = 16

        self.led.draw()

class Mouth(object):
    def __init__(self, leds):
        self.led = leds

    def letter(self, ltr):
        self.led.draw(self.letters(ltr), row_offset=10)


class LEDFace(object):
    def __init__(self, drawClass):
        self.led = drawClass.__init__(self)
        self.eyeLim = 10  # eye goes 0-9, offset to start mouth

    def __del__(self):
        pass

    def talk(self, msg):
        for ltr in msg:
            self.mouth.letter(ltr)


faces = [
    [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,0,1,0,0],
        [0,0,1,0,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,1,1,1,1,1,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ],
    [
        [0,0,0,0,0,0,0],
        [0,0,1,1,1,0,0],
        [0,0,1,0,1,0,0],
        [0,0,1,0,1,0,0],
        [0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [1,1,1,1,1,1,1],
        [1,0,0,0,0,0,1],
        [0,1,0,0,0,1,0],
        [0,1,0,0,0,1,0],
        [0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0]
    ]
]

led = LED()

for _ in range(3):
    for f in faces:
        led.draw(f)
        time.sleep(0.25)
time.sleep(1)
