#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Funciones geográficas auxiliares.

Example:
    from georef import add_unidades_territoriales_to_df
    df_new = add_unidades_territoriales_to_df(df, "latitud", "longitud")
"""

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import with_statement
import requests
import pandas as pd
import os


def get_unidades_territoriales(latitud, longitud):
    """Devuelve las unidades territoriales que contienen al punto de coords.

    Example:
        >>> get_unidades_territoriales(-40, -64)
        >>> {
                'departamento_id': '62028',
                'departamento_nombre': 'Conesa',
                'municipio_id': None,
                'municipio_nombre': None,
                'provincia_id': '62',
                'provincia_nombre': 'Río Negro',
                'latitud': -40,
                'longitud': -64
            }
    """

    base_call = "https://apis.datos.gob.ar/georef/api/ubicacion?lat={}&lon={}&aplanar"
    print("Consultando lat: {}, lon: {}".format(latitud, longitud))
    api_result = requests.get(base_call.format(latitud, longitud)).json()
    result_parsed = api_result["ubicacion"]

    # conserva las coordenadas solicitadas originales
    result_parsed["latitud"] = latitud
    result_parsed["longitud"] = longitud
    del result_parsed["lat"]
    del result_parsed["lon"]

    return result_parsed


def add_unidades_territoriales_to_df(
        df, lat_col="latitud", lon_col="longitud"):
    """Agrega unidades territoriales a un DataFrame con coordenadas.

    Example:
        >>> add_unidades_territoriales_to_df(df, "latitud", "longitud")

    Args:
        df (pandas.DataFrame): Un dataframe con columnas latitud y longitud.
        lat_col (str): Nombre de la columna que tiene latitud.
        lon_col (str): Nombre de la columna que tiene longitud.
    """

    # genera serie con todas las respuestas de la API Georef
    series_unidades_territoriales = df.apply(
        lambda row: get_unidades_territoriales(row[lat_col], row[lon_col]),
        axis=1
    )

    # convierte las respuestas a un DataFrame
    df_unidades_territoriales = pd.DataFrame(
        list(series_unidades_territoriales))

    # mergea las respuestas usando las coordenadas en común
    df_merged = df.merge(
        df_unidades_territoriales,
        left_on=[lat_col, lon_col],
        right_on=["latitud", "longitud"]
    )

    return df_merged
