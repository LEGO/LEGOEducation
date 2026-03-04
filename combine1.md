# LEGO® Education Python API

![LEGO Education logo](./img/LEGOEducation.png)

1. [Introduction and Installation](./README.md)
2. [Connect and Run](./connect.md)
3. [Single Motor](./singlemotor.md)
4. [Double Motor](./doublemotor.md)
5. [Color Sensor](./colorsensor.md)
6. [Controller](./controller.md)
7. **Combine Single Motor and Color Sensor**
8. [Combine Double Motor and Controller](./combine2.md)
9. [Constants](./constants.md)

---
# Combine Single Motor and Color Sensor

You can combine multiple LEGO® Education hardware in one program.  Here is an example of a Single Motor and Color Sensor.

```
import legoeducation as le
import time

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_AZURE
card_serial = '3683'

# Connect to the Single Motor
singlemotor = le.SingleMotor()
singlemotor.connect(card_color=card_color, card_serial=card_serial)

# Connect to the Color Sensor
colorsensor = le.ColorSensor()
colorsensor.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not (singlemotor.connected and colorsensor.connected):
	print('Error connecting to hardware.')
	exit(1) # error connecting

# If color is green, go fast (80%)
# If color is red, go slow (10%)
print('Running for five seconds: green is fast, red is slow.')
for i in range(50):
	if (colorsensor.sensor.color == le.LEGO_COLOR_GREEN):
		singlemotor.motor_run(speed=80)
	elif (colorsensor.sensor.color == le.LEGO_COLOR_RED):
		singlemotor.motor_run(speed=10)
	time.sleep(0.1)
# Done.
singlemotor.motor_stop()

# Disconnect all hardware
singlemotor.disconnect()
colorsensor.disconnect()
exit(0) # successful execution
```

---

**Next:** [Combine Double Motor and Controller](./combine2.md)