import csv
import itertools
import urllib2

import tangible.scales
import tangible.shapes
import tangible.backends.openscad

DATA_URL = 'http://data.stadt-zuerich.ch/ogd.qWLD3E1.link'
ENCODING = 'iso-8859-15'

YEAR_KEY = 'Ereignisjahr'
QUARTER_KEY = 'Stadtquartier (historisch) (Num)'
BIRTHS_KEY = 'Anzahl Geburten (wirtschaftlich)'


if __name__ == '__main__':
    # Download data
    response = urllib2.urlopen(DATA_URL)
    lines = (line.decode(ENCODING).encode('utf8') for line in response)
    reader = csv.DictReader(lines)
    csv_data = list(reader)

    # Get list of years, quarters and births
    years = {int(d[YEAR_KEY]) for d in csv_data}
    quarters = {int(d[QUARTER_KEY]) for d in csv_data}

    # Prepare data
    data_dict = {year: {quarter: 0 for quarter in quarters} for year in years}
    for row in csv_data:
        year = int(row[YEAR_KEY])
        quarter = int(row[QUARTER_KEY])
        births = int(row[BIRTHS_KEY])
        data_dict[year][quarter] = births

    # Normalize data
    max_births = max(int(d[BIRTHS_KEY]) for d in csv_data)
    scale = tangible.scales.linear([0, max_births], [0, 50])
    datapoints = []
    for year, quarter_dict in sorted(data_dict.items()):
        births = [b for _, b in sorted(quarter_dict.items())]
        datapoints.append([value or 1 for value in map(scale, births)])

    # Create shape
    vis = tangible.shapes.bars.BarsND(datapoints, bar_width=4, bar_depth=4)

    # Render OpenSCAD code
    code = vis.render(backend=tangible.backends.openscad.OpenScadBackend)
    print(code)
