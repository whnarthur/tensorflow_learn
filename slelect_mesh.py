import shapefile  # 使用pyshp库

file = shapefile.Reader("F:/2/L44F010041/AdminArea.shp")
shapes = file.shapes()

# <editor-fold desc="读取元数据">
print(file.shapeType)  # 输出shp类型
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
print(file.bbox)  # 输出shp的范围
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
for index in range(len(shapes)):
    geometry = shapes[index]
    print(geometry.shapeType)
    print(geometry.points)

