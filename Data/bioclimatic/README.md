# Bioclimatic data

The bioclimatic variables were extracted from [WorldClim](https://www.worldclim.org/data/worldclim21.html), using TIFF files georeferenced with *EPSG:4326* coordinates: six key temperature and precipitation variables were selected, and their values queried for each unique sighting location. By a preliminary exploration, some erroneous
values were identified, mainly for sightings recorded in the middle of the ocean; these instances were thus considered as outliers and removed to ensure a reliable analysis.

**Variables of interest:**

- BIO1: Annual Mean Temperature
- BIO5: Max Temperature of Warmest Month
- BIO6: Min Temperature of Coldest Month
- BIO12: Annual Precipitation
- BIO15: Precipitation Seasonality (coefficient of variation)

> [!NOTE]  
> The resulting datasets are stored into [cleaned_bioclimatic_train.csv](./cleaned_bioclimatic_train.csv) and [cleaned_bioclimatic_test.csv](./cleaned_bioclimatic_test.csv); further instances' bioclimatic features can be found in [cleaned_bioclimatic_train_extra.csv](./cleaned_bioclimatic_train_extra.csv).

> [!WARNING]  
> The test and extra-train datasets - both in their original and cleaned version - are too heavy to be pushed on GitHub: please download locally the relevant .csv files [here](https://drive.google.com/drive/folders/1Ojkg_U0m5Kp5ZZtRLn5YiAnA9nsLqpN_?usp=sharing).
