import subprocess
import time as t

while(True):
    cmd = subprocess.run(['ping','-c', '1', '8.8.8.8'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    while (cmd.returncode == 0):
        print('Network is connected!')
        t.sleep(5)
        continue
    else:
        print('Network is disconnected!')
        t.sleep(5)
