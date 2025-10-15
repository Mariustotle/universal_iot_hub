# Quick References




## Powershell

```powershell
# Connect to SSH
ssh pi@10.5.10.206
```


## Bash Commands

```bash
# View git status
git status

# Revert specific local changes
git restore filename

# Revert all local changes
git restore .
git clean -fd

# Update to latest code
git fetch
git pull --recurse-submodules

# Commit
git -m commit 'your-message-here'
git push
```

### Bash common actions

```bash
# Navigate to project folder
cd projects/universal_iot_hub/

# Activate local python
source local_env/bin/activate



# Edit config (Remove simulator mode)
sudo nano app_config.json

# Save latest packages added
pip freeze > requirements.txt
```


### Python

```python
# Start application
python main.py

#Cntr+Shift+D = Exit python in console
```

### Visual Studio Code

Shortcuts
- Cntr+Shift+P = Select Interpreter
- Cntr+K then v = View Markdown

