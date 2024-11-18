import tinytuya
import time

# OutletDevice (Device ID, IPAddress, Local Key)
d = tinytuya.OutletDevice('*', '*', "*")
d.set_version(3.3)

# Get Status
data = d.status() 
print('set_status() result %r' % data)

# Turn On
d.set_value(20, True)
time.sleep(1)

# Blink
for _ in range(3):
    d.set_value(24, '00ee03e80447')#Blue
    time.sleep(1)  
    d.set_value(24, '000000000000')  
    time.sleep(1)
    d.set_value(24, '003203e80447')#Green  
    time.sleep(1)  
    d.set_value(24, '000000000000')  
    time.sleep(1)
    d.set_value(24, 'e2ffb8005447')#Red
    time.sleep(1)
    d.set_value(24, '000000000000')  
    time.sleep(1)
    d.set_value(24, '00000000447')#White
    time.sleep(1)
    d.set_value(24, '000000000000')  
    time.sleep(1)

# Turn Off
d.set_value(20, False)
