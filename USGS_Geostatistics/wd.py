import arcpy
import re

params = arcpy.GetParameterInfo("Union_analysis")

test = str(help(arcpy.Union_analysis))

left = "     "
right = "     "
print(test[test.index(left)+len(left):test.index(right)])

from ipywidgets import interact

@interact_manual(slow_function,b = widgets.Text(
    value="None",
    description='Linear Unit Value',
    style=dict(description_width='initial'),
    disabled=False
), c = widgets.Dropdown(
    options=['None','Centimeters','DecimalDegrees', 'Decimeters', 'Feet', 'Inches', 'Kilometers',
             'Meters','Miles','Millimeters','NauticalMiles','Points', 'Unknown', 'Yards'],
    value='None',
    description='Linear Unit Type:',
    style=dict(description_width='initial'),
    disabled=False
))