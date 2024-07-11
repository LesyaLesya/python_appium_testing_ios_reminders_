## Описание проекта

Автотесты для приложения Reminders (IOS) на python + pytest + appium + xcode.

____

## Установка проекта

- Скачать репозиторий на свою машину:

```
git clone https://github.com/LesyaLesya/python_appium_testing_ios_reminders_.git
```

- Перейти в директорию скачанного репозитория

- Установить и активировать виртуальное окружение (для запуска тестов через консоль/ide)

```
python3 -m venv venv
source venv/bin/activate
```
- Обновить PIP и установить зависимости (для запуска тестов через консоль/ide)

```
pip install -U pip
pip install -r requirements.txt
```

- Выбрать интерпретатор для проекта (для запуска тестов через консоль/ide)

- Создать файл .env
```
PLATFORM_NAME="ios"
UDID=ИДЕНТИФИКАТОР ДЕВАЙСА В XCODE
BUNDLE_ID="com.apple.reminders"
APPIUM_SERVER_URL="http://localhost:4723"
```


### Необходимые шаги для установки appium и запуска симулятора (инструкция для MacOs)
- Установить Xcode
- Установить NodeJs
- Установить Appium
```
npm install -g Appium
```
- Установить драйвер
```
appium driver install xcuitest
```

- Можно установить Appium Inspector для написания новых тестов, поиска элементов 
https://github.com/appium/appium-inspector 

- Запустить Xcode - Window -> Device and simulators -> Simulators (выбрать девайс) -> 
скопировать идентификатор Identifier и указать его в файле .env

- Запустить appium сервер
```
appium
```
____

## Запуск тестов

В Terminal выполнить команду:

```
pytest -m marker tests/
```
где:
- -m - маркер, какую группу тестов запускать.



#### Получить отчет Allure 

- В Terminal выполнить команду, в качестве параметра указав путь до исполняемого файла allure на вашей машине:

```
./run_allure_report.sh /path/to/allure/bin
Пример: ./run_allure_report.sh /Applications/allure/bin/allure
```
