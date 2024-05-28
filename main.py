from selenium import webdriver
from time import sleep


def get_driver():
    # Options to make browsing easier
    options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument(
        'disable-dev-shm-usage')
    options.add_argument(
        'no-sandbox')
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    options.add_argument('disable-blink-features=AutomationControlled')

    driver = webdriver.Chrome(options=options)
    driver.get('https://www.timeanddate.com/worldclock/')
    return driver


def main():
    driver = get_driver()
    sleep(2)
    element = driver.find_element(by='xpath',
                                  value='/html/body/div[5]/section[1]/div/div[1]/div[1]/div/div[1]/span/span/span[4]')
    return element


print(main().text)
