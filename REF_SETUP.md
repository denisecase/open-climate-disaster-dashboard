# Set Up Guide for Getting Started

This guide covers

- Use of Windows Subsystem for Linux (WSL) on Windows machines
- Tool installation (Python 3.10, GDAL)
- GDAL Configuration and Environment Variables
- GDAL Installation Verification
- Cloning and Opening the Project in VS Code
- Managing the Virtual Environment
- Help with Jupyter Notebooks and Kernel Selection
- Running Scripts (optional)
- General Notes

---

## 1. On Windows Machines Use WSL

Use Windows Subsystem for Linux. Launch WSL. 

```powershell
wsl
```

## 2. Tool Installation (Python 3.10, GDAL)

1. Remove any old versions of gdal.
2. Update package lists
3. Install Python 3.10 and Development Tools (needed for GDAL).
4. Add the UbuntuGIS Unstable PPA.
5. Install GDAL and Dependencies
6. Set the environment variables

```shell

sudo apt-get remove --purge -y gdal-bin libgdal-dev python3-gdal
sudo apt-get autoremove -y

sudo apt-get update -y

sudo apt-get install -y python3.10 python3.10-venv python3.10-dev build-essential

sudo add-apt-repository -y ppa:ubuntugis/ubuntugis-unstable
sudo apt-get update -y

sudo apt-get install -y gdal-bin libgdal-dev python3-gdal

export CPLUS_INCLUDE_PATH=/usr/include/gdal
export C_INCLUDE_PATH=/usr/include/gdal
export PATH=$PATH:/usr/bin/gdal
```

## 3. Persist GDAL Environment Variables

Persist the environment variables:

```shell
echo 'export CPLUS_INCLUDE_PATH=/usr/include/gdal' >> ~/.bashrc
echo 'export C_INCLUDE_PATH=/usr/include/gdal' >> ~/.bashrc
echo 'export PATH=$PATH:/usr/bin/gdal' >> ~/.bashrc
source ~/.bashrc
```

## 4. Verify GDAL Intallation

Persist the environment variables:

```shell
gdal-config --version
```

If you don't see a version number, it won't work. 
Troubleshoot installs until you see a version number. 

## 5. Git Clone and Open in VS Code

1. Open new terminal and verify gdal returns a version number (if not, reinstall).
2. Create ~/Repos if you don't have it already. On Windows, be sure you are in WSL.
3. Cd (change directory) into ~/Repos.
4. Fork and clone your repo down to your machine into the ~/Repos folder.
5. Open your open-climate-disaster-dashboard in VS Code (adjust the URl to use your GitHub account). 


```shell
gdal-config --version
mkdir ~/Repos
cd ~/Repos
git clone https://github.com/denisecase/open-climate-disaster-dashboard
code .
```



## 6. Manage Virtual Environment

From the VS Code menu, Terminal / New Terminal. Use Windows PowerShell (change commands if using Mac/Linux). 
See [requirements.txt](requirements.txt) for more information. 
If VS Code asks if it should use this, click Yes. 

```shell
python3.10 -m venv .venv
source .venv/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install --upgrade -r requirements.txt --timeout 100
python3 -m pip install GDAL==$(gdal-config --version)
gdal-config --version
```

Helpful verification commands:

```shell
which python
which python3 -m pip
python3 -m pip show pandas
python3 -m pip list
gdal-config --version
```

---

## Help With Notebook Issues

Register .venv as a new Jupyter kernel might help: 

```shell
python3 -m ipykernel install --user --name=ocdd_env --display-name "Python (ocdd_env)"
```

If a notebook was open while configuring .venv, completely exit VS Code and all notebooks. 
Go back to terminal (WSL if Windows), and cd into the project, and reopen VS Code. 

```shell
cd ~\Repos
cd open-climate-disaster-dashboard
code .
```

---

## Run Scripts (Optional)

Running the associated script (.py) will output charts to the [plots](plots/) folder.

```shell
clear
python3 notebooks/01_data_exploration.py
```

---

## General Notes

Use the up arrow to re-run commands. 
