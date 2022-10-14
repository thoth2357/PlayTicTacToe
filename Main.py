from WebDriver import WebDriver








web_driver = WebDriver()
driver = web_driver.get_driver_headless()
web_driver.get_page(driver, "https://www.google.com")
