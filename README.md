# **Cервис помощи в получении здоровых привычек.**                                                       
_(project name: healthy_habits_tracker)_                                                                                                 
                                                                                                                                    
**Цель проекта:** Реализовать приобретение новых полезных привычек и искоренение старых плохих привычек в соответствии 
с книгой «Атомные привычки», написанной в 2018 году Джеймсом Клиром. В рамках учебного курсового проекта реализовать 
бэкенд-часть SPA веб-приложения.                                                              
                                                                                                                                    
                                                                                                                                    
### Реализованные возможности:                                                                                                      
_MVP_                                                                                                                 
- Модель привычек добавлена.                                               
- Эндпоинты для работы с фронтендом реализованы.  
- Приложение для работы с Telegram и рассылками напоминаний создано.

                                                                                                                                    
### Особенности                                                                                                                     
- Сервис реализован на фреймворки Django 4.2                                                                                        
- Проект использует djangorestframework.                                                                                 
- Отлаживание задач реализовано через Celery и Celery-beat                                                                                    
- Для наследования в сущности пользователь, используется модель `AbstractUser`
- Настроен CORS
- Интеграция с Telegram реализовано через API Telegram
                                                                                                                                    
                                                                                                                                    
### Логика работы сервиса                                                                                                           
- Создайте привычку использую для примера предложение: 

я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО]

- За каждую полезную привычку вознаградите себя или сразу после сделайте приятную привычку. 
- Установите время выполнения привычке не больше двух минут.
- Нельзя не выполнять привычку более 7 дней. Например, привычка может повторяться раз в неделю, но не раз в 2 недели. 
- За одну неделю необходимо выполнить привычку хотя бы один раз.
- Не должно быть заполнено одновременно и поле вознаграждения, и поле связанной привычки. Можно заполнить только 
одно из двух полей

Например: в качестве полезной привычки вы будете выходить на прогулку вокруг квартала сразу же после ужина. Вашим 
вознаграждением за это будет приятная привычка — принять ванну с пеной. То есть такая полезная привычка будет иметь 
связанную привычку.

Другой пример: полезная привычка — «я буду не опаздывать на еженедельную встречу с друзьями в ресторан». В 
качестве вознаграждения вы заказываете себе десерт. В таком случае полезная привычка имеет вознаграждение, но не 
приятную привычку.

                                                                                                                                    
### Некоторые важные понятия
**Привычка** - конкретное действие, которое можно уложить в одно предложение: я буду [ДЕЙСТВИЕ] в [ВРЕМЯ] в [МЕСТО].

**Полезная привычка** — это само действие, которое пользователь будет совершать и получать за его выполнение определенное 
вознаграждение (приятная привычка или любое другое вознаграждение).

**Приятная привычка** — это способ вознаградить себя за выполнение полезной привычки. Приятная привычка указывается в 
качестве связанной для полезной привычки (в поле «Связанная привычка»).                                

                                                                                                                                    
### Функционал                                                                                                                      
#### пользователи:
* **Имеет** доступ только к своим привычкам по механизму CRUD.
* **Может** видеть список публичных привычек без возможности их как-то редактировать или удалять. 
                                                                                                                                    
                                                                                                                                    
### Приложение "Core"
#### Модель Привычка:
- **Пользователь** — создатель привычки.
- **Место** — место, в котором необходимо выполнять привычку.
- **Время** — время, когда необходимо выполнять привычку.
- **Действие** — действие, которое представляет собой привычка.
- **Признак приятной привычки** — привычка, которую можно привязать к выполнению полезной привычки.
- **Связанная привычка** — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для 
приятных.
- **Периодичность** (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
- **Вознаграждение** — чем пользователь должен себя вознаградить после выполнения.
- **Время на выполнение** — время, которое предположительно потратит пользователь на выполнение привычки.
- **Признак публичности** — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример 
чужие привычки.

#### Валидаторы
- Исключить одновременный выбор связанной привычки и указания вознаграждения.
- Время выполнения должно быть не больше 120 секунд.
- В связанные привычки могут попадать только привычки с признаком приятной привычки.
- У приятной привычки не может быть вознаграждения или связанной привычки.
- Нельзя выполнять привычку реже, чем 1 раз в 7 дней.

#### Пагинация
Для вывода списка привычек реализована пагинация с выводом по 5 привычек на страницу.



### Эндпоинты
- Регистрация.
- Авторизация.
- Список привычек текущего пользователя с пагинацией.
- Список публичных привычек.
- Создание привычки.
- Редактирование привычки.
- Удаление привычки.


### Безопасность
Для проекта необходимо настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере.


### Документация
Для реализации экранов силами фронтенд-разработчиков настроен вывод документации. При необходимости 
эндпоинты, на которые документация не будет сгенерирована автоматически, описаны вручную.


### Интеграция
Для полноценной работы сервиса реализована работа с отложенными задачами для напоминания о том, в какое время какие 
привычки необходимо выполнять.

Интегрирован сервис с мессенджером Телеграм, который будет заниматься рассылкой уведомлений.

                                                                                                                                    
### Алгоритм запуска сервиса                                                                                                        
                                                                                                                                    
1. Клонируйте содержимое данного репозитория к себе.                                                                                
2. Установите зависимости в venv: `pip3 install -r requirements.txt`.                                                               
3. Создайте базу данных, например, через консоль:                                                                                   
   ```                                                                                                                                 
   psql -U postgres                                                                                                                    
   create database healthy_habits_tracker;                                                                                                   
   ```                                                                                                                                 
4. В .env добавите данные из env.sample.                                                                                            
5. Запустите кэширование с помощью redis.                                                                                           
6. Создайте суперюзера использую команду `python3 manage.py csu`.                                                                  
7. Запустите периодические задачи 
   - Celery worker `celery -A my_project worker —loglevel=info`.
   - Планировщик Celery beat `celery -A my_project beat —loglevel=info`.                                        
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
                                                                                                                                    
### Данный проект это курсовая работа № 7 модуля "DRF" в курсе "Python-разработчик"                                              
_Данный учебный проект состоит из одной частей._                                                                                     

### Описание задач
- [x] Добавлены необходимые модели привычек.                                               
- [x] Реализованы эндпоинты для работы с фронтендом.  
- [ ] Создано приложение для работы с Telegram и рассылками напоминаний.
                                                                                                                                     
**Критерии успешного выполнения данной курсовой:**                                                                                                               
- [x] Настроена CORS.
- [ ] Настроена интеграцию с Телеграмом.
- [x] Реализована пагинация.
- [x] Использовано переменные окружения.
- [x] Все необходимые модели описаны или переопределены.
- [x] Все необходимые эндпоинты реализованы.
- [x] Настроены все необходимые валидаторы.
- [x] Описаны права доступа.
- [ ] Настроены отложенные задачи через Celery.
- [ ] Проект покрыли тестами как минимум на 80%.
- [ ] Код оформлен в соответствии с лучшими практиками.
- [ ] Имеется список зависимостей.
- [ ] Результат проверки Flake8 равен 100%, при исключении миграций.
- [ ] Решение выложили на GitHub.                                                 
