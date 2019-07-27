import folium

def crear_marker(mapa, lat, lon, titulo, items):
    """ Pone un marker con tooltip en el mapa.

    Args:
        lat (float): latitud
        lon (float): longuitud
        titulo (str): titutlo del tooltip
        items (list): lista de strings
        
    """
    
    popup = """<h5>{}</h5>
<i>areas tematicas</i>
<ul>
<li>{}</li>
</ul>""".format(titulo, "</li><li>".join(items))
    tooltip = 'Más información!'
    folium.Marker([lat,lon], popup=popup, tooltip=tooltip).add_to(mapa)