import platform

def detect_and_act_on_os():
    os_name = platform.system()
    match os_name:
        case "Linux":
            print("Linux OS detected. Running Linux-specific code.")
            # Add Linux-specific code here
        case "Windows":
            print("Windows OS detected. Running Windows-specific code.")
            # Add Windows-specific code here
        case "Darwin":
            print("macOS (Darwin) detected. Running macOS-specific code.")
            # Add macOS-specific code here
        case _ as default:
            print(f"Unknown OS detected: {os_name}. Running default code.")
            # Add code for other or unknown OS here

detect_and_act_on_os()
