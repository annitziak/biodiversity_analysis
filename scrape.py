import requests
import csv
from bs4 import BeautifulSoup

# List of species IDs to query
species_ids = [962419]  # Add your list of IDs here

# Define the endpoint template
url_template = "https://api.eol.org/pages/{}/data"

# CSV file to write data
csv_file = 'my_traits.csv'

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
            
            for link in trait_links:
                trait = link.text.strip()  # Get trait name
                
                # Find the specific section for this trait
                trait_section = soup.find('div', class_='data-section-head', string=trait)
                if trait_section:
                    # Get all associated 'trait-val' data for this trait
                    trait_values = trait_section.find_next_siblings('li', class_='js-data-row-contain')
                    
                    for value in trait_values:
                        trait_val = value.find('div', class_='trait-val')
                        if trait_val:
                            # Extract value text
                            trait_data = trait_val.get_text(strip=True)
                            # Append data as a new row: species ID, trait, trait value
                            attributes.append([species_id, trait, trait_data])
        else:
            print(f"'filter by attribute' section not found for species ID {species_id}")

        return attributes
    else:
        print(f"Failed to fetch data for species ID {species_id}, Status code: {response.status_code}")
        return []

# Write headers to CSV file
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Species ID', 'Trait', 'Trait Value'])

    # Iterate through species IDs and fetch/write data
    for species_id in species_ids:
        attributes = fetch_species_data(species_id)
        if attributes:
            writer.writerows(attributes)

print(f"Data extraction completed. Results are saved in {csv_file}")
