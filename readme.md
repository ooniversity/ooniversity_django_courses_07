проект сделан в Pycharm 
виртуальная среда включена
интерпретатор -- Python3.7

### requirements.txt
```
Django==1.10
pkg-resources==0.0.0
```


### судя по первому пункту отчета об ошибке --

```  
Test "1_quadratic_app_view" has been failed:
check app's and view's names: 
names must meet the requirements.
```
тест не видит приложения quadratic, файла views.py
я не могу понять почему так происходит, 
потому что на моем нотбуке приложение создано 
и проходит все примеры тест-кейсов



### порядок создания приложения
- создал приложение "quadratic"
- прописал его в settings INSTALLED_APPS
- вписал представдение в pybursa/urls.py без использования namespace соответствующий url назвал "results"
- создал quadratic/templates/results.html
- создал в файле views.py представление с именем "quadratic_results" и необходимыми функциями 



### структура проекта с предыдущими заданиями курса

```
>>> tree -I 'venv|.idea|__pycache__'
.
├── db.sqlite3
├── manage.py
├── polls
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   ├── polls
│   │   │   ├── detail.html
│   │   │   ├── index.html
│   │   │   └── results.html
│   │   └── README.md
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── pybursa
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── views.py
│   └── wsgi.py
├── quadratic
│   ├── admin.py
│   ├── apps.py
│   ├── __init__.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models.py
│   ├── templates
│   │   └── results.html
│   ├── tests.py
│   └── views.py
├── requirements.txt
├── static
│   ├── css
│   │   ├── bootstrap.css
│   │   ├── README.md
│   │   └── style.css
│   ├── fonts
│   │   └── README.md
│   ├── images
│   │   └── README.md
│   ├── js
│   │   ├── bootstrap.js
│   │   ├── jquery_3.3.1.min.js
│   │   └── README.md
│   └── README.md
└── templates
    ├── contact.html
    ├── index.html
    ├── README.md
    ├── student_detail.html
    └── student_list.html

```

### settings.py


```

INSTALLED_APPS = [

    ...

    'quadratic.apps.QuadraticConfig',
]
```

пробовал писать просто quadratic (у меня работало)


### pybursa/urls.py

``` 

urlpatterns = [
    url(r'^quadratic/results/', quadratic_results, name="results"),
       
    ...

]

```

пробовал использоть inqlude и файл quadratic/urls.py 
(у меня работало)

