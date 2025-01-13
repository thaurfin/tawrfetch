# Tawrfetch

A minimal Python-based system info fetch tool

## Goal

The purpose of creating **Tawrfetch** was to deepen my understanding of various system-related Python libraries and to enhance my programming skills, particularly in the areas of logic building and code optimization.

## Libraries Used

- **psutil**: For retrieving system information such as memory usage, CPU statistics, and uptime.
- **platform**: To obtain information about the operating system, kernel version, and other platform-specific details.
- **socket**: For gathering hostname and IP-related information.
- **subprocess**: To handle system-level commands for fetching CPU info on Windows and macOS.
- **colorama**: For adding color to the terminal output.

## System Information Covered

- **Operating System**: Detection and display of the OS type (Windows, Linux, macOS).
- **Host and User Information**: Hostname and username.
- **Kernel Version**: Display of the current kernel version.
- **Uptime**: Time since the system was last booted.
- **Shell**: The shell currently in use.
- **Desktop Environment** (on Linux): The active desktop environment session.
- **CPU**: Information about the system's CPU, including model name.
- **Memory**: Total and used memory, in GB.

## Example Output

![Tawrfetch Screenshot](/screenshot.png)

## Installation

To install and use **Tawrfetch**, make sure you have Python 3.x installed and then install the necessary dependencies using pip:

```bash
pip install psutil colorama
```
After installation, you can run the tool by executing the Python script:

```bash
python tawrfetch.py
```
