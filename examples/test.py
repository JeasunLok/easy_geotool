import sys
print(sys.executable)

import easy_geotool.io.raster as egtior

input_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\demo1.tif"
output_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\demo1.shp"

example_tif = egtior.read_tif(input_path)
print(example_tif)