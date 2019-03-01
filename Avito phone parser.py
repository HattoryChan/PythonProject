from selenium import webdriver
from time import sleep

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox()
        self.navigate()

    def take_screenshot(self):
        self.driver.save_screenshot('avito_screenshot.png')
    
    def navigate(self):
        self.driver.get('https://www.avito.ru/chelyabinsk/telefony/iphone_6_plus_1625790112')

        sleep(5)
        button = self.driver.find_element_by_xpath('//button[@class="button item-phone-button js-item-phone-button button-origin button-origin-blue button-origin_full-width button-origin_large-extra item-phone-button_hide-phone item-phone-button_card js-item-phone-button_card"]')
        
                                                   
        button.click()

        sleep(3)

        self.take_screenshot()






def main():
    b = Bot()

main()

if __name__ == '_main_':
    main()
