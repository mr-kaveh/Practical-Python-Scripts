import psutil
import time

# Set the threshold for disk space usage (in percentage)
threshold = 90

while True:
    disk_usage = psutil.disk_usage('/')  # Monitor the root directory

    # Calculate the disk usage percentage
    disk_usage_percent = disk_usage.percent

    print(f"Disk Space Usage: {disk_usage_percent:.2f}%")

    # Check if disk space usage exceeds the threshold
    if disk_usage_percent >= threshold:
        print("Disk space usage exceeds the threshold!")
        # You can add your own logic here, such as sending an alert

    # Sleep for a specified interval (e.g., 5 minutes)
    time.sleep(300)  # 300 seconds = 5 minutes
