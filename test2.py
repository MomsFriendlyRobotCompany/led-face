#!/usr/bin/env python

from __future__ import division, print_function
import time
import random
from subprocess import call
from multiprocessing import Process
from linuxLED import LEDTurtle


def say(msg):
	call(msg, shell=True)


class TTS(object):
	"""
	Apple - say
	"""

	def __init__(self, tts=None):
		"""
		You can pass in a specific tts program or let it search for one to
		use. It searches for: say, espeak, spd-say. If no program is found, it uses
		echo to print text to the command line
		"""
		found = False
		if not tts:
			for cmd in ['espeak', 'spd-say', 'say']:
				if call(['which -s {}'.format(cmd)], shell=True) == 0:
					self.tts = [cmd]
					# self.tts = cmd
					found = True
					break
			if not found:
				print('could not find a tts program, using echo instead')
				self.tts = 'echo'
		else:
			self.tts = tts

	def setOptions(self, options):
		"""
		Change the default options
		"""
		self.tts.append(options)

	def say(self, txt):
		"""
		Speak the text passed to this function. If no tts was found, then this
		will print the text instead.
		"""
		c = self.tts[:]  # make a copy
		c.append(txt)
		c = ' '.join(c)
		# call(' '.join(c), shell=True)
		p = Process(target=say, args=(c,))
		p.start()
		# p.join()



# class LEDTurtle(turtle.Turtle):
# 	"""
# 	Simulate a pimoroni LED hat 17x7
# 	"""
# 	def __init__(self):
# 		self.r = 17
# 		self.c = 7
#
# 		turtle.Turtle.__init__(self)
# 		self.penup()
# 		self.speed(0)
# 		self.hideturtle()
#
# 		s = self.getscreen()
# 		s.tracer(self.c*self.r, 0)
# 		# print('delay', s.delay())
#
# 	def __del__(self):
# 		self.bye()
#
# 	def draw(self, face, row_offset=0):
# 		# if len(face) > 17:
# 		# 	raise Exception('LED Face too many rows:', len(face))
# 		for i in range(self.r):
# 			for j in range(self.c):
# 				space = 10
# 				dia = 7
# 				self.setpos((j+row_offset)*space, -i*space)
# 				if face[i][j] == 0:
# 					self.dot(dia, "gray")
# 				elif face[i][j] == 1:
# 					self.dot(dia, "red")
# 				elif face[i][j] == 2:
# 					self.dot(dia, "blue")
# 				else:
# 					raise Exception('Invalid draw value:', face[i][j])



	# eyes = {
	#     'normal': [[0,0,2,0,2,0,0]],
	#     'left': [[0,2,0,2,0,0,0]],
	#     'right': [[0,0,0,2,0,2,0]],
	#     'big': [
	#         [0,2,2,0,2,2,0],
	#         [0,2,2,0,2,2,0]
	#     ]
	# }



class Eyes(object):
	eyes = {
		'normal': [[0,0,2,0,2,0,0]], #  . .
		'left': [[0,2,0,2,0,0,0]],  # . .
		'right': [[0,0,0,2,0,2,0]], #    . .
		'mad': [ # \ /
			[0,2,0,0,0,2,0],
			[0,0,2,0,2,0,0]
		],
		'sad': [ # / \
			[0,0,2,0,2,0,0],
			[0,2,0,0,0,2,0]
		],
		'happy': [ # > <
			[0,2,0,0,0,2,0],
			[0,0,2,0,2,0,0],
			[0,2,0,0,0,2,0]
		],
		'dead': [ # x x
			[2,0,2,0,2,0,2],
			[0,2,0,0,0,2,0],
			[2,0,2,0,2,0,2]
		],
		'surprise': [ # o o
			[0,2,2,0,2,2,0],
			[0,2,2,0,2,2,0]
		]
	}
	def __init__(self):
		# self.led = leds
		# self.dims = dims
		pass

	def look(self, loc):
		if loc not in self.eyes:
			raise Exception('Invalide eyes value:', loc)
		return self.eyes[loc]


