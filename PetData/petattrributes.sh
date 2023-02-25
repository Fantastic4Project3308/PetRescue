#This is a script to scrape each pet html page for attributes: breed, age, gender, color, if spayed, size

if [[ -f $1 ]]; then
    echo -e "Breed \n" > "$1"_attributes.txt
    grep "text: breed" $1 >> "$1"_attributes.txt
    echo -e "Age \n" > "$1"_attributes.txt
    grep "text: Age:" $1 >> "$1"_attributes.txt
    echo -e "Gender \n" > "$1"_attributes.txt
    grep "text: Gender:" $1  >> "$1"_attributes.txt
    echo -e "Color \n" > "$1"_attributes.txt
    grep "text: Color:" $1 >> "$1"_attributes.txt
    echo -e "Spayed \n" > "$1"_attributes.txt
    grep "text: spayedNeutered" $1 >> "$1"_attributes.txtx
    echo -e "Size \n" > "$1"_attributes.txt
    grep "text: size" $1 >> "$1"_attributes
    
else
    echo "file does not exist"
fi