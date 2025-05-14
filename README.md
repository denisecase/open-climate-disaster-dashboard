# open-climate-disaster-dashboard

## On Windows Machines Use WSL

Use Windows Subsystem for Linux. Launch WSL. 

```powershell
wsl
```

## Install Tools

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

## Set Environment Variables

Persist the environment variables:

```shell
echo 'export CPLUS_INCLUDE_PATH=/usr/include/gdal' >> ~/.bashrc
echo 'export C_INCLUDE_PATH=/usr/include/gdal' >> ~/.bashrc
echo 'export PATH=$PATH:/usr/bin/gdal' >> ~/.bashrc
source ~/.bashrc
```

## Verify Intallation

Persist the environment variables:

```shell
gdal-config --version
```

If you don't see a version number, it won't work. 
Troubleshoot installs until you see a version number. 

## Git Clone and Open in VS Code

1. Open new terminal and verify gdal returns a version number (if not, reinstall).
2. Create ~/Repos if you don't have it already. 
3. Install VS Code and Python in WSL.
4. Fork and clone the repo to your machine (e.g. ~/Repos).
5. Open your open-climate-disaster-dashboard in VS Code (adjust the URl to use your GitHub account). 


```shell
mkdir ~/Repos
cd ~/Repos
git clone https://github.com/denisecase/open-climate-disaster-dashboard
code .
```



## Manage Virtual Environment

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

## Notebook Issues

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

## Run Scripts (Optional)

```shell
python3 notebooks/01_data_exploration.py
```

## Data Sources

NOAA National Centers for Environmental Information (NCEI) U.S. Billion-Dollar Weather and Climate Disasters (2025). https://www.ncei.noaa.gov/access/billions/, DOI: 10.25921/stkw-7w73

Smith, Adam B. (2020). U.S. Billion-dollar Weather and Climate Disasters, 1980 - present (NCEI Accession 0209268). [indicate subset used]. NOAA National Centers for Environmental Information. Dataset. https://doi.org/10.25921/stkw-7w73. Accessed [2025-05-13].
[Link](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0209268),
[NOAA_SOURCE.md](NOAA_SOURCE.md).

## See Also

- <https://www.climate.gov/news-features/blogs/beyond-data/2024-active-year-us-billion-dollar-weather-and-climate-disasters>