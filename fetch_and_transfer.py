#!/usr/bin/python3

import requests
import shutil
import paramiko

reqobj = requests.get('http://192.168.1.56:8080/shot.jpg', stream=True)
if reqobj.status_code == 200:
    with open("/home/pi/image.jpg", 'wb') as f:
        reqobj.raw.decode_content = True
        shutil.copyfileobj(reqobj.raw, f)
        f.close()
        
paramiko.util.log_to_file('/tmp/catcam_transfer.log')
host = "catcam.theseymours.org"
port = 22
user = 'ec2-user'
transporter = paramiko.Transport((host,port))
rsa_key = paramiko.RSAKey.from_private_key_file('/home/pi/.ssh/catcam.pem')
transporter.connect(username=user, pkey=rsa_key)
sftp = paramiko.SFTPClient.from_transport(transporter)
localpath = '/home/pi/image.jpg'
remotepath = '/var/html/image.jpg'
sftp.put(localpath,remotepath)
sftp.close()
transporter.close()
