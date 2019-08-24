.PHONY: download_inputs

NOTEBOOK ?=./visualizaciones-next-journal.ipynb
REPORT ?=./reports/visualizaciones-next-journal.html

download_inputs :
	python download.py

clean:
	rm -rf data/input/alumnos.csv
	rm -rf data/input/carreras.csv
	rm -rf data/input/universidades.csv

clean_white_spaces:
	python scripts/shrink_file.py --file '$(REPORT)'

report:
	jupyter nbconvert --execute --ExecutePreprocessor.timeout=-1 --to notebook --inplace --output-dir ./reports $(NOTEBOOK)
	jupyter nbconvert  --to html --output-dir ./reports $(NOTEBOOK)
	$(MAKE) clean_white_spaces REPORT=$(REPORT)
