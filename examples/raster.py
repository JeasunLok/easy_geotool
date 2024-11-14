import sys
sys.path.append(r'D:\Workspace/project/easy_geotool/easy_geotool')

from easy_geotool.io.raster import read_tif, write_tif
from easy_geotool.transform.transform import raster_to_points, raster_to_lines, raster_to_polygons

input_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\demo1.tif"
output_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\demo1.shp"

# example_tif = read_tif(input_path)
# print(example_tif)

# example_tif_data = example_tif[0]
# im_geotrans, im_proj, cols, rows = example_tif[1], example_tif[2], example_tif[3], example_tif[4]
# write_tif(output_path, example_tif_data, im_geotrans, im_proj)


raster_to_polygons(input_path, output_path, single_polygon=True)

