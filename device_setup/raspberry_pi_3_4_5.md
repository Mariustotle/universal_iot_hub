# 🧠 Setup Using Raspberry Pi 3 / 4 / 5

The Raspberry Pi 3/4/5 is a **Single Board Computer (SBC)**. Despite its small size, it functions like a regular computer — it has storage (via SD card), RAM, HDMI output, and USB ports for peripherals. It runs a full operating system, often Raspberry Pi OS (Linux-based), making it ideal for IoT prototyping.

---

## 🔧 Implementation Approach

While development can be done **directly on the Pi**, it's more efficient to use your **laptop or desktop** and connect to the Pi remotely via SSH or VS Code. This approach:

- Keeps your Pi uncluttered
- Improves responsiveness
- Makes it easier to migrate to **headless** or **microcontroller-based** devices later (like the Pi Pico or ESP32)

---

# 🚀 Device Setup

## 1. Install the Operating System

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


### Configure SSH on Raspberry Pi

- Setup SSH (If it was not done on the installer settings)
  
    ```bash
    sudo systemctl enable ssh
    sudo systemctl start ssh

    # View status
    sudo systemctl status ssh
    ```


## 2. Configure Networking

Once booted and connected to your Wi-Fi, you could also do this through your DHCP then you do not need to log into the device OS.

```bash
# View OS Version (the network file might vary)
cat /etc/os-release

# View current IP address
hostname -I

# Show WiFi connections
nmcli connection show

# (Optional) Set a static IP for stability
sudo nano /etc/NetworkManager/system-connections/{connection_name}.nmconnection

```

```ini
[ipv4]
method=manual
addresses=X.X.X.X/24
gateway=X.X.X.X
dns=8.8.8.8;
```
Nano commands: Cntr+O (Save) then Cntr+X (Exit)

```bash
sudo nmcli connection reload
sudo nmcli connection up "{connection_name}"
```

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
    md projects
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
    - Do x
    - Do y. 


