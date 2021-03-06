""" This class consist all necessary web elements extensions methods
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

import ioc_config
from utils.enums.field_type import FieldType
from utils.waits import Waits


class WebElementsExtensions(Waits):

    def send_keys(self, locator, string):
        element = self.find_element(locator)
        element.send_keys(string)

    def send_key_one_by_one(self, locator, string):
        for x in string:
            self.send_keys(locator, x)

    def switch_to_iframe_and_send_keys(self, iframe_name, locator, string):
        self.switch_to_iframe(iframe_name)
        element = self.find_element(locator)
        element.send_keys(string)
        self.switch_to_default_iframe()

    def switch_to_iframe_and_send_keys_one_by_one(self, iframe_name, locator, string):
        self.switch_to_iframe(iframe_name)
        if string != 'None':
            self.send_key_one_by_one(locator, string)
        self.switch_to_default_iframe()

    def switch_to_iframe_and_send_keys_by_java_script(self, iframe_name, locator, string):
        # self.switch_to_iframe(iframe_name)
        # element = self.find_element(locator)
        self._browser.execute_script("window.frames['st-card-number-iframe'].document.getElementById('st-card-number-input').value='123'")
        self.switch_to_default_iframe()

    def switch_to_iframe_and_click(self, iframe_name, locator):
        self.switch_to_iframe(iframe_name)
        element = self.find_element(locator)
        element.click()
        self.switch_to_default_iframe()

    def switch_to_iframe_and_get_text(self, iframe_name, locator):
        self.switch_to_iframe(iframe_name)
        element = self.get_text(locator)
        self.switch_to_default_iframe()
        return element

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def click_with_wait(self, locator):
        self.wait_for_ajax()
        element = self.wait_for_element(locator)
        element.click()

    def find_element(self, locator):
        # self.wait_for_ajax()
        element = self._browser.find_element(*locator)
        # * collects all the positional arguments in a tuple
        return element

    def is_element_displayed(self, locator):
        element = self._browser.find_element(*locator)
        return element is not None

    def is_iframe_displayed(self, iframe_name):
        try:
            self._browser.switch_to.frame(iframe_name)
            return True
        except:
            return False

    def find_elements(self, locator):
        # self.wait_for_ajax()
        elements = self._browser.find_elements(*locator)
        return elements

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def get_text_with_wait(self, locator):
        self.wait_for_element(locator)
        element = self.find_element(locator)
        return element.text

    def get_css_value_with_wait(self, locator, property):
        self.wait_for_element(locator)
        element = self.find_element(locator)
        css_value = element.value_of_css_property(property)
        return css_value

    def clear_input(self, locator):
        element = self.find_element(locator)
        element.clear()

    def is_checkbox_selected(self, locator):
        element = self.find_element(locator)
        return element.is_selected()

    def get_element_attribute(self, locator, attribute_name):
        element = self.find_element(locator)
        return element.get_attribute(attribute_name)

    def is_element_enabled(self, locator):
        element = self.find_element(locator)
        is_enabled = element.is_enabled()
        return is_enabled

    def switch_to_iframe_and_get_element_attribute(self, iframe_name, locator, attribute_name):
        self.switch_to_iframe(iframe_name)
        element = self.find_element(locator)
        attribute = element.get_attribute(attribute_name)
        self.switch_to_default_iframe()
        return attribute

    def switch_to_iframe_and_check_is_element_enabled(self, iframe_name, locator):
        self.switch_to_iframe(iframe_name)
        element = self.find_element(locator)
        is_enabled = element.is_enabled()
        self.switch_to_default_iframe()
        return is_enabled

    def switch_to_iframe_and_get_css_value(self, iframe_name, locator, property):
        self.switch_to_iframe(iframe_name)
        element = self.find_element(locator)
        css_value = element.value_of_css_property(property)
        self.switch_to_default_iframe()
        return css_value

    def scroll_directly_to_element(self, locator):
        element = self.find_element(locator)
        self._browser.execute_script("arguments[0].scrollIntoView();", element)

    def click_by_javascript(self, locator):
        element = self.find_element(locator)
        self._browser.execute_script("arguments[0].click();", element)

    def enter(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.RETURN)

    def select_element_from_list(self, locator, element_number):
        select = Select(self._browser.find_elements(*locator))
        select.select_by_index(element_number)

    def switch_to_iframe(self, iframe_name):
        self.wait_until_iframe_is_presented_and_switch_to_it(iframe_name)

    def switch_to_default_iframe(self):
        self.switch_to_default_content()
        if len(self._browser.find_elements(By.ID, 'st-parent-frame')) > 0:
            self.switch_to_iframe(FieldType.PARENT_IFRAME.value)

    def switch_to_parent_iframe(self):
        self.switch_to_parent_frame()
