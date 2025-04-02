import serial
import time

SERIAL_PORT = "/dev/ttyS0"  # Or /dev/ttyAMA0
BAUD_RATE = 57600

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5)

    verify_password_command = b'\xEF\x01\xFF\xFF\xFF\xFF\x01\x00\x07\x13\x00\x00\x00\x00\x00\x1B'
    ser.write(verify_password_command)
    time.sleep(0.5)  # Give it time to respond
    response = ser.read(ser.in_waiting)
    print(f"Response: {response}")  # Print the raw response
    print(f"Response (hex): {response.hex()}")

    ser.close()

except serial.SerialException as e:
    print(f"Serial port error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")