import serial.tools.list_ports

def find_available_serial_ports():
    ports = serial.tools.list_ports.comports()
    available_ports = [port.device for port in ports]
    return available_ports

# Call the function and print the results
if __name__ == "__main__":
    available_ports = find_available_serial_ports()
    if available_ports:
        print("Available Serial Ports:")
        for port in available_ports:
            print(f" - {port}")
    else:
        print("No serial ports available.")
