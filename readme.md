# 🌐 Universal IoT Hub

A modular, extensible IoT Hub built in Python for enthusiasts and developers to **prototype, test, and manage** various IoT peripherals. This project serves as a central hub, making it easy to:

- Connect and test sensors, actuators, and communication modules.
- Interact via a simple console interface to test and simulate devices
- Extend new devices with custom drivers and shared contracts.

---

## 📦 Project Overview

This project is structured into:

- **Core IoT Hub**: Main runtime logic and thread orchestration.
- **Peripheral Submodule**: Reusable device definitions (sensors, actuators, communication modules).
🔗 [Peripheral Submodule on GitHub »](https://github.com/Mariustotle/universal_iot_hub)

---

## 🚀 Getting Started

### 1. Install Required Software

Make sure the following tools are installed on your system:

- [VS Code](https://code.visualstudio.com/)
- [Git for Windows](https://git-scm.com/) (Terminal Git)
- [Fork Git Client](https://fork.dev/) (GUI Git)
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
        ping x.x.x.x
        telnet x.x.x.x 22
        ssh user@x.x.x.x
        ```

   2. Add new SSH Host (Xntr+Shift+P) >> "Remote-SSH: Add New Host" 
   3. Add the static IP address of your Pi
        ```
        ssh pi@<raspberrypi-ip-address> -A
        ```
        *Note: Default user = pi, password = raspberry which you have hopefully changed.*
    4. This will now install the VS Code Server on the remote device
  
  
*Note: This is just for initial testing, the approach we want to take is remotely working from your laptop to the pi ([Official Guide](https://code.visualstudio.com/docs/remote/ssh)).*


## IoT Specific Setup
- [Raspbery Pi 3/4/5](device_setup/raspberry_pi_3_4_5.md)
- [Raspberri Pi Pico](device_setup/raspberry_pi_pico.md)

### Peripheral Configuration
The IoT platforms is configuration based, so you just need to configure the peripherals you want and it will load them up in the menu. 

*Browse the available [peripherals here](device_setup/peripheral_configuration.md).*



## Quick References
- Cntr+Shift+P = Select Interpreter
- Cntr+K then v = View Markdown