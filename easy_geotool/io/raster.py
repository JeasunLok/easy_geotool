import numpy as np
import rasterio

# read tif
def read_tif(path):
    with rasterio.open(path) as dataset:
        im_data = dataset.read()  
        if len(im_data) == 2:  
            im_data = im_data[np.newaxis, :, :]  
        im_data = np.transpose(im_data, [1, 2, 0])  
        im_proj = dataset.crs 
        im_geotrans = dataset.transform  
        cols, rows = dataset.width, dataset.height
    return im_data, im_geotrans, im_proj, cols, rows


# write tif
def write_tif(newpath, im_data, im_geotrans, im_proj):
    if len(im_data) == 2:  
        im_data = im_data[np.newaxis, :, :]  
    bands = im_data.shape[0]
    height = im_data.shape[1]
    width = im_data.shape[2]
    datatype = im_data.dtype 

    with rasterio.open(newpath, 'w', driver='GTiff', height=height, 
                       width=width, count=bands, 
                       dtype=datatype, crs=im_proj, transform=im_geotrans) as new_dataset:
        for i in range(bands):
            new_dataset.write(im_data[i, :, :], i + 1)