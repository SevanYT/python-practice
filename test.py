# A simple power load estimation check
device_name = input("Enter component name: ")
power_draw_watts = float(input("Enter power draw in Watts: "))

if power_draw_watts > 50:
    print(f"Warning: {device_name} draws high power! You will need active cooling.")
else:
    print(f"Safe: {device_name} is low power.")
