# LEGO® Education Python API

![LEGO Education logo](./img/LEGOEducation.png)

1. [Introduction and Installation](./README.md)
2. [Connect and Run](./connect.md)
3. [Single Motor](./singlemotor.md)
4. [Double Motor](./doublemotor.md)
5. [Color Sensor](./colorsensor.md)
6. [Controller](./controller.md)
7. [Combine Single Motor and Color Sensor](./combine1.md)
8. **Combine Double Motor and Controller**
9. [Constants](./constants.md)

---
# Combine Double Motor and Controller

You can combine multiple LEGO® Education hardware in one program.  Here is an example of a Double Motor and Controller.

```python
import legoeducation as le
import time

# update these values to match the Connection Card
card_color = le.LEGO_COLOR_AZURE
card_serial = '3683'

# Connect to the Double Motor
doublemotor = le.DoubleMotor()
doublemotor.connect(card_color=card_color, card_serial=card_serial)

# Connect to the Controller
controller = le.Controller()
controller.connect(card_color=card_color, card_serial=card_serial)

# Check connection
if not (doublemotor.connected and controller.connected):
	print('Error connecting to hardware.')
	exit(1) # error connecting

# Control left-and-right motors (tank movement) based on left-and-right levers
print('Running for five seconds: levers control motors.')
for i in range(50):
	speed_left = controller.sensor.leftPercent
	speed_right = controller.sensor.rightPercent
	doublemotor.movement_move_tank(speed_left=speed_left, speed_right=speed_right)
	time.sleep(0.1)

# Disconnect all hardware
doublemotor.disconnect()
controller.disconnect()
exit(0) # successful execution
```

---

**Next:** [Constants](./constants.md)