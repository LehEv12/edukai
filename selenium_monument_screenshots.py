from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.options import Options
import time
import os


def take_pictures(latitude, longitude, altitude, heading, pitch, tilt, roll):
    # Path to the Firefox profile
    profile_path = 'C:\\Users\\evanl\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\198ghikw.Earth'

    # Configure GeckoDriver service
    service = Service(GeckoDriverManager().install())

    # Configure Firefox options to use the specified profile
    options = Options()
    options.profile = profile_path

    # Start Firefox browser with the specified options
    driver = webdriver.Firefox(service=service, options=options)

    # List of 'h' parameter values
    h_values = ['0', '60', '120', '180', '240', '300']

    # Base URL without the 'h' parameter
    base_url = f"https://earth.google.com/web/@{latitude},{longitude},{altitude}a,{heading}d,{pitch}y,{{h}}h,{tilt}t,{roll}r/data=OgMKATA"

    for h in h_values:
        # Create the complete URL with the current value of the 'h' parameter
        url = base_url.format(h=h)

        # Open the web page
        driver.get(url)

        # Wait for the page to fully load
        time.sleep(20)

        # Take a screenshot and save the image with a name reflecting the value of the 'h' parameter
        screenshot_path = f'screenshot_{h}.png'
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved in {screenshot_path}")

    # Close the browser
    driver.quit()