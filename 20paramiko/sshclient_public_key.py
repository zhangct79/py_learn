import paramiko

pkey = paramiko.RSAKey.from_private_key_file('./id_rsa')
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
ssh.connect(hostname='192.168.164.131', port=22, username='root', pkey=pkey)

stdid,stdout,stderr = ssh.exec_command('echo `date` && df -hl && cat /etc/hostname')
print(stdout.read().decode('utf-8'))
ssh.close()