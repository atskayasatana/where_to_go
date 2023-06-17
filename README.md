# Яндекс.Афиша

#### Сайт с интересными локациями Москвы, где на карте города обозначены места и добавлены описания с фото.

Сайт с картой города, на которой обозначены места, рекомендуемые к посещению. При выборе точки на карте, слева появляется подробное описание и фотографии места.

![](https://github.com/atskayasatana/Images/blob/6d513dd8ec3d8e83aee9ae63efa0674e2cb48ea9/main_where_to_go.png)

#### Запуск
Для запуска пользователю нужны Python версии не ниже 3. 
Все настройки окружения вынесены в .env файл, поэтому в директории проекта нужно самостоятельно добавить файл с собственными настройками переменных ниже:
```
SECRET_KEY=
DEBUG=
ALLOWED_HOSTS=
DB_ENGINE= # движок базы данных в настройках DATABASES файла settings.py
DB_NAME= # имя базы данных в настройках DATABASES файла settings.py
STATIC_ROOT=
STATIC_URL=
MEDIA_ROOT=
MEDIA_URL=

```
Проекту нужно создать окружение:
```
conda create -n <имя окружения> python=3.10 anaconda
```

Созданное окружение нужно активировать:

```
conda activate <имя окружения>
```

После активации окружения необходимо установить библиотеки из файла requirements.txt:

```
pip install -r requirements.txt
```
Загрузим все изменения базы данных:
```
python manage.py makemigrations
```
```
python manage.py migrate
```
И запускаем проект:
```
python manage.py runserver
```
Локальная версия сайта находится [здесь](http://127.0.0.1:8000/)

#### Администрирование сайта
Для доступа к админке нужен суперпользователь:
```
python manage.py createsuperuser
```
С созданными логином и паролем нужно перейти по http://127.0.0.1:8000/admin

Пользователю доступны 2 раздела: Images и Places.

![Главная](https://github.com/atskayasatana/Images/blob/6c1a4150eb13de7058472c32848690cc0d9e519d/admin_main_page.png)

В Images добавляются изображения, в Places - описания мест и изображения.

В админке можно добавлять картинки как отдельно в разделе Image, так и сразу при создании новой локации.

![Добавляем картинку](https://github.com/atskayasatana/Images/blob/6c1a4150eb13de7058472c32848690cc0d9e519d/add%20image_1.png)


При добавлении картинки в Images название ей присваивается автоматически.

Все картинки добавленные в Image появятся и в разделе Places.

![Локации](https://github.com/atskayasatana/Images/blob/6c1a4150eb13de7058472c32848690cc0d9e519d/places.png)

Картинки можно перемещать/менять местами. Для этого нужно зажать левую кнопку мыши на серой области Image Image Object. 

![Перетаскивание](https://github.com/atskayasatana/Images/blob/6c1a4150eb13de7058472c32848690cc0d9e519d/drag%20image.png)

Изменения в порядке отобразятся и в области с описанием локации.




