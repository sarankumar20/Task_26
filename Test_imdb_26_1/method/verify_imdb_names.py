
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException, ElementNotInteractableException
from Test_imdb_26_1.elements_selector.locator import Element
class Advance_search_fields(Element):

    def __init__(self, driver):
        self.driver = driver

    def click_signin_popup(self):
        popup =self.driver.find_element(by=By.XPATH, value=self.sign_value)
        assert self.driver.find_element(by=By.LINK_TEXT, value='Sign In').is_displayed()
        signin_close = self.driver.find_element(by=By.XPATH, value=self.sign_close_icon)
        if popup.is_displayed():
            signin_close.click()
        else:
            print("its not opening")

    def click_and_enter_value_name_field(self, name_text):
        try:
            self.driver.execute_script("window.scrollBy(0,300)")
            wait = WebDriverWait(self.driver, 10)
            name_dropdown =wait.until(ec.element_to_be_clickable(self.dropdown_name))
            name_dropdown.click()
            name_input_box = wait.until(ec.presence_of_element_located(self.input_text_name))
            name_input_box.send_keys(name_text)
            see_result_button =wait.until(ec.element_to_be_clickable(self.see_result))
            action = ActionChains(self.driver)
            action.move_to_element(see_result_button).click().perform()
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")

    def click_and_enter_value_date_field(self, date_from, date_to):
        try:
            link = "https://www.imdb.com/search/name/"
            self.driver.execute_script("window.scrollBy(0,500)")
            wait = WebDriverWait(self.driver, 10)
            birthdayDate_dropdown = wait.until(ec.element_to_be_clickable(self.dropdown_birthday))
            birthdayDate_dropdown.click()
            date_start = wait.until(ec.presence_of_element_located(self.from_date))
            date_start.send_keys(date_from)
            date_end = wait.until(ec.presence_of_element_located(self.to_date))
            date_end.send_keys(date_to)
            see_result_button =wait.until(ec.element_to_be_clickable(self.see_result))
            action = ActionChains(self.driver)
            action.move_to_element(see_result_button).click().perform()
            assert self.driver.current_url == link
            print("success{a}".format(a=self.driver.current_url))
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")

    def click_and_select_awards_dropdown(self):
        try:
            self.driver.execute_script("window.scrollBy(0,500)")
            wait = WebDriverWait(self.driver, 10)
            Awards_dropdown = wait.until(ec.element_to_be_clickable(self.dropdown_awards))
            Awards_dropdown.click()
            best_actor_win = wait.until(ec.presence_of_element_located(self.button_actor))
            action = ActionChains(self.driver)
            action.move_to_element(best_actor_win).click().perform()
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")

    def click_and_enter_value_nickname(self):
        try:
            self.driver.execute_script("window.scrollBy(0,700)")
            wait = WebDriverWait(self.driver, 10)
            nick_name = wait.until(ec.element_to_be_clickable(self.dropdown_adult_name))
            nick_name.click()
            radio_butt = wait.until(ec.element_to_be_clickable(self.include_button))
            if radio_butt.is_selected():
                pass
            else:
                radio_butt.click()
        except NoSuchElementException:
            print("NoSuchElement")
        except ElementClickInterceptedException:
            print("ElementClickIntercepted")
        except ElementNotInteractableException:
            print("ElementNotIntractable")





