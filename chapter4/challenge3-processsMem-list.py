# utilizes lists to keep the processes that are using more than 100MB memory on a linux system

import psutil

def get_processes_with_high_memory_usage(threshold_memory_mb=500):
    high_memory_processes = []

    for process in psutil.process_iter(['pid', 'name', 'memory_info']):
        process_info = process.info
        process_pid = process_info['pid']
        process_name = process_info['name']
        process_memory_mb = process_info['memory_info'].rss / (1024 * 1024)  # Convert to MB

        if process_memory_mb > threshold_memory_mb:
            high_memory_processes.append({
                'pid': process_pid,
                'name': process_name,
                'memory_mb': process_memory_mb
            })

    return high_memory_processes

def main():
    threshold_memory_mb = 100
    high_memory_processes = get_processes_with_high_memory_usage(threshold_memory_mb)

    if high_memory_processes:
        print(f"Processes using more than {threshold_memory_mb}MB memory:")
        for process in high_memory_processes:
            print(f"PID: {process['pid']}, Name: {process['name']}, Memory: {process['memory_mb']:.2f}MB")
    else:
        print(f"No processes found using more than {threshold_memory_mb}MB memory.")

if __name__ == "__main__":
    main()
