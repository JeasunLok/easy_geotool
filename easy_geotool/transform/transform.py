import geopandas as gpd
import rasterio
from rasterio.features import rasterize
from rasterio.transform import from_bounds
from pyproj import CRS

def vector_to_raster(vector_path, raster_path, pixel_size=10, mode="constant", fill_value=0, burn_value=1, field_name=None):
    """
    将矢量数据转换为栅格数据，支持地理坐标系的转换，以保证分辨率为米，并根据模式选择栅格值。

    参数：
    - vector_path: 矢量数据文件路径 (.shp)
    - raster_path: 输出栅格文件路径 (.tif)
    - pixel_size: 像素大小（米为单位）
    - mode: 栅格填充值模式 ("constant" 或 "field")
    - fill_value: 栅格中非矢量区域的填充值（常量模式）
    - burn_value: 栅格中矢量区域的填充值（常量模式）
    - field_name: 在 "field" 模式下用于填充栅格的字段名
    """
    # 读取矢量数据
    vector_data = gpd.read_file(vector_path)
    crs = vector_data.crs  # 获取矢量的原始坐标系
    
    # 如果是地理坐标系（例如 WGS84），转换为一个适当的投影坐标系
    if not crs.is_projected:
        projected_crs = CRS.from_epsg(3857)  # 使用 Web Mercator 作为投影示例
        vector_data = vector_data.to_crs(projected_crs)
        print(f"坐标系从地理坐标系 {crs} 转换为投影坐标系 {projected_crs}")
    else:
        projected_crs = crs

    # 获取矢量边界和转换矩阵
    minx, miny, maxx, maxy = vector_data.total_bounds
    width = int((maxx - minx) / pixel_size)
    height = int((maxy - miny) / pixel_size)
    
    # 创建栅格转换矩阵
    transform = from_bounds(minx, miny, maxx, maxy, width, height)

    # 根据模式设置填充值
    if mode == "constant":
        shapes = [(geom, burn_value) for geom in vector_data.geometry]
    elif mode == "field" and field_name is not None and field_name in vector_data.columns:
        shapes = [(geom, value) for geom, value in zip(vector_data.geometry, vector_data[field_name])]
    else:
        raise ValueError("在 'field' 模式下，必须提供有效的 field_name 参数")

    # 使用 rasterize 生成栅格
    raster_data = rasterize(
        shapes,
        out_shape=(height, width),
        fill=fill_value,
        transform=transform,
        dtype='float32'
    )

    # 保存栅格文件，使用原始矢量的坐标系
    with rasterio.open(
        raster_path,
        'w',
        driver='GTiff',
        height=height,
        width=width,
        count=1,
        dtype=raster_data.dtype,
        crs=crs,  # 保持原始坐标系
        transform=transform
    ) as dst:
        dst.write(raster_data, 1)

    print(f"矢量数据已成功转换为栅格数据并保存到 {raster_path}")
