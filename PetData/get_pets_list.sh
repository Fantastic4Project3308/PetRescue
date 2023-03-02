if [ -z "$1" -o $(echo "$1" | grep -E -io "cat|dog" | wc -l) -ne 1 ]; then
    echo "Must specify one input parameter, it can be either \"cat\" or \"dog\"."
    echo "Exit get_pets_list.sh"
    exit
fi

#time_stamp=$(date '+ %d-%m-%Y-%H-%M-%S')
#names_path="${pwd}/$1$time_stemp.txt"
#
#if [ -d $names_path ]; then 
#    rm $names_path 
#fi

ws_pentago="https://ws.petango.com/webservices/adoptablesearch"
ws_adoptableAnimals="wsAdoptableAnimals.aspx"
AUTH_KEY="x5eowv5twf8po63is6gylhf8r608c75k6ksb48t17nmtjtfyof"
name_id_subURL_list="$1_name_id_subURL_list.txt"
temp_html="temp.html"

wget -q -O $temp_html "$ws_pentago/$ws_adoptableAnimals?species=$1&colnum=5&authkey=$AUTH_KEY"
grep "list-animal-name" $temp_html > $name_id_subURL_list
rm $temp_html
echo "Number of $1s' name-id-subURL extracted: $(cat $1_name_id_subURL_list.txt | wc -l)"
echo "Extraction completed."