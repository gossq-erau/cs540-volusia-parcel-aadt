set OGR2OGR="E:\Program Files\PostgreSQL\13\bin\ogr2ogr"
set SHAPEFILE="E:\Python\aadt\data\aadt.shp"
set OUTPUT="E:\Python\aadt\data\aadt_volusia.shp"

%OGR2OGR% -f "ESRI Shapefile" -s_srs EPSG:26917 -t_srs EPSG:2236 %OUTPUT% %SHAPEFILE%
