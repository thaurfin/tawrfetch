#!/usr/bin/env python3
# This shebang allows the script to be executed directly from the command line if it has execution permissions.
# It ensures that the script is executed with Python 3.

import os
# 'os' module provides functions to interact with the operating system, such as getting the current user's login name and hostname.
import platform
# 'platform' module is used to access information about the operating system (OS), such as its name and version.
import socket
# 'socket' module is used for networking, here it retrieves the local machine's hostname.
import psutil
# 'psutil' module allows for retrieving system and process information, like memory usage and uptime.
import subprocess
# 'subprocess' module is used to execute system commands and retrieve their output, here it helps fetch CPU info.
from colorama import Fore, Back, init
# 'colorama' is used to print colored text to the terminal. 'Fore' is for text color, 'Back' is for background color.
# 'init()' initializes colorama for cross-platform compatibility.
import shutil
# 'shutil' module provides functions to interact with the file system, here it is used to get the terminal width.

# ASCII art to display
# This is a string containing ASCII art that will be displayed at the beginning of the script.
# It serves as a visual element or "banner" when the script is run.
ascii_art = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣴⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣦⡀⠀
⠀⢸⣿⣧⣀⣀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣀⣼⣿⡧⠀
⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⠿⠁⠀
⠀⠀⠀⠀⠙⠛⠿⠿⠿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠿⠿⠿⠛⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣤⡄⠀⠀⠀⠀⠀⠀⢀⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠿⠀⠀⠀⠀⠀⠀⠿⠿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡆⠀⠀⢠⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣦⣤⡾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"""

# Initialize colorama
# This initializes the colorama module to support colored output across different operating systems,
# including Windows, which might require additional support for ANSI color codes.
init(autoreset=True)

# Functions
# The following functions are defined to gather system information.

def get_uptime(): 
    # Retrieves the system's uptime (the time since the last boot).
    
    uptime_seconds = psutil.boot_time()  # Gets the system's boot time in seconds since epoch.
    uptime_seconds = psutil.time.time() - uptime_seconds  # Current time minus boot time to get the uptime in seconds.

    # Calculate days, hours, and minutes from the total uptime in seconds.
    days = uptime_seconds // (24 * 3600)  # Days
    hours = (uptime_seconds % (24 * 3600)) // 3600  # Hours
    minutes = (uptime_seconds % 3600) // 60  # Minutes

    return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes"  # Return uptime in a readable format.

def get_cpu_info():
    # Retrieves the CPU information based on the platform (Windows, Linux, Darwin).
    
    system_platform = platform.system()  # Get the current operating system name.
    try:
        if system_platform == "Windows":
            # On Windows, use 'wmic' to fetch the CPU model.
            cpu_info = subprocess.check_output('wmic cpu get caption', shell=True)
            return cpu_info.decode('utf-8').split('\n')[1].strip()  # Parse the output to return the CPU model name.

        elif system_platform == "Linux":
            # On Linux, read '/proc/cpuinfo' to get CPU information.
            with open("/proc/cpuinfo", "r") as f:
                for line in f:
                    if "model name" in line:
                        return line.split(":")[1].strip()  # Return the CPU model name.

        elif system_platform == "Darwin":
            # On macOS (Darwin), use sysctl command to get the CPU model.
            cpu_info = subprocess.check_output("sysctl -n machdep.cpu.brand_string", shell=True)
            return cpu_info.decode('utf-8').strip()  # Return the CPU model name.

    except Exception as e:
        # If an error occurs, return the error message.
        return f"Error fetching CPU info: {e}"

    return "Unknown CPU"  # If no platform matches, return a default message.

def get_memory_info():
    # Retrieves system memory usage information (total and used).
    
    memory_info = psutil.virtual_memory()  # Use psutil to get memory stats.
    total_memory = memory_info.total / (1024**3)  # Convert total memory from bytes to gigabytes.
    used_memory = memory_info.used / (1024**3)  # Convert used memory from bytes to gigabytes.

    return f"{used_memory:.2f}/{total_memory:.2f} GB"  # Return memory usage in a readable format.

def center_text(text, terminal_width):
    """ 
    Centers the provided text on the terminal by adding padding spaces on both sides.
    Splits the text by line and centers each line according to the terminal's width.
    """
    return "\n".join([line.center(terminal_width) for line in text.split('\n')])

def display_info():
    # Main function that gathers and displays system information.

    terminal_width = shutil.get_terminal_size().columns  # Get the terminal's width to center content.

    # Print the ASCII art centered in the terminal with yellow text on a black background.
    print(Back.BLACK + Fore.YELLOW + center_text(ascii_art, terminal_width))

    # Retrieve the username of the person logged into the system.
    uname = os.getlogin()

    # Retrieve the hostname of the machine.
    hname = socket.gethostname()

    # Display the user and host information, using colorama to style the output.
    print(Fore.YELLOW + f"{uname}" + Fore.BLUE + "@" + Fore.YELLOW + f"{hname}")
    print(Fore.YELLOW + "-------------------")  # Print a separator line in yellow.

    # Display various system details (OS, host, kernel version, etc.) using the colors.
    print(Fore.YELLOW + "OS:", Fore.BLUE + platform.system())
    print(Fore.YELLOW + "Host:", Fore.BLUE + hname)
    print(Fore.YELLOW + "Kernel:", Fore.BLUE + platform.uname().release)
    print(Fore.YELLOW + "Uptime:", Fore.BLUE + get_uptime())
    print(Fore.YELLOW + "Shell:", Fore.BLUE + os.environ.get('SHELL', 'N/A'))
    print(Fore.YELLOW + "CPU:", Fore.BLUE + get_cpu_info())
    print(Fore.YELLOW + "Memory:", Fore.BLUE + get_memory_info())

if __name__ == "__main__":
    # This ensures that the display_info function is executed when the script is run.
    display_info()