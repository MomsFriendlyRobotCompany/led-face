from __future__ import division, print_function
from platform import system as os_name

if os_name() == 'Linux':
    import scrollphathd
else:
    class scrollphathd(object):
        pass


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
