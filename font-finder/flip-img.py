import os
import sys 
import time 
from PIL import Image

class Listener():
    def __init__(self, filename, handler):
        self._cached_stamp = 0
        self.filename = filename
        self.handler = handler

    def check(self):
        stamp = os.stat(self.filename).st_mtime
        if stamp != self._cached_stamp:
            print("File changed, reloading")
            self._cached_stamp = stamp
            self.handler()

    def run ( self ) :
        while True:
            self.check()
            time.sleep(0.1)

def run () :
    im = Image.open('./letter.png')
    angle = 180
    out = im.rotate(angle)
    out.save('./letter-rotate.png')

listen = Listener(
    './letter.png',
    run
) 

listen.run()
