import tinytuya
import time

# OutletDevice (deviceId, ipAddress, localKey)
d = tinytuya.OutletDevice('eb885ae9d9d24f7f0ayi2s', '192.168.100.39', "8r!tQFKBHInG'TDf")
d.set_version(3.3)

# Get Status
data = d.status() 
print('set_status() result %r' % data)

# Turn On
d.set_value(20, True)
time.sleep(1)

#Blink
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

d.set_value(20, False)
