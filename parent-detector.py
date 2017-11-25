from gpiozero import MotionSensor

pir = MotionSensor(6)
pir.wait_for_motion()
print("Motion detected!")