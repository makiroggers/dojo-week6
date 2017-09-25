# TOTALLY OPTIONAL SHIT
TIME_ZONE = 'America/Los_Angeles'
AUTH_USER_MODEL = '<<APP_NAME>>.User'
LOGIN_REDIRECT_URL = '<<APP_NAME>>/login/'

LOCAL_APPS = [
    'apps.<<APP_NAME>>',
]

# RECOMMENDED SHIT TO ADD
STATICFILES_DIR = [
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "apps/<<APP_NAME>>/static/"),
    os.path.join(BASE_DIR, "<<PROJECT_NAME>>/static/")
]
FILES_DIR = os.path.abspath(os.path.join(BASE_DIR, '../templates'))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.dirname(__file__), '../<<PROJECT_NAME>>/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# CONSOLE DEBUG TO CHECK DIRECTORIES
print '\n', '\n'
print "BASE DIR..."
print BASE_DIR, '\n', '\n'
print "STATICFILES_DIR..."
print STATICFILES_DIR, '\n', '\n'
print "FILES_DIR..."
print FILES_DIR, '\n', '\n'
print "TEMPLATES_DIR..."
print TEMPLATES[0]['DIRS'], '\n', '\n'
