from POMDemo.Locators.locators import Locators
class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.welcome_link_id = Locators.welcome_link_id
        self.logout_link_linkText = Locators.logout_link_linkText



    def clickWelcome(self):
        self.driver.find_element_by_id(self.welcome_link_id).click()

    def clickLogout(self):
        self.driver.find_element_by_link_text(self.logout_link_linkText).click()







