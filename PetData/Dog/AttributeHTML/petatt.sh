#This is a script to scrape each pet html page for attributes: name, breed, age, gender, color, size
#to do: background and location
if [[ -f $1 ]]; then
    echo -e "Name:" > "$1"_attributes.txt
    grep -o -P '(?<="lbName">).*(?=</span>)' $1 >> "$1"_attributes.txt
    echo -e "Description: " > "$1"_attributes.txt
    grep -o -P '(?<="og:description").*(?=/>)' $1 >> "$1"_attributes.txt
    echo -e "Breed:" >> "$1"_attributes.txt
    grep -o -P '(?<="lbBreed">).*(?=</span>)' $1 >> "$1"_attributes.txt
    echo -e "Age:" >> "$1"_attributes.txt
    grep -o -P '(?<="lbAge">).*(?=</span>)' $1 >> "$1"_attributes.txt
    echo -e "Gender:" >> "$1"_attributes.txt
    grep -o -P '(?<="lbSex">).*(?=</span>)' $1 >> "$1"_attributes.txt
    echo -e "Color:" >> "$1"_attributes.txt
    grep -o -P '(?<="lblColor">).*(?=</span>)' $1 >> "$1"_attributes.txt
    echo -e "Size:" >> "$1"_attributes.txt
    grep -o -P '(?<="lblSize">).*(?=</span>)' $1 >> "$1"_attributes.txt
    echo -e "Location:" >> "$1"_attributes.txt
    grep -o -P '(?<="lblLocation">).*(?=</span>)' $1 >> "$1"_attributes.txt
    
else
    echo "file does not exist"
fi