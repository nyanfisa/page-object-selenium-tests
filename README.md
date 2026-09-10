# UI Automation Framework (Page Object Model) `🚧 Work in progress`

Фреймворк для автоматизированного тестирования веб-интерфейсов на Python с использованием Selenium WebDriver и pytest.

Проект построен на паттерне **Page Object Model (POM)**, что делает код тестов переиспользуемым, читаемым и легко расширяемым.

---

## Стек технологий

- **Python 3.14**
- **pytest** — тестовый фреймворк
- **Selenium WebDriver** — управление браузером
- **Page Object Model** — архитектурный паттерн
- **python-dotenv** — хранение конфиденциальных данных в `.env`
- **Git** — контроль версий

---

## Структура проекта

selenium_testing/
├── pages/
│   ├── __init__.py           
│   ├── base_page.py          
│   ├── main_page.py          
│   ├── login_page.py         
│   ├── register_page.py      
│   └── locators.py           
├── test_main_page.py         
├── conftest.py               
├── requirements.txt          
├── .env.example              
├── .gitignore                
└── README.md                 

---

## Архитектура

### BasePage
Базовый класс, от которого наследуются все страницы. Содержит общие методы:
- `open()` — открыть страницу по URL
- `is_element_present(how, what)` — проверить наличие элемента
- `should_be_on_page(expected_path)` — проверить текущий URL через `urlparse`

### Page Objects
Каждая страница — отдельный класс, который знает:
- свой URL,
- свои локаторы,
- свои действия (методы)
   
Locators
Все локаторы вынесены в locators.py и сгруппированы по страницам. 

## Установка и запуск

1. Клонировать репозиторий
```bash
git clone https://github.com/nyanfisa/page-object-selenium-tests.git
cd page-object-selenium-tests
```
2. Создать и активировать виртуальное окружение
```bash
python -m venv venv
```
# Windows:
```bash
venv\Scripts\activate
```
# Linux/macOS:
```bash
source venv/bin/activate
```

3. Установить зависимости
```bash
pip install -r requirements.txt
```

5. Запустить тесты

```bash
pytest -sv
```

Что покрывают тесты:

- Открытие главной страницы
- Проверка наличия ссылки на страницу логина
- Переход на страницу авторизации
- Проверка URL страницы логина
- Переход на страницу регистрации
- Проверка наличия всех элементов формы регистрации (поля email, выпадающий список страны, кнопка создания аккаунта)


## Возможные улучшения

Добавить отчёты Allure
Настроить запуск в CI (GitHub Actions)
Добавить параметризацию тестов
Расширить покрытие (корзина, вишлист, поиск по меткам)

## Автор
nyanfisa

