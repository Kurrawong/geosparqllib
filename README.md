# geosparqllib

A Python functions library for working with GeoSPARQL data.

This Python library contains a series of functions for creating, using and otherwise working with GeoSPARQL RDF data.

Common tasks handled by this library are:

* creating GeoSPARQL data from other spatial data
* ...

## Installation

This library is [available on PyPI](https://pypi.org/project/geosparqllib/) so can be installed using PIP:

```
pip install geosparqllib
```

or Poetry:

```
poetry add geosparqllib
```

## Use

Here's an example of using the `make_geometry()` function:

```python
from geosparqllib import make_geometry

j = """
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon", 
        "coordinates": [
          [ 
            [0, 0], 
            [1, 0], 
            [1, 1], 
            [0, 1], 
            [0, 0] 
          ]
        ]
      }
    }
    """
f = "http://example.com/f/1"
geom, bn = make_geometry(f, j)
print(geom.serialize(format="longturtle"))
```
returns:
```
PREFIX geo: <http://www.opengis.net/ont/geosparql#>

<http://example.com/f/1>
    geo:hasGeometry
        [
            a geo:Geometry ;
            geo:asWKT "POLYGON ((0 0, 1 0, 1 1, 0 1, 0 0))"^^geo:wktLiteral ;
        ] ;
.
```

## License

[BSD- 3-Clause](https://opensource.org/license/BSD-3-clause) (and [in RDF](https://purl.org/NET/rdflicense/BSD3.0)).


## Contact

Developer:

*Nicholas Car*  
[KurrawongAI](https://kurrawong.ai)  
<nick@kurrawong.ai>




## Admin

### Useful build commands

```
~$ poetry run pytest
# update version in pyproject.toml
~$ git commit -am "new version x.x.x"
~$ git tag x.x.x
~$ git push --tags
~$ poetry build
~$ poetry publish
```