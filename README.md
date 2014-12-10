# Zürich Geburtenrate Visualisierung

Dies ist eine druckbare 3D Visualisierung der Geburten pro Quartier in Zürich seit 1993.

Die Visualisierung wird mit
[Tangible](https://tangible.readthedocs.org://github.com/dbrgn/tangible/) und
[OpenSCAD](http://www.openscad.org/) gerendert.

Datenquelle: https://www.stadt-zuerich.ch/portal/de/index/ogd/daten/bev_geburten_herkunft_geschlecht_geburtenrate_seit-1934.html

## 3D Modell neu generieren

Abhängigkeiten installieren

    $ apt-get install openscad
    $ pip install tangible

3D Modell generieren

    $ python2 visualize.py > births.scad

3D Modell rendern

    $ openscad births.scad

Von OpenSCAD kann das Modell nun als .stl exportiert werden.
