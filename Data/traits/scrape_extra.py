import requests
import csv
from bs4 import BeautifulSoup

# Listing species' IDs to query
species_ids = []
with open("ids_extra.txt", "r") as file:
    species_ids = [line.rstrip() for line in file]

# Defining endpoint template and files to write
url_template = "https://api.eol.org/pages/{}/data"
csv_file = 'my_traits_extra.csv'
log_file = 'log_extra.txt'

# Fetching and parsing from API
def fetch_species_data(species_id):
    url = url_template.format(species_id)
    response = requests.get(url)
    # Checking for successful response
    if response.status_code == 200:
        # Parsing HTML content via BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        attributes = []
        filter_div = soup.find('div', class_='ui scrolling dropdown item') # div for filtering by attribute traits
        if filter_div:
            trait_links = filter_div.find_all('a', class_='item') # all <a> tags, to get trait names
            trait_names = [link.text.strip() for link in trait_links]
            trait_sections = soup.find_all('div', class_='data-section-head') # all data-section-head elements
            # Finding traits values
            for trait in trait_names:
                for trait_section in trait_sections:
                    trait_heading = trait_section.find('h3')
                    if trait_heading and trait_heading.text.strip() == trait:
                        next_sibling = trait_section.find_next_sibling()
                        while next_sibling and 'data-section-head' not in next_sibling.get('class', []):
                            # Extracting information within 'trait-val' for each 'js-data-row-contain'
                            if next_sibling.name == 'li' and 'js-data-row-contain' in next_sibling.get('class', []):
                                trait_val = next_sibling.find('div', class_='trait-val')
                                if trait_val:
                                    trait_data = trait_val.get_text(strip=True) # text content
                                    attributes.append([species_id, trait, trait_data]) # values' fetch
                            next_sibling = next_sibling.find_next_sibling()
                        break
        else:
            print(f"'Filter by attribute' section not found for species ID {species_id}")

        return attributes
    else:
        print(f"Failed to fetch data for species ID {species_id}, Status code: {response.status_code}")
        return []

# Saving dataset
with open(csv_file, mode='a', newline='') as file, open(log_file, mode='w') as log:
    writer = csv.writer(file)
    writer.writerow(['Species ID', 'Trait', 'Trait Value'])
    for species_id in species_ids:
        attributes = fetch_species_data(species_id)
        if attributes:
            writer.writerows(attributes)
            print(f"Done for species: {species_id}")
        else:
            print(f"Failed extraction for species: {species_id}")
            log.write(f"Failed extraction for species_id {species_id}\n")
print(f"Data extraction completed. Results are saved in {csv_file}")