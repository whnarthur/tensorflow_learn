import shapefile  # 使用pyshp库
import os
import json


def gen_geosjon(geometry):
    json_data = {}
    geo_geometry = {}
    coords = []
    for point in geometry.points:
        geo_point = []
        geo_point.append(point[0])
        geo_point.append(point[1])
        coords.append(geo_point)
    geo_geometry["coordinates"] = coords
    geo_geometry["type"] = "LineString"
    json_data["geometry"] = geo_geometry
    return json_data


if __name__ == "__main__":
    path = '/Users/weihainan/Documents/waibao/2'
    all_shape_files = []
    for dirpath, dirnames, filenames in os.walk(path):
        for file in filenames:
            fullpath = os.path.join(dirpath, file)
            if fullpath.find("AdminArea.shp") != -1:
                all_shape_files.append(fullpath)

    features = []
    for shape_file in all_shape_files:
        file = shapefile.Reader(shape_file)
        shapes = file.shapes()

        # <editor-fold desc="读取元数据">
        # print(file.shapeType)  # 输出shp类型
        '''
        NULL = 0
        POINT = 1
        POLYLINE = 3
        POLYGON = 5
        MULTIPOINT = 8
        POINTZ = 11
        POLYLINEZ = 13
        POLYGONZ = 15
        MULTIPOINTZ = 18
        POINTM = 21
        POLYLINEM = 23
        POLYGONM = 25
        MULTIPOINTM = 28
        MULTIPATCH = 31
        '''
        # print(file.bbox)  # 输出shp的范围
        # </editor-fold>
        # print(shapes[1].parts)
        # print(len(shapes))  # 输出要素数量
        # print(file.numRecords)  # 输出要素数量
        # print(file.records())  # 输出所有属性表

        # <editor-fold desc="输出字段名称和字段类型">
        '''
        字段类型：此列索引处的数据类型。类型可以是：
        “C”：字符，文字。
        “N”：数字，带或不带小数。
        “F”：浮动（与“N”相同）。
        “L”：逻辑，表示布尔值True / False值。
        “D”：日期。
        “M”：备忘录，在GIS中没有意义，而是xbase规范的一部分。
        '''
        # fields = file.fields
        # print(fields)
        # </editor-fold>

        # <editor-fold desc="输出几何信息">
        if len(shapes) > 0:
            geometry = shapes[0]
            # print(geometry.shapeType)
            # print(geometry.points)
            json_data = gen_geosjon(geometry)
            prop = {}
            prop["file_path"] = shape_file
            json_data["properties"] = prop
            json_data["type"] = "Feature"
            # print(json_data)
            features.append(json_data)

    geojson_res = {}
    geojson_res["features"] = features
    geojson_res["type"] = "FeatureCollection"

    with open("output.geojson", "w") as fp:
        fp.write(json.dumps(geojson_res, indent=4))
