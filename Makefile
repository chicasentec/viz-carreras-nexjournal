.PHONY: download_inputs

download_inputs :
	python download.py

clean:
	rm -rf data/input/alumnos.csv
	rm -rf data/input/carreras.csv
	rm -rf data/input/universidades.csv
