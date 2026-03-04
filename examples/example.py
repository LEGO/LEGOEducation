import legoeducation as le

# Connect to Single Motor
singlemotor = le.SingleMotor()
singlemotor.connect()

# Check if connected
if not singlemotor.connected:
	print('Error connecting to Single Motor.')
	exit(1) # error connecting

# Main Code:
singlemotor.motor_run_for_degrees(360) # run one rotation

# Disconnect from Single Motor
singlemotor.disconnect()
exit(0) # successful execution