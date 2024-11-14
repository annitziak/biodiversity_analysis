import requests
import csv
from bs4 import BeautifulSoup

# List of species IDs to query
species_ids = []  # Add your list of IDs here
with open("ids_extra.txt", "r") as file:
    species_ids = [line.rstrip() for line in file]

# Define the endpoint template
url_template = "https://api.eol.org/pages/{}/data"

# CSV file to write data
csv_file = 'my_traits_extra.csv'
log_file = 'log.txt'

# Function to fetch and parse data from API
def fetch_species_data(species_id):
    url = url_template.format(species_id)
    response = requests.get(url)
    
    # Check for a successful response
    if response.status_code == 200:
        # Parse the HTML content with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Define the list to collect attributes
        attributes = []
        
        # Find the specific div containing the filter by attribute traits
        filter_div = soup.find('div', class_='ui scrolling dropdown item')


        if filter_div:
            # Find all <a> tags within this div to get trait names
            trait_links = filter_div.find_all('a', class_='item')
            trait_names = [link.text.strip() for link in trait_links]
            
            # Retrieve all data-section-head elements once
            trait_sections = soup.find_all('div', class_='data-section-head')

            # Loop through each trait name to find its associated values
            for trait in trait_names:
                for trait_section in trait_sections:
                    trait_heading = trait_section.find('h3')
                    
                    # Check if the trait heading matches the current trait
                    if trait_heading and trait_heading.text.strip() == trait:
                        # Start collecting trait values from the current section
                        next_sibling = trait_section.find_next_sibling()
                        while next_sibling and 'data-section-head' not in next_sibling.get('class', []):
                            # Extract information within 'trait-val' for each 'js-data-row-contain'
                            if next_sibling.name == 'li' and 'js-data-row-contain' in next_sibling.get('class', []):
                                trait_val = next_sibling.find('div', class_='trait-val')
                                if trait_val:
                                    # Get the text content for each trait value
                                    trait_data = trait_val.get_text(strip=True)
                                    # Append data as a new row: species ID, trait, trait value
                                    attributes.append([species_id, trait, trait_data])
                            # Move to the next sibling element
                            next_sibling = next_sibling.find_next_sibling()
                        break  # Exit the loop once the correct trait section is processed
        else:
            print(f"'filter by attribute' section not found for species ID {species_id}")

        return attributes
    else:
        print(f"Failed to fetch data for species ID {species_id}, Status code: {response.status_code}")
        return []

# Write headers to CSV file
with open(csv_file, mode='w', newline='') as file, open(log_file, mode='w') as log:
    writer = csv.writer(file)
    writer.writerow(['Species ID', 'Trait', 'Trait Value'])

    # Iterate through species IDs and fetch/write data
    for species_id in species_ids:
        attributes = fetch_species_data(species_id)
        if attributes:
            writer.writerows(attributes)
            print(f"Done for species: {species_id}")
        else:
            print(f"Failed extraction for species: {species_id}")
            log.write(f"Failed extraction for species_id {species_id}\n")

print(f"Data extraction completed. Results are saved in {csv_file}")