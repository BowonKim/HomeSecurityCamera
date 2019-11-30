import picamera
import time
import datetime

with picamera.Picamera() as camera:
     now = datetime.datetime.now()
     filename = now.strftime('%m%d%H')   # used time when the video was taken as the name of the file
     camera.start_preview()
     camera.stop_preview()
     camera.capture(filename + '.jpg')
