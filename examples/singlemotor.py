# Single Motor Example
import legoeducation as le
import time

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_AZURE
card_serial = '3683'

# Connect to the Single Motor
singlemotor = le.SingleMotor()
singlemotor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not singlemotor.connected:
	print('Error connecting to Single Motor.')
	exit(1) # error connecting

# Example:
# - Reset single motor relative position (to 0)
# - Start running single motor slow (speed 20%)
# - Check single motor position for 5 seconds
# - If single motor position is greater than 360, fun fast (speed 80%)

singlemotor.motor_reset_relative_position()

singlemotor.motor_run(speed=20)

for i in range(50):
	print(f'Current position: {singlemotor.motor.position}')
	if (singlemotor.motor.position > 360):
		singlemotor.motor_run(speed=80)
	time.sleep(0.1) # 1/10th of a second
	
singlemotor.motor_stop()

# Disconnect
singlemotor.disconnect()
exit(0) # successful execution