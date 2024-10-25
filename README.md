# aml_assignment

# 25-10-2024

Investigating the completeness of traits available in traits.csv. 
This file was downloaded from here: https://opendata.eol.org/dataset/all-trait-data-large/resource/6e24f0df-56ee-470f-b81e-e5a367a65bfb

We noticed a discrepancy between the information presented in the website, and that found in the downloaded csv. 
As a case study, we picked an animal "Pseudaspis cana" and checked the information on the website here: https://api.eol.org/pages/962419
this shows traits like "Body symmetry", "are eaten by" etc. 

In order to check if this information is available locally, we first try to find all traits for this animal. We did this by

```
DFtraits[DFtraits['scientific_name'] == "Pseudaspis cana"]
```

In order to find out if the trait is present, we first checked if there's a mapping from trait name to trait_id or some other representation, like so:

``` 
$ grep -E 'are eaten by' Data/traits/terms.csv
http://purl.obolibrary.org/obo/RO_0002471,are eaten by,association
```

Next, we filtered by checking for the presence of these traits as string values. 

```
# DFtraits[DFtraits['page_id'] == 962419].apply(lambda row: row.astype(str).str.contains('RO_0002471').any(), axis=1)
```

The above search yield false for all values, indicating that no such trait was present.
We repeated this for another animal 'Serpentes' and did find the presense of one trait (which validated the methodology), but confirmed the hypothesis that the data is incomplete for many animals.