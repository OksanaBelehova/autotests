# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
from time import sleep

sbis_site = 'https://fix-online.sbis.ru/'
sbis_site_dialogs = 'https://fix-online.sbis.ru/page/dialogs'
driver = webdriver.Chrome()
user_login, user_password = 'template22', 'template!44'
find_name = 'Печатная Вероника'
try:
    driver.get(sbis_site)
    sleep(1)
    # Авторизация
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login, 'Логин не подходит'
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER), 'Пароль не подходит'
    sleep(2)
    assert driver.current_url == sbis_site, 'Неверный url в адресной строке'
    sleep(2)

    # Переходим в Контакты
    contacts_for_first_click = driver.find_element(By.CSS_SELECTOR, '[data-qa="NavigationPanels-Accordion__title"].NavigationPanels-Accordion__title.NavigationPanels-Accordion__title_level-1')
    assert contacts_for_first_click.is_displayed(), 'Нет вкладки контакты'
    action_chains = ActionChains(driver)
    sleep(2)
    action_chains.click(contacts_for_first_click)
    action_chains.perform()
    sleep(1)
    contacts_for_second_click = driver.find_element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle.NavigationPanels-SubMenu__title-with-separator.NavigationPanels-Accordion__prevent-default')
    action_chains.click(contacts_for_second_click)
    action_chains.perform()
    sleep(1)
    assert driver.current_url == sbis_site_dialogs, 'Неверный url в адресной строке'
    sleep(1)

    # Нажимаем + добавить сообщение
    plus_click = driver.find_element(By.CSS_SELECTOR, '.icon-RoundPlus')
    assert plus_click.is_displayed(), 'Нет кнопки добавить сообщение'
    action_chains = ActionChains(driver)
    action_chains.click(plus_click)
    action_chains.perform()
    sleep(1)

    # Ищем пользователя
    find_user = driver.find_element(By.CSS_SELECTOR, '.controls-Popup.ws-float-area-show-complete .controls-Field')
    sleep(1)
    assert find_user.is_displayed(), 'Нет поиска'
    find_user.send_keys(find_name)
    sleep(1)

    # Выбираем пользователя из списка
    choose = driver.find_element(By.CSS_SELECTOR, '[attr-data-qa="key-a8c053e8-1d41-4efe-b66b-bcf720116bf3"]')
    assert choose.is_displayed(), 'Нет пользователя в списке'
    choose.click()
    sleep(2)

    # Вставляем текст сообщения
    message = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    assert message.is_displayed(), 'Поле ввода для сообщения не отображается'
    message.send_keys('Сообщение от автотеста')
    sleep(2)

    # Отправляем сообщение
    button_send_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    assert button_send_message.is_displayed(), 'Нет кнопки отправить сообщение'
    button_send_message.click()
    sleep(2)

    # Находим поиск и вводим наш текст
    search_message = driver.find_element(By.CSS_SELECTOR, '.controls-Field')
    assert search_message.is_displayed(), 'Нет поиска'
    search_message.send_keys('Сообщение от автотеста')
    sleep(2)
    search_button = driver.find_element(By.CSS_SELECTOR, '.controls-Button__text_clickable_bg-same')
    assert search_button.is_displayed(), 'Нет кнопки найти'
    search_button.click()
    sleep(2)

    # Ищем наше не прочитанное сообщение
    message_item = driver.find_element(By.CSS_SELECTOR, '.msg-dialogs-item_unread')
    assert message_item.is_displayed(), 'Сообщение не отобржается'

    # Наводим на сообщение и удаляем его
    action_chains = ActionChains(driver)
    action_chains.move_to_element(message_item)
    action_chains.context_click(message_item)
    action_chains.perform()
    sleep(2)
    del_message = search_message = driver.find_element(By.CSS_SELECTOR, '[title="Перенести в удаленные"]')
    del_message.click()
    sleep(2)

    # Проверяем отображение заглушки
    hint_message = driver.find_element(By.CLASS_NAME, 'hint-Template-Wrapper__hint_emptyFilteredTemplate')
    assert hint_message.is_displayed(), 'Заглушка не отображается'

    # Еще раз инициируем поиск
    search_button = driver.find_element(By.CSS_SELECTOR, '[data-qa="Search__searchButton"]')
    assert search_button.is_displayed(), 'Лупа не отображается'
    search_button.click()
    sleep(2)

    # Проверяем отображение заглушки
    hint_message = driver.find_element(By.CLASS_NAME, 'hint-Template-Wrapper__hint_emptyFilteredTemplate')
    assert hint_message.is_displayed(), 'Заглушка не отображается'

finally:
    driver.quit()
