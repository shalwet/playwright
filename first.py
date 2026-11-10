# ФИО: хлебникова александра
# Дата: 2026-10-11
# Время: 23:19
# Описание изменений: я изменила исходный пример.
# 1. добавила ожидание полной загрузки (wait_for_load_state)
# 2. добавила проверку на наличие url (.to_have_url)
# 3. добавила комментарии к каждому изменению. 
# зачем: для того чтобы код работал стабильно, и пользователь гарантированно попал на нужный ему сайт 


import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")
    
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")
    page.wait_for_load_state() # добавлено: ожидание полной загрузки
    page.get_by_role("link", name="Get started").click()
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()
    expect(page).to_have_url(re.compile("Installation")) # добавлено: проверка что страница имеет URL

# Результат запуска: "==================================================== 2 passed, 1 warning in 4.52s ===================================================="
# Код выполнен без ошибок.