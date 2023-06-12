# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

sbis_site = 'https://test.sbis.ru/'
sbis_title = 'СБИС — экосистема для бизнеса: учет, управление и коммуникации'
driver = webdriver.Chrome()
tensor_ru = 'https://tensor.ru/'
tensor_about = 'https://tensor.ru/about'
try:
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Не верно открыт сайт'
    assert driver.title == sbis_title, 'Не верный заголовок'
    tabs = driver.find_elements(By.CSS_SELECTOR, '.sbisru-Header__menu-item')
    assert len(tabs) == 4, 'Должно быть 4 вкладки'

    contacts = driver.find_element(By.PARTIAL_LINK_TEXT, 'Контакты')
    contacts.click()
    sleep(1)

    logo = driver.find_element(By.CLASS_NAME, 'sbisru-Contacts__logo-tensor')
    logo.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(1)

    power_of_people = driver.find_element(By.XPATH, '//*[contains(text(), "Сила в людях")]')
    assert power_of_people.is_displayed()
    about_lnk = driver.find_elements(By.CLASS_NAME, 'tensor_ru-Index__link')[1]
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", about_lnk)
    sleep(1)
    assert about_lnk.is_displayed()
    about_lnk.click()
    sleep(1)
    assert driver.current_url == tensor_about
finally:
    driver.quit()
