import tinytuya

print("Scanning network again...")
devices = tinytuya.deviceScan()  # Basic scan
print("\nFound devices:")
for ip, device in devices.items():
    print(f"\nDevice found at {ip}:")
    print(f"  Device ID: {device['gwId']}")
    print(f"  IP: {device['ip']}")
    print(f"  Version: {device['version']}")