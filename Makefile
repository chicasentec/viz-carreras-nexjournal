download_inputs :
	rm -f data/input/data.csv
	rm -f data/input/data.csv.1
	rm -f data/input/data.csv.2
	wget -i input_url.txt -P data/input --content-disposition --trust-server-names


