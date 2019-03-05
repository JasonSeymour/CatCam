#!/usr/bin/python3

import shutil
import paramiko
import subprocess
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("filename", help="Filename to process")
args = parser.parse_args()
file = args.filename


cmd = '/usr/bin/convert '
cmd += file
cmd += ' -pointsize 20 -fill red -gravity northwest -annotate +0+0 "$(date)" -resize 1920 /home/camera/image2.jpg'
subprocess.call(cmd, shell=True)

paramiko.util.log_to_file('/tmp/catcam_camera_transfer.log')
host = "catcam.theseymours.org"
port = 22
user = 'ec2-user'
transporter = paramiko.Transport((host,port))
rsa_key = paramiko.RSAKey.from_private_key_file('/home/camera/.ssh/catcam.pem')
transporter.connect(username=user, pkey=rsa_key)
sftp = paramiko.SFTPClient.from_transport(transporter)
localpath = '/home/camera/image2.jpg'
remotepath = '/var/html/image.jpg'
sftp.put(localpath,remotepath)
sftp.close()
transporter.close()

