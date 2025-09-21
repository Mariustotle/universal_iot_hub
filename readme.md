# 🌐 Universal IoT Hub

A modular, extensible IoT Hub built in Python for enthusiasts and developers to **prototype, test, and manage** various IoT peripherals. This project serves as a central hub, making it easy to:

- Connect and test sensors, actuators, and communication modules.
- Interact via a simple console interface to test and simulate devices
- Extend new devices with custom drivers and shared contracts.

---

## 📦 Project Overview

This project is structured into:

### Repositories
- **Core IoT Hub**: Main runtime logic and thread orchestration.
- **Peripheral Submodule**: Reusable device definitions (sensors, actuators, communication modules).
🔗 [Peripheral Submodule on GitHub »](https://github.com/Mariustotle/universal_iot_hub)

### Supported Peripherals
The IoT platforms is configuration based, so you just need to configure the peripherals you want and it will load them up in the menu.  You can browse the available [peripherals here](https://github.com/Mariustotle/iot_peripherals/blob/main/peripheral_index.md).

---

## 🚀 Getting Started

### 1. Install Required Software

Make sure the following tools are installed on your system:

- [VS Code](https://code.visualstudio.com/)
- [Git for Windows](https://git-scm.com/) (Terminal Git)
- [Fork Git Client](https://fork.dev/) (GUI Git)
- [PuTTyGEN]() (SSH Key Generator)
- Install Python (PowerShell in administrator Mode)
  ```powershell
    # Create new Alias Profile (Persist alias with reboot)
    New-Item -Path $PROFILE.AllUsersAllHosts -Type File -Force
    $PROFILE | Select-Object -Property AllUsersAllHosts

    # Install the specific Python version
    choco install python --version=3.12.5 -y --force

    # Set a PowerShell Alias for this version on the Global Profile
    Add-Content -Path $PROFILE.AllUsersAllHosts -Value 'Set-Alias -Name python312 -Value "C:\Python312\python.exe"'
    . $PROFILE.AllUsersAllHosts
    python312 --version

    #  Update PIP
    python312 -m pip install --upgrade pip

    # Install virtual environment package
    python312 -m pip install virtualenv    

  ```

---

### 2. Clone the Repository

```powershell
git clone https://github.com/Mariustotle/universal_iot_hub.git
cd universal_iot_hub
git submodule update --init --recursive
```

### 3. Setup the Project on your main windows devlopment environment

1. Install VS Code Extentions
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
   - [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
   - [Remote Development extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
  
2.  Setup IoT Project
    1.  Create local virtual environment and activate it
        ```powershell
        python -m pip install --upgrade pip

        python312 -m virtualenv local_env
        ./local_env/Scripts/activate
        ```
    2.  Install packages
        ```powershell 
        pip install -r requirements.txt
        ```
    3.  Setup launch file
        ```json
        {
            "version": "0.2.0",
            "configurations": [
                {
                "name": "Run main.py",
                "type": "python",
                "request": "launch",
                "program": "${workspaceFolder}/main.py",
                "console": "integratedTerminal"
                }
            ]
        }
        ```
   
3.  Run the solution and interact with the menu in the console
    - In the config (app_config.json) switch on the simulator
        ```json
            {
                "Simulator": true,
                ...
            }
        ```
    - Run "main.py"
    - Follow the console menu and see how it works
  
4. *Setup the remote connection
   1. Check that you have connectivity
        ```PowerShell
        # Test Connectivity
        telnet x.x.x.x 22

        # Connect to SSH Server
        ssh user@x.x.x.x -A
        ```

   2. Add new SSH Host (Xntr+Shift+P) >> "Remote-SSH: Add New Host" 
   3. Add the static IP address of your Pi
        ```
        ssh pi@<raspberrypi-ip-address> -A
        ```
        *Note: Default user = pi, password = raspberry which you have hopefully changed.*
   4. This will now install the VS Code Server on the remote device
   
        *You can get a more comprehensive guide from the source [Official Guide](https://code.visualstudio.com/docs/remote/ssh)*
        
   
5. Make the connection seamless
   You will get prompted for the password until you setup a key exchange.

   + Generate a SSH Key from PuttyGen (SSH-2 RSA Key)
     + Save the FULL key (Putty format) as **id_rsa_full.ppk**
     + Copy public key into a **id_rsa.pub** file

        ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/PuTTyGen_publicKey.png)

     + Save the private key (In Open SSH format) as **id_rsa** file

        ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/PuTTyGen_privateKey.png)  
    
     + Copy the above 2 files to C:\Users\{username}\.ssh\pi\ (Laptop)

        ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/sshKeys.png)  
   
    + Open SSH connection to PI e.g. `ssh {user}@{address}`
    + Create SSH Folder on the Pi (Will complain if already exist) `$ sudo mkdir ~/.ssh`
    + Edit the SSH Authorization file `$ sudo nano ~/.ssh/authorized_keys`
      Copy paste from **id_rsa.pub** (Public Key) file >> Cntr+O (Save) Cntr+X (Exit)
    + Set the required file protection
    
        ```bash
        # Fix ownership (make sure pi owns its own .ssh folder)
        sudo chown -R pi:pi /home/pi/.ssh

        # Fix folder permissions
        chmod 700 /home/pi/.ssh
        chmod 700 ~/.ssh

        # Fix file permissions (if they exist)
        chmod 600 /home/pi/.ssh/authorized_keys
        chmod 600 ~/.ssh/authorized_keys
        
        # View SSH auth options
        grep -i auth /etc/ssh/sshd_config
     
        ```
      
   + Configure the SSH Connection
       + Open the config file (Global SSH config file) in VS Code (Settings cog in remote window)
       + Add the IdentityFile reference pointing to the id_rsa file (Private Key)
       
       ![](https://raw.githubusercontent.com/mariusvrstr/hydriot/main/Raspberry%20Pi/_resources/sshConfigurationFile.png)    
       + Save and restart VS Code (Desktop)
   + Reconnect to remote VS Code environment (Should NOT prompt for pass)


## IoT Specific Setup
- [Raspbery Pi 3/4/5](device_setup/raspberry_pi_3_4_5.md)
- [Raspberri Pi Pico](device_setup/raspberry_pi_pico.md)


## Quick References

### VS Code
- Cntr+Shift+P = Select Interpreter
- Cntr+K then v = View Markdown

### Python
- pip freeze > requirements.txt


### Linux Run from Bash

```bash
# Navigate to project folder
cd projects/universal_iot_hub/

# Update to latest code
git fetch
git pull --recurse-submodules

# Activate local python
source local_env/bin/activate

# Start application
python main.py
```


