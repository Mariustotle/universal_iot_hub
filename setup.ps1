# Create local python instance
# =============================
python312 -m virtualenv local_env
./local_env/Scripts/activate


# Update package Manager
python -m pip install --upgrade pip


# Install required packages
pip install -r requirements.txt

# Save updates to packages
pip freeze > requirements.txt





