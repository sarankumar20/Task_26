from selenium.webdriver.common.by import By

class Element:
    sign_value = '//div[contains(@class,"ipc-list-card")]'
    sign_close_icon = '//*[@id="imdbHeader"]/div[2]/div[5]/div/div/div/div/div[1]/button'
    dropdown_name = (By.ID, 'nameTextAccordion')
    input_text_name = (By.NAME, 'name-text-input')
    see_result = (By.XPATH, '//button/span[@class="ipc-btn__text"]')
    dropdown_birthday = (By.ID, 'birthDateAccordion')
    from_date = (By.NAME, 'birth-date-start-input')
    to_date = (By.NAME, 'birth-date-end-input')
    dropdown_awards = (By.ID, 'awardsAccordion')
    button_actor = (By.XPATH, '//span[text()="Best Actor-Winning"]')
    dropdown_adult_name = (By.ID, 'adultNamesAccordion')
    include_button = (By.ID, 'include-adult-names')
