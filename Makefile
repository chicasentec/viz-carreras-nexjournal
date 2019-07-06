download_inputs :
	rm data/input/data.csv
	rm data/input/data.csv.1
	rm data/input/data.csv.2 
	wget -i input_url.txt -P data/input --content-disposition --trust-server-names


