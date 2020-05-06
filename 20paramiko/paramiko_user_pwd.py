import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname='192.168.164.134', port=22, username='root', password='root')
stdin, stdout, stderr = ssh.exec_command('echo `date` && ls -ltr')
print(stdout.read().decode('utf-8'))

returncode = stdout.channel.recv_exit_status()
print('returncode:',returncode)
ssh.close()