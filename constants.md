# LEGO® Education Python API

![LEGO Education logo](./img/LEGOEducation.png)

1. [Introduction and Installation](./README.md)
2. [Connect and Run](./connect.md)
3. [Single Motor](./singlemotor.md)
4. [Double Motor](./doublemotor.md)
5. [Color Sensor](./colorsensor.md)
6. [Controller](./controller.md)
7. [Combine Single Motor and Color Sensor](./combine1.md)
8. [Combine Double Motor and Controller](./combine2.md)
9. **Constants**

---
# Constants

When the LEGO® Education Python API is imported into your Python code with `import legoeducation as le`, then the `le` alias can be used to access all of the following constants (e.g. `le.LEGO_COLOR_NOCOLOR`).

## LEGO Color

The LEGO Color constants are used in a variety of ways (Connection Card colors, Color Sensor detected colors, etc). Note that not all LEGO Color constants are available in each context.

```
LEGO_COLOR_NOCOLOR
LEGO_COLOR_RED
LEGO_COLOR_YELLOW
LEGO_COLOR_BLUE
LEGO_COLOR_TEAL
LEGO_COLOR_GREEN
LEGO_COLOR_PURPLE
LEGO_COLOR_WHITE
LEGO_COLOR_MAGENTA
LEGO_COLOR_ORANGE
LEGO_COLOR_AZURE
```

## Motor End State (Single and Double Motors)

For use in `motor_set_end_state` and `movement_set_end_state` functions.

```
MOTOR_END_STATE_DEFAULT
MOTOR_END_STATE_COAST
MOTOR_END_STATE_BRAKE
MOTOR_END_STATE_HOLD
MOTOR_END_STATE_CONTINUE
MOTOR_END_STATE_SMART_COAST
MOTOR_END_STATE_SMART_BRAKE
```

## Motor Move Direction (Single and Double Motors)

For use in `motor_run`, `motor_run_for_time`, `motor_run_for_degrees`, and `motor_run_to_absolute_position` functions.

```
MOTOR_MOVE_DIRECTION_CLOCKWISE
MOTOR_MOVE_DIRECTION_COUNTERCLOCKWISE
MOTOR_MOVE_DIRECTION_SHORTEST
MOTOR_MOVE_DIRECTION_LONGEST
```

## Motor State (Single and Double Motors)

For use with `motorState` (via `MotorNotification`).

```
MOTOR_STATE_READY
MOTOR_STATE_RUNNING
MOTOR_STATE_STALLED
MOTOR_STATE_CMD_ABORTED
MOTOR_STATE_REGULATION_ERROR
MOTOR_STATE_MOTOR_DISCONNECTED
MOTOR_STATE_HOLDING
MOTOR_STATE_DC_RUNNING
MOTOR_STATE_NOT_ALLOWED_TO_RUN
```

## Motor Gesture (Single and Double Motors)

For use with `gesture` (via `MotorNotification`).

```
MOTOR_GESTURE_NO_GESTURE
MOTOR_GESTURE_SLOW_CLOCKWISE
MOTOR_GESTURE_FAST_CLOCKWISE
MOTOR_GESTURE_SLOW_COUNTERCLOCKWISE
MOTOR_GESTURE_FAST_COUNTERCLOCKWISE
MOTOR_GESTURE_WIGGLED
```

## Motor Sides (Double Motor)

When specifying motor in `done`, `motor_set_speed`, `motor_run`, `motor_run_for_time`, `motor_run_for_degrees`, `motor_reset_relative_position`, `motor_run_to_relative_position`, `motor_run_to_absolute_position`, `motor_set_duty_cycle`, `motor_stop`, `motor_set_end_state`, and `motor_set_acceleration` functions.

```
MOTOR_LEFT
MOTOR_RIGHT
MOTOR_BOTH
```

## Motor Bits (Double Motor)

For use with `motorBitMask` (via `MotorNotification`).

```
MOTOR_BITS_LEFT
MOTOR_BITS_RIGHT
```

## Movement Direction (Double Motor)

For use in `movement_move` and `movement_move_for_time` functions.

```
MOVEMENT_DIRECTION_FORWARD
MOVEMENT_DIRECTION_BACKWARD
MOVEMENT_DIRECTION_LEFT
MOVEMENT_DIRECTION_RIGHT
```

## Movement Move Direction (Double Motor)

For use in `movement_move_for_degrees` function.

```
MOVEMENT_MOVE_DIRECTION_FORWARD
MOVEMENT_MOVE_DIRECTION_BACKWARD
```

## Movement Turn Direction (Double Motor)

For use in `movement_turn_for_degrees` function.

```
MOVEMENT_TURN_DIRECTION_LEFT
MOVEMENT_TURN_DIRECTION_RIGHT
```

## Device Face (Double Motor)

For use in `imu_set_yaw_face` function and with `orientation` and `yawFace` (via `ImuDeviceNotification`).

```
DEVICE_FACE_TOP
DEVICE_FACE_FRONT
DEVICE_FACE_RIGHT
DEVICE_FACE_BOTTOM
DEVICE_FACE_BACK
DEVICE_FACE_LEFT
```

## Motion Gesture (IMU in Double Motor)

For use with `gesture` (via `ImuGestureNotification`).

```
MOTION_GESTURE_NO_GESTURE
MOTION_GESTURE_TAPPED
MOTION_GESTURE_DOUBLE_TAPPED
MOTION_GESTURE_COLLISION
MOTION_GESTURE_SHAKE
MOTION_GESTURE_FREEFALL
```

## Light Pattern (Button on Hardware)

For use with `light_color` function.

```
LIGHT_PATTERN_SOLID
LIGHT_PATTERN_BREATHE
LIGHT_PATTERN_PULSE
LIGHT_PATTERN_SHORT_BLINK
LIGHT_PATTERN_LONG_BLINK
LIGHT_PATTERN_DOUBLE_BLINK
```

## Button State (Button on Hardware)

For use with `state` (via `ButtonStateNotification`).

```
BUTTON_STATE_RELEASED
BUTTON_STATE_PRESSED
```

## Sound Pattern (Hardware Beep)

For use with `beep` function.

```
SOUND_PATTERN_BEEP_SINGLE
SOUND_PATTERN_BEEP_DOUBLE
SOUND_PATTERN_BEEP_TRIPLE
SOUND_PATTERN_BEEP_UP_MIDDLE_DOWN
```

## USB Powered State

For use with `UsbPowerState` (via `InfoDeviceNotification`).

```
USB_POWER_STATE_USB_NOT_CONNECTED
USB_POWER_STATE_USB_CONNECTED
```

## Program Action

For use with `program_flow_notification` function.

```
PROGRAM_ACTION_START
PROGRAM_ACTION_STOP
```

---

**Return to start:** [Introduction and Installation](./README.md)
