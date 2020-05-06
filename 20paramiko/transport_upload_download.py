import paramiko
import os

trans = paramiko.Transport(('192.168.164.134', 22))
trans.connect(username='root', password='root')

ssh = paramiko.SSHClient()
ssh._transport = trans

stdin, stdout, stderr = ssh.exec_command('echo `date` && df -hl')
print(stdout.read().decode('utf-8'))

sftp = paramiko.SFTPClient.from_transport(trans)
sftp.put(localpath='./transport_upload_download.py', remotepath='/tmp/transprot_upload_download_tmp.py')
sftp.get(localpath='./transport_upload_download_1.py', remotepath='/tmp/download_tmp.py')

stdin, stdout, stderr = ssh.exec_command('ls -ltr /tmp')
print(stdout.read().decode('utf-8'))