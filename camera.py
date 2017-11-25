from picamera import PiCamera
from time import sleep

# Initialize camera
camera = PiCamera()

# Change the rotation, this applies only if the camera is upside down
camera.rotation = 180

camera.resolution = (500, 500)

# Use the camera
camera.start_preview()

for i in range(5):
    # Wait
    sleep(5)
    # Take a picture
    camera.capture('/home/pi/Desktop/image%s.jpg' % i)

# Kill the camera
camera.stop_preview()
