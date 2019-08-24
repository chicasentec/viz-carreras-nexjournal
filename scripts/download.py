import requests
import os


def download_to_file(url, path):
    print('Descargando {} como {}'.format(url, path))
    response = requests.get(url)

    with open(path, 'wb') as f:
        f.write(response.content)


def main():
    download_to_file(
        'https://docs.google.com/spreadsheets/d/1zMbFfT1MPhmjHjm5zfwPUBqaHxJRU7tD5mOxHFht_M0/gviz/tq?tqx=out:csv&sheet=alumnos', 'data/input/alumnos.csv')
    download_to_file('https://docs.google.com/spreadsheets/d/1zMbFfT1MPhmjHjm5zfwPUBqaHxJRU7tD5mOxHFht_M0/gviz/tq?tqx=out:csv&sheet=universidades',
                     'data/input/universidades.csv')
    download_to_file(
        'https://docs.google.com/spreadsheets/d/1zMbFfT1MPhmjHjm5zfwPUBqaHxJRU7tD5mOxHFht_M0/gviz/tq?tqx=out:csv&sheet=carreras', 'data/input/carreras.csv')

if __name__ == '__main__':
    main()
