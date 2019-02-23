#!/usr/bin/python3

import requests
import shutil

reqobj = requests.get('http://192.168.1.56:8080/shot.jpg', stream=True)
if reqobj.status_code == 200:
    with open("/home/pi/image.jpg", 'wb') as f:
        reqobj.raw.decode_content = True
        shutil.copyfileobj(reqobj.raw, f)
        f.close()
        
        