import subprocess
cmd = ['uname', '-a']
proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

o, e = proc.communicate()

print(f"Output: {o.decode('ascii')}")
print(f"Error: {e.decode('ascii')}")
print(f"code: {str(proc.returncode)}")

if(o.decode('ascii').find('Linux') != -1):
    print('Linuxx')
else:
    print('not Linux')