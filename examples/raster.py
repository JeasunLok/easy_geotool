import sys
import matplotlib.pyplot as plt
import numpy as np
from skimage.exposure import equalize_hist
sys.path.append(r'D:\Workspace/project/easy_geotool/easy_geotool')

from easy_geotool.io.raster import read_tif, write_tif
from easy_geotool.transform.transform import raster_to_points, raster_to_lines, raster_to_polygons
from easy_geotool.raster.display import display_raster_image

input_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\demo1.tif"
input_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\440000GD_L5_TM_2006_R1C1.TIF"
# output_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\demo1.shp"

# example_tif = read_tif(input_path)
# print(example_tif)

# example_tif_data = example_tif[0]
# im_geotrans, im_proj, cols, rows = example_tif[1], example_tif[2], example_tif[3], example_tif[4]
# write_tif(output_path, example_tif_data, im_geotrans, im_proj)


# raster_to_polygons(input_path, output_path, single_polygon=True)

# 读取遥感图像进行显示
input_path = r"D:\Workspace\project\easy_geotool\easy_geotool\examples\data\example.tif"
nodata_value = [0, 255]  # 假设 NoData 值为 0、255
example_tif = read_tif(input_path)
rgb_bands = [3, 2, 1] 
example_tif_data = example_tif[0]
single_band = None
im_geotrans, im_proj, cols, rows = example_tif[1], example_tif[2], example_tif[3], example_tif[4]
data = display_raster_image(example_tif_data, rgb_bands=rgb_bands, single_band=single_band, nodata_value=nodata_value, equalize=True)
