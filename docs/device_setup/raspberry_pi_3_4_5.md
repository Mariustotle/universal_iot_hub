# 🧠 Setup Using Raspberry Pi 3 / 4 / 5

The Raspberry Pi 3/4/5 is a **Single Board Computer (SBC)**. Despite its small size, it functions like a regular computer — it has storage (via SD card), RAM, HDMI output, and USB ports for peripherals. It runs a full operating system, often Raspberry Pi OS (Linux-based), making it ideal for IoT prototyping.


## Configuration

1. Setup your OS
   1. Format and install OS on SD
   2. Configure the device
   3. Setup OS Specific Pi
      - Raspberry Pi 3
      - Raspberry Pi 4
      - Raspberry Pi 5
  
2. Configure the Project
   1. Configure Git
   2. Configure Python


## 1.1 Install the Operating System

1. Download and install the [Raspberry Pi Imager](https://www.raspberrypi.com/software/).
2. Insert your SD card into your computer.
3. Launch the Imager and select:
   - **Device**: Match your Raspberry Pi model
   - **OS**: Choose "Raspberry Pi OS (32-bit) with Desktop" *(lightweight with GUI)*
     > [Compare OS versions](https://www.raspberrypi.com/software/operating-systems/)
4. Click the ⚙️ gear icon ("**Edit Settings**") to customize:
   - Set **username** and **password**
   - Enable **Wi-Fi** and input credentials
   - Enable **SSH**
   - Set **device name (hostname)** if desired
5. Flash the image and insert the SD card into your Pi.
6. Power on the device and wait for it to boot.


## 1.2 Configure Device

![Control Centre](https://raw.githubusercontent.com/Mariustotle/universal_iot_hub/refs/heads/main/resources/os/raspberry_pi_console_centre.jpg)


Setting                 | Description                                
-------------           | ---------------
SSH                     | Needed for remote terminal access
SPI                     | Fast device communication bi-directional GPIO communication
1-Wire                  | A very simple communication bus for low-speed sensors—typically temperature sensors like DS18B20
Serial Port             | Provides a serial communication interface (TX/RX pins) for connecting to microcontrollers, GPS modules, or other serial devices
Serial Console          | Lets you access the Raspberry Pi’s terminal (command line) through the UART serial pins.





## 3. Configure via PowerShell


```PowerShell
# Easier to configure from PowerShell on laptop than Bash on Pi
ssh {user}@{ip} 22
```


## 4. Install Required Software

- Update the Linux packages
    ```bash
    sudo apt update && sudo apt upgrade -y
    ```

- Install latest Python (Should already be installed)
  
    ```bash

    # Install the latest version
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip

    # View version
    python3 --version

    ```

    *You could take a longer route and install a [specific python version](device_setup/raspberry_pi_pico.md).*

- Git
  
    ```bash
    sudo apt install git -y

    ```



- VS Code Server
  
    Go back to the main readme and do the [Setup the remote connection] step for Visual Studio Code. It is installed via SSH.

*Visit the official site for a more [detailed walkthrough](https://www.raspberrypi.com/documentation/computers/getting-started.html).*

## 5. Setup the project

1. Clone the project to 
   ```bash
    # Create and checkout to a projects folder in the root
    mkdir projects
    cd projects
    git clone https://github.com/Mariustotle/universal_iot_hub.git
    
    # Submodule checkout
    cd universal_iot_hub
    git submodule update --init --recursive
   ```
  
2. Create a virtual environmenment and install packages
   
   ```bash

    # Check that Venv is installed
    sudo apt install -y python3-venv

    # Navigate to root project folder
    cd ~/projects/universal_iot_hub

    # Create and use virtual environment
    python3 -m venv local_env
    . ./local_env/bin/activate

    # Run requirements.txt
    pip install -r requirements.txt

   ```

3. Configure VS Code for remote access
    - Install Extensions
      - Python
  
    - Do y. 


