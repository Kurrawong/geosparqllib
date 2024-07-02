from typing import Optional, Union
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import GEO, RDF, SDO
from shapely import Point, Polygon, to_wkt, from_geojson


def make_geometry(
        coordinates: Union[Point, Polygon, str],
        feature_iri: Optional[URIRef] = None,
        name: Optional[str] = None
) -> (Graph, BNode):
    """This function accepts coordinates in several forms, an optional Feature IRI and optional name and returns
    a Graph containing a Geometry and the node ID (Blank Node) of the Geometry"""
    g = Graph()
    geom = BNode()
    if feature_iri is not None:
        g.add((feature_iri, GEO.hasGeometry, geom))
    g.add((geom, RDF.type, GEO.Geometry))
    wkt = None
    if type(coordinates) in [Point, Polygon]:
        wkt = to_wkt(coordinates)
    elif type(coordinates) == str:
        if coordinates.strip().startswith(("POINT", "POLYGON")):
            wkt = coordinates
        elif coordinates.strip().startswith(("{", "[")):
            wkt = to_wkt(from_geojson(coordinates))
    else:
        raise TypeError("You must supply coordinates either as a Shapely Point or Polygon or a WKT or GeoJSON string")

    g.add((geom, GEO.asWKT, Literal(wkt, datatype=GEO.wktLiteral)))
    if name is not None:
        g.add((geom, SDO.name, Literal(name)))

    return g, geom
