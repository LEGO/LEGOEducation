# Simple Connect and Run Example

# 1. Import the legoeducation library using le alias
import legoeducation as le

# 2. Define a variable for the hardware
singlemotor = le.SingleMotor()

# 3. Connect to the hardware using a Connection Card
# Example: Azure Color Card with Serial Number 3683
singlemotor.connect(card_color=le.LEGO_COLOR_AZURE, card_serial="3683")

# 4. Check if (not) connected
if not singlemotor.connected:
	print('Error connecting to Single Motor.')
	exit(1) # error connecting

# 5. Interact with the hardware
singlemotor.motor_run_for_degrees(360) # run one rotation

# 6. Disconnect from the hardware
singlemotor.disconnect()
exit(0) # successful execution