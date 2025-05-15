# Open Climate Disaster Dashboard

![Under Construction](https://img.shields.io/badge/status-under_construction-yellow?style=for-the-badge)

![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)
![Python](https://img.shields.io/badge/python-3.10%2B-green.svg)
![GitHub last commit](https://img.shields.io/github/last-commit/denisecase/open-climate-disaster-dashboard)
![GitHub issues](https://img.shields.io/github/issues/denisecase/open-climate-disaster-dashboard)

Based on NOAA Web Site at: <https://www.ncei.noaa.gov/access/billions/>

- Current Notebook: [notebooks/01_data_exploration.ipynb](notebooks/01_data_exploration.ipynb)
- Current Script: [notebooks/01_data_exploration.py](notebooks/01_data_exploration.py)

## NOAA Data Source

- **Dataset:** [NOAA NCEI U.S. Billion-Dollar Weather and Climate Disasters (2025)](https://www.ncei.noaa.gov/access/billions/)
- **DOI:** [10.25921/stkw-7w73](https://doi.org/10.25921/stkw-7w73)
- **Citation:**  Smith, Adam B. (2020). *U.S. Billion-dollar Weather and Climate Disasters, 1980 - present* (NCEI Accession 0209268).  
  NOAA National Centers for Environmental Information. Dataset.  
  Accessed [2025-05-13].
- **License:** Public Domain, as provided by the U.S. Government.  
- The dataset is publicly available and can be accessed [here](https://www.ncei.noaa.gov/access/metadata/landing-page/bin/iso?id=gov.noaa.nodc:0209268).
- More information at [REF_NOAA_SOURCE.md](REF_NOAA_SOURCE.md).

## NOAA Dataset Details

- All costs are measured in **millions of USD**.
- The dataset includes columns for:
    - `Name`: The name of the disaster.
    - `Disaster`: The type of event (e.g., Flooding, Hurricane).
    - `Begin Date`: The starting date of the event.
    - `End Date`: The ending date of the event.
    - `CPI-Adjusted Cost`: The cost adjusted for inflation.
    - `Unadjusted Cost`: The raw cost at the time of the event.
    - `Deaths`: The number of fatalities attributed to the event.
- Example Row: `Western Storms and Flooding (December 1982-March 1983),Flooding,19821213,19830331,4828.7,1499.6,50`

## Original Web Page
For more information, visit the official NOAA [Billion-Dollar Weather and Climate Disasters](https://www.ncei.noaa.gov/access/billions/) page.

![Preview](images/noaa_cpi_cummulative_monthly.jpg)

## Current Preview
Below is the initial view of the monthly CPI-Adjusted Costs of Billion-Dollar Disasters. 
An PyShiny dashboard is planned for interactive exploration.

![Monthly CPI-Adjusted Costs of Billion-Dollar Disasters](plots/07_MonthlyCPI.png)

## See Also
For more insights into climate impacts and billion-dollar disasters:
- [NOAA Climate Blog (2024 Active Year for Disasters)](https://www.climate.gov/news-features/blogs/beyond-data/2024-active-year-us-billion-dollar-weather-and-climate-disasters)

## Installation
To set up the project, follow the instructions in [REF_SETUP.md](REF_SETUP.md).

## Contributions
Contributions are welcome! 
Please open an issue or submit a pull request. 
See the [CONTRIBUTING.md](CONTRIBUTING.md) guide for more information.

## License
This project is licensed under the **Apache 2.0 License**. 
See the [LICENSE](LICENSE) file for details.
