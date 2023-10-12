import psutil
import time

#pip3 install psutil

# Set the threshold for high CPU usage (e.g., 80%)
cpu_threshold = 10

while True:
    # Get the current CPU usage
    cpu_percent = psutil.cpu_percent(interval=1)  # Check CPU usage every 1 second

    # Check if CPU usage exceeds the threshold
    if cpu_percent > cpu_threshold:
        # Perform an action when CPU usage is high (e.g., print a message)
        print(f"High CPU usage detected: {cpu_percent}%")

    # You can add more conditions and actions as needed

    # Sleep for a while to avoid constant checking
    time.sleep(5)
