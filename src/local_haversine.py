from math import sqrt
from math import atan2
from math import sin
from math import cos
from math import radians

EARTH_RADIUS=6371.0

def haversine(a, b):
    '''
    Given two points a = (x, y) and b = (x', y')
    return their haversine distance
    '''
    alat, along = [radians(i) for i in a]
    blat, blong = [radians(j) for j in b]
    dlat  = radians(blat - alat)
    dlong = radians(blong - along)
    alpha = sin(dlat / 2.0) ** 2\
          + cos(alat) * cos(blat)\
          + sin(dlong / 2.0) ** 2
    c = 2 * atan2(sqrt(alpha), sqrt(1 - alpha))
    return c * EARTH_RADIUS