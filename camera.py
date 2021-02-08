from picamera import Picamera
from time import sleep


camera = Picamera()
camera.resolution = (2592, 1944)
i = 0
for i in range(4):
	camera.capture(f'image{i:3d}')
	sleep(60)



