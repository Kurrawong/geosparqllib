from typing import Optional, Union
from rdflib import Graph, URIRef, Literal, BNode
from rdflib.namespace import GEO, RDF, SDO
from shapely import Point, Polygon, to_wkt, from_geojson


def make_geometry(
        feature_iri: URIRef,
        coordinates: Union[Point, Polygon, str],
        name: Optional[str] = None
) -> Graph:
    g = Graph()
    geom = BNode()
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
        raise TypeError("You must supply coordinates eitehr as a Shapely Point or Polygon or a WKT or GeoJSON string")

    g.add((geom, GEO.asWKT, Literal(wkt, datatype=GEO.wktLiteral)))
    if name is not None:
        g.add((geom, SDO.name, Literal(name)))

    return g
