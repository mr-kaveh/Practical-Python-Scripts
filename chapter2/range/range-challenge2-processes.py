#ps -aux | awk ' { print $11 } '
import subprocess

lst = []

# Checkout the official Python Documentation
# https://docs.python.org/3/library/subprocess.html#

ps = subprocess.Popen(["ps", "-aux"], stdout=subprocess.PIPE) 
output = subprocess.run(["awk", "{ print $11 }"], stdin=ps.stdout, stdout=subprocess.PIPE)
lst = output.stdout.splitlines() # split the output so we can place them in a list
# The list contains bytes and needs to convert to string
# This is how => bytes_value.decode('utf-8')
for index in range(len(lst)):
    if lst[index].decode('utf-8') == "awk":
        print(F"{lst[index].decode('utf-8')} is found")

