### Project Initialization

**Linux virtual environment**
```sh
# Linux/Ubuntu
python -m venv --clear .venv # Clear .venv folder before proccedding
source .venv/bin/activate  
python -m pip install --upgrade pip
# Install required packages
pip install -r requirements.txt
```
 
**Windows virtual environment**
```sh
# Windows PS
python -m venv --clear .venv
.\.venv\Scripts\Activate.ps1
# Install required packages
pip3 install -r requirements.txt