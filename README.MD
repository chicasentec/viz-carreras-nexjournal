# Proyecto NextJournal

Analisis y visualizaciones de la base de datos de genero y carreras universitarias en Argentina.

## Usar el repositorio

1. Clonar o descargar repositorio
2. `pip install -e .`

### ETL - Correr solo si desean hacer cambios a los datos o trabajar con una BBDD propia

Si se desea modificar el procesamiento de los datos:

* Abrir y correr etl-next-journal.ipynb

### Visualizaciones

Para ver, usar y/o modificar las visualizaciones (sobre los datos de este repositorio ya procesados, o los datos modificados por el ETL):

* Abrir y correr visualizaciones-next-journal.ipynb

### Visualizaciones en HTML

Para generar una vista estática de las visualizaciones en HTML sin abrir el notebook:

* `make report`
