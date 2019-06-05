# ---------------------
# Coordinate Transformation function using WPS specification
# ---------------------
from osgeo import ogr
from osgeo import osr
 
def title():
    return "envelope" # title of the function
 
def abstract():
    return "A function that get the envelope of a vector geometry." # short description of the function
 
def inputs():
    return [
        ['feature', 'Input feature','The feature in the source reference system.','application/json', True]
    ]
 
def outputs():
    return [['result', 'transformed feature','5555','application/json']]
 
def execute(parameters):
    feature = parameters.get('feature')
    if (feature is not None):
        feature = feature['value']
 
    datasource = ogr.Open(feature)
    print()
    layer = datasource.GetLayer(0)
    feature = layer.GetFeature(0)
    OverijsselGeometry = feature.GetGeometryRef()
    env = OverijsselGeometry.GetEnvelope()
    print("Feature extent: x_min = %.2f x_max = %.2f y_min = %.2f y_max = %.2f" % (env[0], env[1], env[2], env[3]))
    print("Content-type: application/json")
    print()
