# drf

<b>Important commands</b>

django-admin startproject onlineshop

python manage.py startapp products

python manage.py makemigrations 

python manage.py migrate

<b>Add this in main project urls file for static file</b>

if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
	
<b>Adds in settings.py</b>

MEDIA_ROOT = "uploads"

MEDIA_URL = "/media/"

<b>Install and add Tinymce  texteditor</b>

**Install Tinymce using pip**

pip install django-tinymce4-lite

**add in INSTALLEDAPP**

'tinymce',

**Add in urlpatterns of main project urls.py file**

path('tinymce/', include('tinymce.urls')),

**Import in models.py file**

from tinymce import HTMLField

#Repalce TextField 

content = HTMLField()

**Add this in setting.py file**


TINYMCE_DEFAULT_CONFIG = {
    'height': 360,
    'width': 1120,
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'modern',
    'plugins': '''
            textcolor save link image media preview codesample contextmenu
            table code lists fullscreen  insertdatetime  nonbreaking
            contextmenu directionality searchreplace wordcount visualblocks
            visualchars code fullscreen autolink lists  charmap print  hr
            anchor pagebreak
            ''',
    'toolbar1': '''
            fullscreen preview bold italic underline | fontselect,
            fontsizeselect  | forecolor backcolor | alignleft alignright |
            aligncenter alignjustify | indent outdent | bullist numlist table |
            | link image media | codesample |
            ''',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,
    }
