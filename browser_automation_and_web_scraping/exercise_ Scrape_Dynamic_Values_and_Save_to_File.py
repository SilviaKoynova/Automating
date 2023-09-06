from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime as dt

service = Service(r"C:\Users\Силвиа\Downloads\chromedriver.exe")

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument('disable-infobars')
    options.add_argument('start-maximized')
    options.add_argument('disable-dev-shm-usage')
    options.add_argument('no-sandbox')
    options.add_experimental_option('excludeSwitches',['enable-automation'])
    options.add_argument('disable-blink-features=AtomationControlled')

    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://automated.pythonanywhere.com/")
    return driver


def clean_text(text):
  """Extract only the temperature from text"""
  output = float(text.split(": ")[1])
  return output

def write_file(text):
    filename = f"{dt.now().strftime('%Y-%m-%d.%H-%M-%S')}.txt"
    with open(filename, 'w') as file:
        file.write(text)

def main():
    driver = get_driver()
    time.sleep(2)
    while True:
        element = driver.find_element(by='xpath', value='/html/body/div[1]/div/h1[2]')
        text = str(clean_text(element.text))
        write_file(text)


print(main())