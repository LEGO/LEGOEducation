# Controller Example
import legoeducation as le
import time

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_AZURE
card_serial = '3683'

# Connect to the Controller
controller = le.Controller()
controller.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not controller.connected:
	print('Error connecting to Controller.')
	exit(1) # error connecting

# Example:
# - reaction game: which Controller lever went above 90% first?
print('Push one of the Controller levers forward.')
for i in range(50):
	if (controller.sensor.leftPercent > 90 or controller.sensor.rightPercent > 90):
		if (controller.sensor.leftPercent > 90):
			print('- Left first!')
			break
		else:
			print('- Right first!')
			break
	time.sleep(0.1)
else:
	print('Neither lever was pushed...')

# Disconnect
controller.disconnect()
exit(0) # successful execution