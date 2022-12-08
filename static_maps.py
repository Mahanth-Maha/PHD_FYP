import folium

class StaticMapHTMLGenerator():
    
    def __init__(self,recent_lat,recent_lon) -> None:
        self.m = folium.Map(location=[recent_lat,recent_lon], zoom_start=10)

    def test(self):
        folium.Marker([45.5236, -122.6750], popup='Portland, OR').add_to(self.m)
        folium.Marker([45.5236, -122.6623], popup='Oregon Health & Science University').add_to(self.m)
        folium.Marker([45.5215, -122.6261], popup='Lucky Labrador Brewing Company').add_to(self.m)

    def insert_mark(self,lat,lon):
        folium.Marker([lat, lon]).add_to(self.m)

    def gen_html(self,path = 'map.html'):
        """ generate an HTML map """
        self.m.save(path)
        return True
    
    def phd_fyp_html_generator(self,locs,path = 'map.html'):
        """ generate an HTML map """
        for lat, lon in locs:
            self.insert_mark(lat,lon)
        self.m.save(path)
        return True
    

