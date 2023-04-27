### PetData: The folder to provide the web scraping bash scripts and store external data to use on FurEver Pet

Our web scraping source petango.com is no longer available. "Petango has been adopted by 24Petconnect, 24Pet’s leading online property for shelter adoptions and lost pet registrations." - the owner of Petango.

#### Web Scraping bash Scripts:
  - get_pet_profile_html.sh
  - get_pets_list.sh
  - petattrributes.sh
  - /Cat/AttributeHTML/catatt.sh
  - /Dog/AttributeHTML/petatt.sh

#### Auxiliary Files:
  - cat_name_id_subURL_list.txt
  - dog_name_id_subURL_list.txt
  
#### How does it work? Let's scrap a dog profile from Petago as an example:
  1. Launch a Bash(Unix shell), redirect the current path to /PetData.
  2. run `./get_pets_list.sh dog`; the script shall return "Number of dogs' name-id-subURL extracted: 32" "Extraction completed.", else it shall return an error message.
  3. You shall see a dog_name_id_subURL_list.txt under the current path. This text file contains many lines of scraped dog IDs, names, and URLs. Each line is surrounded by HTML <div></div>
  4. run `./get_pet_profile_html.sh dog`; the script creates a bunch of HTMLs under /Dog/AttributeHTML/.
  5. run `cd /Dog/AttributeHTML` to nevigate to /Dog/AttributeHTML, then run `petatt.sh 36636186_attributes.html`; this script creates a 36636186_attributes.html_attributes.txt that contains lines of human-readable dog features. The text is now ready to use on FurEver Pet.
