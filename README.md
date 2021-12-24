# shp2geojson
- this is a script to convert shp file to geojson

## what is shp
- shp is a extention developed by ESRI

## composition of shp file 
|no|extention|explation|mandatory|
|---|---|---|---|
|1|shp|a main format |✔|
|2|shx|a index format |✔|
|3|dbf|dbase|✔|
|4|sbn|index|❌|
|5|sbx|create index in shp field|❌|
|6|pri|lcoation|❌|
|7|cpg|language|❌|
|8|qix|quard tree index|❌|

## requirement
- python3
- libarary pyshp

## how to
### install library
- pip install pyshp

### use
- python shp2geojson.py -d yourShpDirectory

### help
- python shp2geojson.py --help

## done
now you could convert to geojson !!
