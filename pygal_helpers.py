#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Funciones auxiliares para usar pygal.
"""

import os
import pygal


def df_to_pygal_line(df, height=300):
    """Genera un gráfico de líneas a partir de un DataFrame."""
    chart = pygal.Line(x_label_rotation=20, height=height)
    chart.x_labels = list(df.index)

    for col in df.columns:
        chart.add(col, list(df[col]))

    return chart


def get_pygal_html(pygal_chart_obj):
    """Convierte un gráfico de pygal en HTML."""

    html_pygal = """
   <!DOCTYPE html>
   <html>
     <head>
     <script type="text/javascript" src="http://kozea.github.com/pygal.js/javascripts/svg.jquery.js"></script>
     <script type="text/javascript" src="http://kozea.github.com/pygal.js/latest/pygal-tooltips.min.js"></script>
     <script type="text/javascript" xlink:href="https://kozea.github.io/pygal.js/2.0.x/pygal-tooltips.min.js"></script>
       <!-- ... -->
     </head>
     <body>
       <figure>
         {pygal_render}
       </figure>
     </body>
   </html>
   """

    return html_pygal.format(
        pygal_render=pygal_chart_obj.render(is_unicode=True)
    )
