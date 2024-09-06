from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time


def check_ordering_paused(url):
    options = Options()
    options.add_argument('--headless')  # Run the Edge WebDriver in headless mode

    # Initialize the Edge WebDriver with the options
    driver = webdriver.Edge(options=options)

    driver.get(url)
    time.sleep(2)  # Wait for the page to fully load

    # Get the full page text
    page_text = driver.find_element(By.TAG_NAME, 'body').text.lower()

    driver.quit()

    # Check if "Ordering paused" or "closed" is present in the text
    if "ordering paused" in page_text or "closed" in page_text:
        return "Ordering paused"
    else:
        return "venue-online"
