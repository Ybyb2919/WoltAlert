import requests
from bs4 import BeautifulSoup
import time
import datetime
import winsound

# Define the URLs to check and the attributes to look for in the div elements
url1 = input("Example: https://wolt.com/en/isr/tel-aviv/restaurant/fat-cow\nEnter WOLT URL for restaurant 1:")
print()
div_attributes1 = {"data-test-id": "CartViewButtonInformationBlock", "data-test-value": "venue-offline"}

url2 = input("Enter URL for restaurant 2: ")
div_attributes2 = {"data-test-id": "CartViewButtonInformationBlock", "data-test-value": "venue-offline"}

# Define the time interval to check for changes (in seconds)
check_interval = 10
print(f"Checking every {check_interval} seconds and playing a test sound.")
winsound.Beep(500, 2000)

# Define variables to store the previous values of the div elements
prev_value1 = None
prev_value2 = None

# Define a variable to keep track of the number of iterations
iteration_count = 0

while True:
    # Refresh the pages every other iteration
    if iteration_count % 2 == 0:
        response1 = requests.get(url1)
        response2 = requests.get(url2)
    soup1 = BeautifulSoup(response1.content, "html.parser")
    soup2 = BeautifulSoup(response2.content, "html.parser")

    # Find the div elements with the specified attributes
    div_element1 = soup1.find("div", div_attributes1)
    div_element2 = soup2.find("div", div_attributes2)

    # Get the values of the data-test-value attributes
    value1 = div_element1.get("data-test-value") if div_element1 is not None else "venue-online"
    value2 = div_element2.get("data-test-value") if div_element2 is not None else "venue-online"

    # Check if the values have changed since the previous iteration
    messages = []
    if prev_value1 is None:
        messages.append(f"{datetime.datetime.now()} - Initial value of {div_attributes1} for restaurant 1: {value1}")
    elif prev_value1 != value1:
        messages.append(
            f"{datetime.datetime.now()} - Value of {div_attributes1} for restaurant 1 has changed from {prev_value1} to {value1}")
        winsound.Beep(500, 2000)
    else:
        messages.append(
            f"{datetime.datetime.now()} - Value of {div_attributes1} for restaurant 1 has not changed: {value1}")

    if prev_value2 is None:
        messages.append(f"{datetime.datetime.now()} - Initial value of {div_attributes2} for restaurant 2: {value2}")
    elif prev_value2 != value2:
        messages.append(
            f"{datetime.datetime.now()} - Value of {div_attributes2} for restaurant 2 has changed from {prev_value2} to {value2}")
        winsound.Beep(500, 2000)
    else:
        messages.append(
            f"{datetime.datetime.now()} - Value of {div_attributes2} for restaurant 2 has not changed: {value2}")

    print("\n".join(messages))

    # Update the previous value variables
    prev_value1 = value1
    prev_value2 = value2

    # Update the iteration count
    iteration_count += 1

    # Wait for the specified interval before checking again
    time.sleep(check_interval)
