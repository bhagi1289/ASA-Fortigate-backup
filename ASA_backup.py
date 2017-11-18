from datetime import datetime
import paramiko
import time

host_ip = ''#IP
login_username = ''#user Name
login_password = ''#Password
enable_password = ''#Enable password
 
client_pre=paramiko.SSHClient()
client_pre.load_system_host_keys()
client_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_pre.connect(host_ip, username=login_username , password=login_password, look_for_keys=False, allow_agent=False)

client=client_pre.invoke_shell()
time.sleep(2)
output=client.recv(65535)
print (output.splitlines())

client.send('enable\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send(enable_password + '\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send('terminal pager 0\n')
time.sleep(2)
output=client.recv(65535)
print(output.splitlines())

client.send('more system:running-config\n')
time.sleep(100)
version_info = ""
output = " "

now = datetime.now()
backup_time = now.strftime("%Y-%m-%d")
fd = open("backup_"+host_ip+"_"+backup_time+".log","w")

while client.recv_ready():
 output = client.recv(65535)
 version_info += output.decode('UTF-8')

fd.write(version_info)
print("File Created")
client.close()
client_pre.close()

raw_input()