import folium


def crear_marker(mapa, lat, lon, titulo,
                 estudiantes_total, estudiantes_mujeres_pct, items):
    """ Pone un marker con tooltip en el mapa.

    Args:
        lat (float): latitud
        lon (float): longuitud
        titulo (str): titutlo del tooltip
        items (list): lista de strings

    """
    try:
        estudiantes_total = int(estudiantes_total)
    except Exception as e:
        estudiantes = None

    popup_html = """<h5>{}</h5>
<p>
Estudiantes 2017: {}
<br>
Mujeres 2017 (%): {:.1%}
</p>
<ul>
<li>{}</li>
</ul>""".format(
        titulo, estudiantes_total,
        estudiantes_mujeres_pct, "</li><li>".join(items)
    )
    tooltip = 'Click para más información!'
    popup = folium.Popup(popup_html, max_width=500, min_width=300)
    folium.Marker([lat, lon], popup=popup, tooltip=tooltip).add_to(mapa)


def add_label(folium_map, label, latitude, longitude, font_size=8):
    """Agrega un texto en determinadas coordenadas en un mapa de folium."""

    folium.map.Marker(
        [latitude, longitude],
        icon=folium.features.DivIcon(
            html='<div style="font-size: {}pt">{}</div>'.format(font_size, label))
    ).add_to(folium_map)


def add_labels_from_column(folium_map, gdf, label_column, font_size=7):
    """Agrega textos de una columna de un GeoDataframe en centroides de las geometrías."""

    for centroid, label in zip(gdf.geometry.centroid, gdf[label_column]):
        latitude = centroid.coords[0][1]
        longitude = centroid.coords[0][0]
        add_label(folium_map, label, latitude, longitude, font_size=font_size)