class Mouth(object):
	letters = {
		'a': [ # 7x6
			[0,2,2,2,2,2,0],
			[0,2,2,2,2,2,0],
			[0,2,2,2,2,2,0],  # set value to brightness?
			[0,2,1,1,1,2,0],
			[0,0,2,2,2,0,0]
		],
		'e': [ # 7x5
			[0,2,2,2,2,2,0],
			[0,2,2,2,2,2,0],
			[0,2,1,1,1,2,0],  # set value to brightness?
			[0,0,2,2,2,0,0]
		],
		'o': [ # 7x4
			[0,0,0,2,2,0,0],
			[0,0,2,2,2,2,0],
			[0,0,2,2,2,2,0],
			[0,0,0,2,2,0,0],
		],
		'uq': [ # 7x2
			[0,0,2,2,0,0,0],
			[0,0,2,2,0,0,0],
		],
		'wr': [
			[0,0,0,2,2,0,0],
			[0,0,2,2,2,2,0],
			[0,0,2,1,1,2,0],
			[0,0,0,2,2,0,0],
		],
		'ts': [ # 7x3
			[2,2,2,2,2,2,2],
			[0,2,0,0,0,2,0],
			[0,0,2,2,2,0,0]
		],
		'ln': [ # 7x5
			[2,0,0,0,0,0,2],
			[0,2,2,2,2,2,0],
			[0,2,2,1,1,2,0],
			[0,2,1,1,2,2,0],  # set value to brightness?
			[0,0,2,2,2,0,0]
		],
		'mbp': [ # 7x1
			[0,2,2,2,2,2,0]
		],
		'fv': [
			[0,2,2,2,2,2,0],
			[0,0,2,0,2,0,0]
		],
		'nothing': [ # 7x1
			[0,2,2,2,2,2,0]
		],
		'other': [ # 7x5
			[0,0,0,0,0,0,0],
			[0,0,2,2,2,0,0],
			[0,2,2,2,2,2,0],  # set value to brightness?
			[0,0,2,2,2,0,0]
		],

	}
	def __init__(self):
		pass

	def letter(self, ltr):
		ltr = ltr.lower()
		if ltr == 'a': ltr = self.letters['a']
		elif ltr == 'o': ltr = self.letters['o']
		elif ltr == 'e': ltr = self.letters['e']
		elif ltr == 'w' or ltr == 'r': ltr = self.letters['wr']
		elif ltr == 't' or ltr == 's': ltr = self.letters['ts']
		elif ltr == 'l' or ltr == 'n': ltr = self.letters['ln']
		elif ltr == 'u' or ltr == 'q': ltr = self.letters['uq']
		elif ltr == 'm' or ltr == 'b' or ltr == 'p': ltr = self.letters['mbp']
		elif ltr == 'f' or ltr == 'v': ltr = self.letters['fv']
		elif 97 <= ord(ltr) <= 122: ltr = self.letters['other']
		else: ltr = self.letters['nothing']

		m = ltr + [[0]*7 for i in range(7-len(ltr))]

		# self.led.draw(ltr, row_offset=10)
		return m


class LEDFace(object):
	# value?
	look_size = {
		'forward': 4,
		'up': 0,
		'down': 9
	}
	nose = [[0]*7]

	def __init__(self, drawClass):
		# self.led = drawClass.__init__(self)
		self.led = drawClass()
		self.eyeLim = 10  # eye goes 0-9, offset to start mouth
		self.mouth = Mouth()
		self.eye = Eyes()
		self.look('forward')
		self.tts = TTS()

		# print('forehead', self.forehead)
		# print('nose', self.nose)

	def look(self, where):
		self.forehead = [[0]*7 for i in range(self.look_size[where])]

	def __del__(self):
		pass

	def talk(self, msg):
		self.look('forward')
		eye_type = 'normal'
		self.tts.say(msg)
		for ltr in msg:
			if ltr == ' ':
				where = random.choice(self.look_size.keys())
				print(where)
				self.look(where)

				eye_type = random.choice(self.eye.eyes.keys())
				print('eye_type:', eye_type)

			print(ltr)
			m = self.mouth.letter(ltr)
			e = self.eye.look(eye_type)
			face = self.forehead+e+self.nose+m
			zeros = [[0]*7 for i in range(17-len(face))]
			self.led.draw(face + zeros)
			# time.sleep(.001)

	def draw(self, pic):
		self.led.draw(pic)


led = LEDFace(LEDTurtle)
led.talk('hi how are you! This is a test')
time.sleep(1)
