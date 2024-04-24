from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def automate_web_testing(url=):
    driver = webdriver.Chrome()

    try:
        driver.get(url)

        search_box = driver.find_element_by_name('q')
        search_box.send_keys('Python automation')
        search_box.send_keys(Keys.RETURN)

        assert 'Python automation' in driver.title
        print("Test passed: Search results page title contains 'Python automation'")
    except Exception as e:
        print("Test failed:", e)
    finally:
        driver.quit()

automate_web_testing()
