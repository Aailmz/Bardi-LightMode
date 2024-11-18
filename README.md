# Control Bardi Light & LED Strip Devices Using Python

### Overview
This project demonstrates how to control and make a light mode in Bardi LED Strip Devices LED Strip Devices using Python.

### Requirements
- Python 3.x
- Bardi Light Devices
- [Tuya Developer](https://developer.tuya.com/en/) and SmartApp
- [TinyTuya](https://pypi.org/project/tinytuya/) library for enhanced device control

### Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Aailmz/Bardi-LightMode.git
   cd Bardi-LightMode
   ```

2. **Install Dependencies:**
   ```bash
   pip install tinytuya
   ```

3. **Configure Bardi Devices:**
   
   **Tuya Developer:**
   - https://developer.tuya.com/en/
  
   **You can see the complete tutorial from here:**
   - https://pypi.org/project/tinytuya/
   - https://medium.com/@randhi.pp/control-bardi-smart-home-devices-using-python-3344868d2909
     
4. **Common Command:**
   
   **Scan Devices that connected:**
   ```bash
   python -m tinytuya scan 
   ```
   **Wizard Devices:**
   ```bash
   python -m tinytuya wizard 
   ```
   Each command output will be stored in .json file.

### Usage
- Run the light mode:
  ```bash
  python flowing.py
  ```
- Run simplified scanner:
  ```bash
  python scanner.py
  ```

### Contributing
Feel free to submit issues or pull requests to improve the project.
