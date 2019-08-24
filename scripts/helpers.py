#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Funciones auxiliares para compactar el notebook."""

import pkg_resources
import pandas as pd
import numpy as np


def read_csv(filename, **kwargs):
    """Lee CSVs del repositorio a un DataFrame."""
    path = pkg_resources.resource_filename(
        'data', 'output/{}'.format(filename)
    )
    return pd.read_csv(path, **kwargs)


def format_pct(value):
    if pd.notnull(value):
        return round((value * 100), 1)
    else:
        return value


def get_bins(min_value, max_value, bins_num=5):
    step = (max_value - min_value) / bins_num
    bins = list(np.arange(min_value, max_value, step))
    bins.append(max_value)
    return bins
