import requests
from bs4 import BeautifulSoup
import time
import datetime
import winsound
import validators
from utils import check_ordering_paused

# Define the URLs to check and the attributes to look for in the div elements
url = input("Example: https://wolt.com/en/isr/tel-aviv/restaurant/fat-cow\nEnter WOLT URL:")
while not validators.url(url):
    print("Invalid URL. Please enter a valid WOLT URL.")
    url = input("Please enter a valid URL:")

# Define the time interval to check for changes (in seconds)
check_interval = 5
print(f"Checking every {check_interval} seconds and playing a test sound.")
winsound.Beep(500, 2000)

# Define variables to store the previous values of the div elements
prev_value = None

# Define a variable to keep track of the number of iterations
iteration_count = 0

while True:

    ordering_paused_text = check_ordering_paused(url)
    print(f"Ordering paused: {ordering_paused_text}")

    # Determine the current status for each restaurant
    value = "Ordering paused" if ordering_paused_text else "venue-online"

    # Check if the values have changed since the previous iteration
    messages = []
    if prev_value is None:
        messages.append(f"{datetime.datetime.now()} - Initial restaurant status: {value}")
    elif prev_value != value:
        messages.append(
            f"{datetime.datetime.now()} - Value has changed from {prev_value} to {value}")
        winsound.Beep(500, 2000)
    else:
        messages.append(f"{datetime.datetime.now()} - Value has not changed: {value}")

    print("\n".join(messages))

    # Update the previous value variable
    prev_value = value

    # Update the iteration count
    iteration_count += 1

    # Wait for the specified interval before checking again
    time.sleep(check_interval)