from .base import *
# you need to set "myproject = 'prod'" as an environment variable
# in your OS (on which your website is hosted)

try:
    if os.environ['DJANGO_ENV'] == 'prod':
        from .prod import *
        print("Production settings loaded from prod.py file")
    elif os.environ['DJANGO_ENV'] == 'test':
        from .test import *
        print("test settings loaded from test.py file")
    elif os.environ['DJANGO_ENV'] == 'dev':
        from .dev import *
        print("development settings loaded from dev.py file")
    else:
        print("Environment value invalid!")
except Exception as e:
    print("exception {} occured while initiating settings in __init__.py file.".format(e))
    from .local import *
    print("local settings loaded from local.py file")
