# Wolt Alert Script

## Introduction

The Wolt Alert Script is a Python script designed to monitor the online/offline status of restaurants on the Wolt food delivery platform. It periodically checks the specified URLs for changes in the specified attributes and provides notifications when a change is detected.

## Features

- Monitors the online/offline status of restaurants on Wolt.
- Sends notifications and plays a sound when a change in status is detected.
- Provides real-time updates on the status of multiple restaurants.
- User-defined URLs and attributes for flexible monitoring.

## Prerequisites

- Python 3.x installed on your system.
- Required libraries: `requests`, `beautifulsoup4`.

You can install the required libraries using the following command:

```bash
pip install requests beautifulsoup4
```

## Usage

1. Clone this repository or download the script file.
2. Run the script using the command:
   ```bash
   python wolt_alert_script.py
   ```
3. Enter the desired restauratns URL and hit ENTER
4. The script will start monitoring the specified URLs at the defined interval and provide notifications whenever there's a change in status.

## Customization
- You can adjust the check_interval variable to set the time interval (in seconds) between checks.
- The script uses the winsound library to play a sound when a change is detected. If you're not using Windows, you might need to replace this with a different sound library compatible with your operating system.

## Disclaimer
This script is for educational and personal use only. Use it responsibly and in accordance with Wolt's terms of service.
