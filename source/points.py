# points.py
# @author Quentin Goss [gossq@my.erau.edu]
import math
from shapely import wkb

def point_line_distance_2d(point,seg_start,seg_end):
        # Distance of a point to a line segment
        #
        # @param point : [float,float]
        #   x,y coordinate of point
        # @param seg_start : (float,float)
        #   x,y coordinate of segment start
        # @param seg_end : (float,float)
        #   x,y coordinate of segment end
        #
        # @return float
        #   Distance of point to line segment 
        x0,y0 = (point.x,point.y)
        x1,y1 = seg_start
        x2,y2 = seg_end
        return abs((x2-x1)*(y1-y0)-(x1-x0)*(y2-y1))/math.sqrt((x2-x1)**2+(y2-y1)**2)


def point_shape_distance_2d(point,shape):
    # Distance of a point to the nearest edge of a shape
    #
    # @param point : [float,float]
    #   x,y coordinate of point
    # @param shape : [(x,y),(x,y),...]
    #   Shape as a list of (x,y) coordinate pairs
    # 
    # @return float
    #   Distance of point to the nearest edge of shape.
    segments = [[shape.coords[i-1],shape.coords[i]] for i in range(1,len(shape.coords))]
    distances = [point_line_distance_2d(point,seg[0],seg[1]) for seg in segments]
    return min(distances)


def shape_to_linestring(shape):
    # Generates a linestring from a shape
    # 
    # @param shape : [(x,y),(x,y),...]
    #   Shape as a list of (x,y) coordinate pairs
    #
    # @return str
    #   linestring
    msg = "LINESTRING(%f %f" % (shape[0][0],shape[0][1])
    for xy in shape[1:]:
        msg += ",%f %f" % (xy[0],xy[1])
    return "%s)" % msg

def linestring_to_shape(linestring):
    # Generates a shape from a linestring
    #
    # @param linestring : str
    #   PostGIS linestring
    # 
    # @return [(x,y),(x,y),...]
    #   Shape
    shape = []
    linestring = linestring[linestring.index('(')+1:-1]
    for xy in linestring.split(","):
        x,y = xy.split(" ")
        shape.append(  (float(x),float(y))  )
    return shape


def wkb_decode(geom):
    # Decodes a PostGIS wkb hex encoded geom string
    #
    # @param geom : str
    #   Hex econded wkb geometry string
    #
    # @return decoded type
    return wkb.loads(geom,hex=True)


# Volusia EPSG  2236
# FDOT    EPSG 26917
