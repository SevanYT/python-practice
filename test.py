# A simple power load estimation check device_name = input("Enter component name: ") power_draw_watts = float(input("enter power draw in watts: ")) 
if power_draw_watts > 50: 
    print(f"warning: {device_name} draws high power! you will need active cooling.") 
else: 
    print(f"safe: {device_name} is low power.")  
