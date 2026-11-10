# ФИО: хлебникова александра
# Дата: 2026-10-11
# Время: 22:35
# Описание: я скопировала этот код из раздела "Writing tests" и запустила его. он запускает браузер, проверяет,
# что на главной странице заголовок "Playwright" и что когда переходишь по ссылке "Get started", то она
# ведет на страницу с заголовком "Installation"



import re
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    page.goto("https://playwright.dev/")

    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    page.goto("https://playwright.dev/")

    page.get_by_role("link", name="Get started").click()

    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

# Результат запуска: "==================================================== 2 passed, 1 warning in 6.39s ===================================================="
# Код выполнен без ошибок.