import serial
import time

SERIAL_PORT = "/dev/ttyS0"  # Or /dev/ttyAMA0
BAUD_RATE = 57600

def send_command(ser, command):
    ser.write(command)
    time.sleep(0.1)  # Adjust delay as needed
    response = ser.read(ser.in_waiting)
    return response

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=5)

    # Command: Verify Password (adjust as needed)
    verify_password_command = b'\xEF\x01\xFF\xFF\xFF\xFF\x01\x00\x07\x13\x00\x00\x00\x00\x00\x1B'
    response = send_command(ser, verify_password_command)
    print(f"Verify password response: {response.hex()}")

    ser.close()

except serial.SerialException as e:
    print(f"Serial port error: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")