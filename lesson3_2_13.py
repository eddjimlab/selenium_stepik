from selenium import webdriver
import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestLinks(unittest.TestCase):

    def fill_form(self, link):
        self.browser = webdriver.Chrome()
        self.browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = self.browser.find_element_by_css_selector('.first_block .first')
        input1.send_keys("first")
        input2 = self.browser.find_element_by_css_selector('.first_block .second')
        input2.send_keys("second")
        input3 = self.browser.find_element_by_css_selector('.first_block .third')
        input3.send_keys("third")

        input4 = self.browser.find_element_by_css_selector('.second_block .first')
        input4.send_keys(".second_block .first")
        input5 = self.browser.find_element_by_css_selector('.second_block .second')
        input5.send_keys(".second_block .second")

        # Отправляем заполненную форму
        button = self.browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        # time.sleep(1)
        welcome_text_elt = WebDriverWait(self.browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )
        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text
        return welcome_text

    def test_first_link(self):
        link1 = "http://suninjuly.github.io/registration1.html"
        self.assertEqual("Congratulations! You have successfully registered!", self.fill_form(link1), "Link1 is OK")

    def test_second_link(self):
        link2 = "http://suninjuly.github.io/registration2.html"
        self.assertEqual("Congratulations! You have successfully registered!", self.fill_form(link2), "Link2 is OK")

    def tearDown(self):
        # time.sleep(2)
        self.browser.quit()


if __name__ == '__main__':
    unittest.main()
