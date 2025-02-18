# Пример проекта автотестов для сайта [T‑Ж](https://t-j.ru)
> T‑Ж – журнал про ваши деньги. Этот ресурс предлагает актуальные статьи, аналитические материалы и интерактивные сервисы, помогающие пользователям разбираться в финансовых вопросах и принимать обоснованные решения.

### Используемые технологии
<p align="center">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/chrome/chrome-original-wordmark.svg" height="40" width="40" />
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg" height="40" width="40" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/82/Telegram_logo.svg" width="40" height="40"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg" width="40" height="40"/>
</p>

## Покрываемый функционал
- Проверка title страницы T‑Ж
- Поиск инструментов на сайте T‑Ж
- Проверка навигационного меню 
- Cценарий работы калькулятора

## Запуск тестов

### Локально
Важно! Перед запуском нужно создать файл `.env` и указать в нём SELENOID_LOGIN, SELENOID_PASS и SELENOID_URL

Для запуска тестов локально выполните следующие шаги:
1. Склонировать репозиторий.
2. Открыть проект в PyCharm.
3. В терминале выполнить следующие команды:
   ```
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   
### С помощью [Jenkins](https://jenkins.autotests.cloud/job/C17-gonchrrv-lesson_14/)
#### Для запуска автотестов необходимо:
- Открыть [джобу](https://jenkins.autotests.cloud/job/C17-gonchrrv-lesson_14/) в Jenkins.
- Нажать на кнопку **Build with Parameters**.
- Выбрать необходимые значения параметров `BROWSER_TYPE` и `BROWSER_VERSION`.
- Нажать на **Build**.

<img src="images/screenshots/Jenkins_build.png" alt="Jenkins Build" width="600">

## Отчет о прохождении тестов (Allure)

### Локально
Для получения отчёта нужно ввести команду 
```allure serve allure-results```

Ниже представлен пример Allure отчёта:

<img src="images/screenshots/allure_report_example.png" alt="Allure Report" width="600">

Видео прохождения теста:

<img src="images/screenshots/allure_video_report.gif" alt="Allure Report" width="600">

Подробные инструкции по работе с Allure можно найти по [ссылке](https://allurereport.org/docs/).


### В проекте реализована интеграция с Allure TestOps и Atlassian Jira
Интеграция с Allure TestOps:
<img src="images/screenshots/allure_test_ops_1.png" alt="Allure TestOps" width="600">
<img src="images/screenshots/allure_test_ops_2.png" alt="Allure TestOps" width="600">

Интеграция с Atlassian Jira:
<img src="images/screenshots/atlassian_jira_1.png" alt="Allure TestOps" width="600">
<img src="images/screenshots/atlassian_jira_2.png" alt="Allure TestOps" width="600">



### В проекте настроена отправка краткого отчёта в Telegram
<img src="images/screenshots/allure_tg_report.png" alt="Telegram Allure Report" width="600">
