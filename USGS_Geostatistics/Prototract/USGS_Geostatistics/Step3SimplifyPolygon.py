# -*- coding: utf-8 -*-
"""
Generated by ArcGIS ModelBuilder on : 2020-04-06 01:13:07
"""
import arcpy
from sys import argv


def Step3SimplifyPolygon(Simplification_Tolerance, Input_Barrier_Layers, Output_Aggregate, Output_Simplify,
                         Simplification_Algorithm="POINT_REMOVE", Minimum_Area_2_="0 Unknown",
                         Handling_Topological_Errors="RESOLVE_ERRORS",
                         Keep_collapsed_points=True):  # Step3SimplifyPolygon

    # To allow overwriting outputs change overwriteOutput option to True.
    arcpy.env.overwriteOutput = False

    # Process: Simplify Polygon (Simplify Polygon)
    output_feature_class_Pnt = \
    arcpy.SimplifyPolygon_cartography(in_features=Output_Aggregate, out_feature_class=Output_Simplify,
                                      algorithm=Simplification_Algorithm, tolerance=Simplification_Tolerance,
                                      minimum_area=Minimum_Area_2_, error_option=Handling_Topological_Errors,
                                      collapsed_point_option=Keep_collapsed_points, in_barriers=Input_Barrier_Layers)[0]


if __name__ == '__main__':
    # Global Environment settings
    with arcpy.EnvManager(
            scratchWorkspace=r"C:\Users\kjuli\PycharmProjects\USGS_Geostatistics\USGS_Geostatistics\USGS_Geostatistics.gdb",
            workspace=r"C:\Users\kjuli\PycharmProjects\USGS_Geostatistics\USGS_Geostatistics\USGS_Geostatistics.gdb"):
        Step3SimplifyPolygon(*argv[1:])
