from __future__ import division, print_function
from platform import system as os_name
import turtle

if os_name() == 'Linux':
    import scrollphathd
else:
    # this is just a fake class that does nothing
    # if I am doing dev on something besides Linux
    class scrollphathd(object):
        def __init__(self): pass
        def clear(self): pass
        def set_brightness(self, brightness): pass
        def set_pixel(self, x, y, brightness): pass
        def show(self): pass


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
                scrollphathd.set_pixel(i, j, self.brightness)


if os_name() != 'Linux':
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
			s.tracer(self.c*self.r, 0)
			# print('delay', s.delay())

		def __del__(self):
			self.bye()

		def draw(self, face, row_offset=0):
			# if len(face) > 17:
			# 	raise Exception('LED Face too many rows:', len(face))
			for i in range(self.r):
				for j in range(self.c):
					space = 10
					dia = 7
					self.setpos((j+row_offset)*space, -i*space)
					if face[i][j] == 0:
						self.dot(dia, "gray")
					elif face[i][j] == 1:
						self.dot(dia, "red")
					elif face[i][j] == 2:
						self.dot(dia, "blue")
					else:
						raise Exception('Invalid draw value:', face[i][j])
