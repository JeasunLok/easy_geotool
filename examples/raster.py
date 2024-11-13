import sys
sys.path.append(r'E:\project\ljs\easy_geotool\easy_geotool')

from easy_geotool.io.raster import read_tif, write_tif

data_tif = r"E:\project\ljs\easy_geotool\easy_geotool\examples\data\gd_to_all.tif"
example_tif = read_tif(data_tif)
print(example_tif)

example_tif_data = example_tif[0]
im_geotrans, im_proj, cols, rows = example_tif[1], example_tif[2], example_tif[3], example_tif[4]
write_tif(r"E:\project\ljs\easy_geotool\easy_geotool\examples\data\gd_to_all_write.tif", example_tif_data, im_geotrans, im_proj)


