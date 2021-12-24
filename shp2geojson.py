import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
import sys
import shapefile
from json import dumps

def process():
    ## 디렉토리 경로
    ## output(geojson) 폴더는 dir+"_geojson"으로 생성
    dir = ""
    dash = str(sys.argv[1])
    if dash == "-d":
        dir = str(sys.argv[2])
 
    file_with_extension = [f for f in listdir(dir) if isfile(join(dir, f))]
    file_name = [os.path.splitext(f)[0] for f in file_with_extension]
    print(file_name[0])

    # read the shapefile
    for file in file_name:
        print(dir+"/"+file)
        reader = shapefile.Reader(dir+"/"+file, encoding='euc-kr')
        fields = reader.fields[1:]
        field_names = [field[0] for field in fields]
        buffer = []
        for sr in reader.shapeRecords():
            atr = dict(zip(field_names, sr.record))
            geom = sr.shape.__geo_interface__
            buffer.append(dict(type="Feature", properties=atr, geometry=geom)) 
        
        # write the GeoJSON file
        Path(dir+"_geojson").mkdir(parents=True, exist_ok=True)
        geojson = open(dir+"_geojson/"+file+".geojson", "w",encoding='UTF-8')
        geojson.write(dumps({"type": "FeatureCollection", "name":file, "features": buffer}, indent=2, ensure_ascii=False) + "\n")
        geojson.close()		


if len(sys.argv) <= 1:
    print("i need arguments\nplease command --help if you need")
	
elif len(sys.argv) == 2:
    if str(sys.argv[1]) == "--help":
        print("❓help❓\n#### command lists ####\n-d yourDirectoryPath")
elif str(sys.argv[1]) == "-d":
    process()

