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


## IoT Specific Setup
- [Raspbery Pi 3/4/5](device_setup/raspberry_pi_3_4_5.md)
- [Raspberri Pi Pico](device_setup/raspberry_pi_pico.md)


## Quick References
- Cntr+Shift+P = Select Interpreter
- Cntr+K then v = View Markdown