from geosparqllib import *
from rdflib.compare import to_isomorphic


def test_make_geometry_formats():
    # make Geometry from a Shapely Polygon
    poly = Polygon(((112.76, -43.77), (153.80, -43.77), (153.80, -9.92), (112.76, -9.92), (112.76, -43.77)))
    ex1, bn1 = make_geometry(poly, URIRef("http://example.com/feature/1"), name="bounding box")

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
    ex2, bn2 = make_geometry(gj, URIRef("http://example.com/feature/1"), name="bounding box")

    assert to_isomorphic(ex1) == to_isomorphic(ex2)


def test_make_geometry_nofeature():
    # make Geometry from a Shapely Polygon
    poly = Polygon(((112.76, -43.77), (153.80, -43.77), (153.80, -9.92), (112.76, -9.92), (112.76, -43.77)))
    ex1, bn1 = make_geometry(poly)

    compare = Graph().parse(
        data="""
        PREFIX geo: <http://www.opengis.net/ont/geosparql#>
        
        []    a geo:Geometry ;
        geo:asWKT "POLYGON ((112.76 -43.77, 153.8 -43.77, 153.8 -9.92, 112.76 -9.92, 112.76 -43.77))"^^geo:wktLiteral ;
        .""",
        format="turtle"
    )

    assert to_isomorphic(ex1) == to_isomorphic(compare)
