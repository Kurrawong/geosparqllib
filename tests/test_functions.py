from geosparqllib import *
from rdflib.compare import to_isomorphic


def test_make_geometry():
    # make Geometry from a Shapely Polygon
    poly = Polygon(((112.76, -43.77), (153.80, -43.77), (153.80, -9.92), (112.76, -9.92), (112.76, -43.77)))
    ex1 = make_geometry(URIRef("http://example.com/feature/1"), poly, name="bounding box")

    # make Geometry from GeoJSON
    gj = """
        {
          "type": "Feature",
          "properties": {},
          "geometry": {
            "type": "Polygon", 
            "coordinates": [
              [ 
                [112.76, -43.77], 
                [153.8, -43.77], 
                [153.8, -9.92], 
                [112.76, -9.92], 
                [112.76, -43.77] 
              ]
            ]
          }
        }
        """
    ex2 = make_geometry(URIRef("http://example.com/feature/1"), gj, name="bounding box")

    assert to_isomorphic(ex1) == to_isomorphic(ex2)
