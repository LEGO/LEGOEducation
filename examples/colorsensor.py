# Color Sensor Example
import legoeducation as le
import time

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_AZURE
card_serial = '3683'

# Connect to the Color Sensor
colorsensor = le.ColorSensor()
colorsensor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not colorsensor.connected:
	print('Error connecting to Color Sensor.')
	exit(1) # error connecting

# Example:
# - for five seconds: stream RGB values
# - look at RGB values and print "Red" if color is red
print('looking for colors:')
for i in range(50):
	# stream 
	R = colorsensor.sensor.rawRed
	G = colorsensor.sensor.rawGreen
	B = colorsensor.sensor.rawBlue
	print(f'RGB: {(R, G, B)}')
	if (R > 128 and G < 128 and B < 128):
		print('> RED!')
	time.sleep(0.1)

# Disconnect
colorsensor.disconnect()
exit(0) # successful execution