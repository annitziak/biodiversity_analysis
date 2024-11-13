# Species' locations data
An information set about the geographical coordinates where different species have been observed; the train data has been collected by citizen scientists and obtained from iNaturalist, the test data - describing the presence of the same species as the training set in other locations - is downloaded from IUCN. The relevant .npz files are loaded and locations presenting invalid environmental values (see Data/bioclimatic) are filtered out; the resulting datasets are stored into species_train.csv, species_train_extra.csv, and species_test.csv.

(https://www.inaturalist.org)
(https://www.iucnredlist.org/resources/spatial-data-download)