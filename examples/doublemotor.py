# Double Motor Example
import legoeducation as le
import time

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_AZURE
card_serial = '3683'

# Connect to the Double Motor
doublemotor = le.DoubleMotor()
doublemotor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not doublemotor.connected:
	print('Error connecting to Double Motor.')
	exit(1) # error connecting

# Example:
# - go forward
# - turn 90-degrees
# - repeat that 4 times (a square)
for i in range(4):
	doublemotor.movement_move_for_time(1000, speed=30)
	doublemotor.movement_turn_for_degrees(90)
doublemotor.movement_stop()

# Disconnect
doublemotor.disconnect()
exit(0) # successful execution