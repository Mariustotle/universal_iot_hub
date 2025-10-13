# How to install a Specific Python Version

This will show you how to download, build and install a specific python version.

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Build Tools
sudo apt install -y build-essential libssl-dev zlib1g-dev \
libncurses5-dev libgdbm-dev libnss3-dev libreadline-dev \
libffi-dev libsqlite3-dev wget curl libbz2-dev

# Download Source

cd /usr/src
sudo wget https://www.python.org/ftp/python/3.12.7/Python-3.12.7.tgz
sudo tar xzf Python-3.12.7.tgz
cd Python-3.12.7

# Install
sudo ./configure --enable-optimizations
sudo make -j$(nproc)
sudo make altinstall

# Verify version
python3.12 --version

# Create Alias
sudo update-alternatives --install /usr/bin/python312 python312 /usr/local/bin/python3.12 1

# Test Alias
python312 --version


# Test Alias
python3.12 --version

# Upgrade pip
python -m ensurepip --upgrade
python -m pip install --upgrade pip
```







