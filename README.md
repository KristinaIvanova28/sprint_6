# Автотесты для «Яндекс.Самокат» — Sprint 6

Этот проект содержит автоматизированные UI-тесты для учебного сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/), разработанного в рамках обучения в Яндекс.Практикуме.

Тесты написаны с использованием:
- **Selenium WebDriver** — для управления браузером
- **Page Object Model** — для структурирования кода
- **Pytest** — как фреймворк для тестирования
- **Allure** — для генерации красивых отчётов
- **webdriver-manager** — для автоматической установки драйверов

---

## 🧰 Технологии

- Python 3.8+
- Selenium 4
- Pytest
- Allure
- Firefox (через geckodriver)
- Git
- Page Object Model

---

## 📦 Установка и настройка

### 1. Клонируй репозиторий

```bash
git clone https://github.com/ваш-логин/Sprint_6.git
cd Sprint_6

### 2. Создай и активируй виртуальное окружение
python -m venv venv

На macOS / Linux:
source venv/bin/activate

На Windows:
venv\Scripts\activate

### 3. Установи зависимости
pip install -r requirements.txt

🧪 Запуск тестов
Запусти все тесты:
pytest

Запусти с подробным выводом:
pytest -v

Запусти конкретный файл:
pytest tests/test_faq.py -v

Результаты тестов сохраняются в папку allure-results.

 
📊 Генерация Allure-отчёта

Убедись, что у тебя установлен Allure CLI.

Установка Allure (если не установлен)

macOS:
brew install allure

Linux (Ubuntu):
sudo apt-get install allure-commandline

Windows (через Chocolatey):
choco install allure

Генерация и просмотр отчёта
allure serve allure-results
Это запустит локальный сервер и откроет отчёт в браузере. 

Или вручную:

allure generate allure-results -o allure-report --clean
allure open allure-report
 
🌿 Ветки

main — основная ветка с рабочей версией
develop — ветка разработки, основная для написания кода

✅ Задачи проекта

Проверить раскрытие ответов в разделе «Вопросы о важном»
Протестировать полный позитивный сценарий заказа самоката
Проверить переходы по логотипам (Самокат и Яндекс)
Использовать параметризацию
Сгенерировать Allure-отчёт

