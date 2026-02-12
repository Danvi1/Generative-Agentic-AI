device_status = "active" # values are active or inactive
temperature = 36
if device_status == "active":
    if temperature > 35:
        print("Temperature is high!!!")
    else:
        print("Temperature is normal")
else: 
    print("Device is Offline")
