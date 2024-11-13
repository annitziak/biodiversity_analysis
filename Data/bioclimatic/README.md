> [!WARNING]  
> Bioclimatic test and extra-train datasets and their cleaned versions are to big to be pushed on GitHub: please download locally the relevant .csv files from:
> https://drive.google.com/drive/folders/1Ojkg_U0m5Kp5ZZtRLn5YiAnA9nsLqpN_?usp=sharing

# Bioclimatic data
An information set about the various locations' environmental features has been extracted from the dataframes available at WorldClim; the outputs are saved as bioclimatic_train.csv, bioclimatic_train_extra.csv and bioclimatic_test.csv. The locations presenting invalid environmental values are then filtered out, the resulting datasets are stored into cleaned_bioclimatic_train.csv, cleaned_bioclimatic_train_extra.csv and cleaned_bioclimatic_test.csv.

**Variables of interest:**
- BIO1: Annual Mean Temperature
- BIO5: Max Temperature of Warmest Month
- BIO6: Min Temperature of Coldest Month
- BIO12: Annual Precipitation
- BIO15: Precipitation Seasonality (Coefficient of Variation)

(https://www.worldclim.org/data/worldclim21.html)